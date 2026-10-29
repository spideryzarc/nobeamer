# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.40", "pillow>=10"]
# ///
"""Design lab for Marp themes: render, contact sheets, layout lint, visual diff, A/B variants.

Usage (from the project root):
    uv run lab/swiss_lab.py sheet                      # render the deck, lint, write contact sheet
    uv run lab/swiss_lab.py lint [--json]              # numeric layout checks, no images
    uv run lab/swiss_lab.py baseline                   # freeze current renders as reference
    uv run lab/swiss_lab.py diff                       # compare with baseline, sheet of changed slides
    uv run lab/swiss_lab.py ab -s 4,5 -v tight=":root{--gutter:32px}" -v wide=lab/wide.css

Common options: --deck FILE (default demo-swiss.marp.md), --theme FILE, -s/--slides "1,3-5".
A variant value is inline CSS or a path to a .css file; it is injected as a global <style> into the deck,
so `:root { ... }` overrides theme tokens exactly like a deck-level style would.
Outputs go to lab/out/<deck>/ and baselines to lab/baseline/<deck>/ (both git-ignored).
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont
from playwright.sync_api import TimeoutError as PlaywrightTimeout, sync_playwright

ROOT = Path(__file__).resolve().parent.parent
LAB = ROOT / "lab"
# Chrome binary: $NOBEAMER_CHROME, else the first existing candidate (local install, cloud sandbox)
CHROME = os.environ.get("NOBEAMER_CHROME") or next(
    (c for c in ("/usr/bin/google-chrome", "/opt/pw-browsers/chromium") if Path(c).exists()), "/usr/bin/google-chrome"
)
W, H = 1280, 720

LINT_JS = """
(minFont) => {
  const TOL = 2;
  const label = el => {
    const cls = typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\\s+/).slice(0, 2).join('.') : '';
    const href = el.querySelector?.(':scope > a[href^="#"], :scope > p > a[href^="#"]')?.getAttribute('href') || '';
    const text = (el.innerText || '').trim().replace(/\\s+/g, ' ').slice(0, 36);
    return `${el.tagName.toLowerCase()}${cls}${href ? `[${href}]` : ''}${text ? ` "${text}"` : ''}`;
  };
  return [...document.querySelectorAll('svg[data-marpit-svg]')].map((svg, i) => {
    const sec = svg.querySelector('foreignObject:not([data-marpit-advanced-background]) > section, foreignObject[data-marpit-advanced-background="content"] > section');
    // Bounds come from the slide frame (svg), not the section box, which may grow past the frame
    const sr = svg.getBoundingClientRect();
    const cs = getComputedStyle(sec);
    const box = {
      l: sr.left + parseFloat(cs.paddingLeft), r: sr.right - parseFloat(cs.paddingRight),
      t: sr.top + parseFloat(cs.paddingTop), b: sr.bottom - parseFloat(cs.paddingBottom),
    };
    const issues = [];
    const flagged = [];
    const add = (el, kind, px) => {
      if (flagged.some(f => f.kind === kind && f.el.contains(el))) return;
      flagged.push({ el, kind });
      issues.push({ kind, px: Math.round(px), el: label(el) });
    };
    let maxBottom = box.t;
    for (const el of sec.querySelectorAll('*')) {
      if (el.closest('mjx-container svg, .katex-html svg')) continue;
      const s = getComputedStyle(el);
      if (s.display === 'none' || s.visibility === 'hidden') continue;
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      if (s.position !== 'absolute' && s.position !== 'fixed') {
        maxBottom = Math.max(maxBottom, r.bottom);
        if (r.bottom > box.b + TOL) add(el, 'overflow-bottom', r.bottom - box.b);
        if (r.right > box.r + TOL) add(el, 'overflow-right', r.right - box.r);
        if (r.left < box.l - TOL) add(el, 'overflow-left', box.l - r.left);
        // Block escaping a non-clipping parent (typically an uncleared float collapsing its container)
        const par = el.parentElement;
        if (par && par !== sec && s.display !== 'inline' && !el.closest('.katex, mjx-container') && getComputedStyle(par).overflowY === 'visible') {
          const pr = par.getBoundingClientRect();
          if (r.bottom > pr.bottom + TOL) add(el, 'escapes-parent', r.bottom - pr.bottom);
        }
      }
      if (s.overflowX !== 'visible' && el.scrollWidth > el.clientWidth + 1) add(el, 'clipped-x', el.scrollWidth - el.clientWidth);
      if (s.overflowY !== 'visible' && el.scrollHeight > el.clientHeight + 1) add(el, 'clipped-y', el.scrollHeight - el.clientHeight);
      const fs = parseFloat(s.fontSize);
      if (fs < minFont && [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) add(el, 'small-font', fs);
    }
    // Sibling blocks whose boxes intersect: floats wrapping text, negative margins, collisions
    const flow = el => { const s = getComputedStyle(el); return s.position !== 'absolute' && s.position !== 'fixed' && s.display !== 'none' && s.display !== 'inline'; };
    for (const parent of [sec, ...sec.querySelectorAll('div, blockquote, figure')]) {
      const kids = [...parent.children].filter(flow).map(el => ({ el, r: el.getBoundingClientRect() })).filter(k => k.r.width && k.r.height);
      for (let a = 0; a < kids.length; a++) for (let b = a + 1; b < kids.length; b++) {
        const A = kids[a].r, B = kids[b].r;
        const w = Math.min(A.right, B.right) - Math.max(A.left, B.left), h = Math.min(A.bottom, B.bottom) - Math.max(A.top, B.top);
        if (w > TOL && h > TOL) add(kids[b].el, 'overlap', Math.min(w, h));
      }
    }
    return {
      slide: i + 1,
      classes: sec.className,
      fill: Math.round(100 * (maxBottom - box.t) / (box.b - box.t)),
      issues,
    };
  });
}
"""


def parse_slides(spec: str | None) -> set[int] | None:
    if not spec:
        return None
    out = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out.update(range(int(a), int(b or a) + 1))
    return out


def parse_variant(spec: str) -> tuple[str, str]:
    name, _, value = spec.partition("=")
    path = ROOT / value
    css = path.read_text() if value.endswith(".css") and path.is_file() else value
    return name, css


def inject_style(md: str, css: str) -> str:
    """Insert a global <style> right after the front matter."""
    m = re.match(r"---\n.*?\n---\n", md, re.S)
    at = m.end() if m else 0
    return f"{md[:at]}\n<style>\n{css}\n</style>\n{md[at:]}"


def build_html(deck: Path, theme: Path, out_dir: Path, css: str | None) -> Path:
    """Compile the deck with every slide stacked (bare template), resolving relative URLs against the deck dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    md = deck.read_text()
    if css:
        md = inject_style(md, css)
    src = out_dir / "deck.md"
    src.write_text(md)
    html = out_dir / "deck.html"
    subprocess.run(
        ["marp", str(src), "--html", "--template", "bare", "--theme-set", str(theme), "-o", str(html)],
        check=True, capture_output=True, cwd=ROOT, stdin=subprocess.DEVNULL, timeout=60,
    )
    text = html.read_text().replace("<head>", f'<head><base href="{deck.parent.as_uri()}/">', 1)
    html.write_text(text)
    return html


class Lab:
    def __init__(self, args):
        self.deck = (ROOT / args.deck).resolve()
        self.theme = (ROOT / args.theme).resolve()
        self.slides = parse_slides(args.slides)
        self.min_font = args.min_font
        self.offline = args.offline
        self.out = LAB / "out" / self.deck.name.split(".")[0]
        self._pw = sync_playwright().start()
        self.browser = self._pw.chromium.launch(executable_path=CHROME, headless=True, args=["--no-sandbox"])

    def close(self):
        self.browser.close()
        self._pw.stop()

    def render(self, variant: str = "current", css: str | None = None, shots: bool = True) -> tuple[list[dict], dict[int, Path]]:
        vdir = self.out / variant
        html = build_html(self.deck, self.theme, vdir, css)
        page = self.browser.new_page(viewport={"width": W, "height": H})
        if self.offline:
            # Simulate previews that block remote resources (e.g. VS Code): web fonts fall back to local fonts
            page.route(re.compile(r"^https?://"), lambda route: route.abort())
        page.set_default_timeout(30_000)
        page.goto(html.as_uri())
        try:
            page.wait_for_load_state("networkidle", timeout=15_000)
        except PlaywrightTimeout:
            print(f"warning: network not idle after 15s ({variant}), rendering anyway", file=sys.stderr)
        page.evaluate("document.fonts.ready")
        report = page.evaluate(LINT_JS, self.min_font)
        pngs = {}
        if shots:
            for old in vdir.glob("*.png"):
                old.unlink()
            for i, svg in enumerate(page.query_selector_all("svg[data-marpit-svg]"), 1):
                if self.slides and i not in self.slides:
                    continue
                pngs[i] = vdir / f"{i:02d}.png"
                svg.screenshot(path=pngs[i])
        page.close()
        if self.slides:
            report = [r for r in report if r["slide"] in self.slides]
        return report, pngs


# ---------- image helpers ----------

def font(size: int):
    for name in ("DejaVuSansMono-Bold.ttf", "/usr/share/fonts/dejavu-sans-mono-fonts/DejaVuSansMono-Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def tag(img: Image.Image, text: str, bad: bool = False) -> Image.Image:
    img = img.convert("RGB")
    d = ImageDraw.Draw(img)
    f = font(max(14, img.width // 28))
    x0, y0, x1, y1 = d.textbbox((0, 0), text, font=f)
    d.rectangle((0, 0, x1 - x0 + 12, y1 - y0 + 10), fill=(200, 0, 0) if bad else (20, 20, 20))
    d.text((6 - x0, 5 - y0), text, font=f, fill="white")
    if bad:
        d.rectangle((0, 0, img.width - 1, img.height - 1), outline=(200, 0, 0), width=4)
    return img


def grid(tiles: list[Image.Image], cols: int, gap: int = 8) -> Image.Image:
    tw, th = tiles[0].size
    rows = -(-len(tiles) // cols)
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * gap, rows * th + (rows + 1) * gap), (128, 128, 128))
    for k, t in enumerate(tiles):
        r, c = divmod(k, cols)
        sheet.paste(t, (gap + c * (tw + gap), gap + r * (th + gap)))
    return sheet


def thumb(path: Path, width: int) -> Image.Image:
    img = Image.open(path).convert("RGB")
    return img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)


def diff_image(a: Path, b: Path, threshold: int = 24) -> tuple[float, Image.Image]:
    ia, ib = Image.open(a).convert("RGB"), Image.open(b).convert("RGB")
    if ia.size != ib.size:
        return 100.0, ib
    mask = ImageChops.difference(ia, ib).convert("L").point(lambda v: 255 if v > threshold else 0)
    pct = 100 * sum(mask.histogram()[255:]) / (ia.width * ia.height)
    ghost = Image.blend(ib, Image.new("RGB", ib.size, "white"), 0.7)
    ghost.paste(Image.new("RGB", ib.size, (230, 0, 20)), mask=mask)
    return pct, ghost


# ---------- reporting ----------

def is_bad(r: dict) -> bool:
    """Slide has layout errors, unless the deck marks them as intentional with the `lab-expect` class."""
    return "lab-expect" not in r["classes"].split() and any(i["kind"] != "small-font" for i in r["issues"])


def print_lint(report: list[dict]) -> int:
    errors = 0
    for r in report:
        cls = r["classes"] or "-"
        state = "ok" if not r["issues"] else f"{len(r['issues'])} issue(s)" + ("" if is_bad(r) else " (expected)")
        print(f"#{r['slide']:02d} {cls:<16} fill {r['fill']:>3}%  {state}")
        for it in r["issues"]:
            print(f"      {it['kind']:<16} {it['px']:>4}px  {it['el']}")
        errors += is_bad(r)
    return errors


def cmd_lint(lab: Lab, args) -> int:
    report, _ = lab.render(shots=False)
    if args.json:
        print(json.dumps(report, indent=1))
        return 0
    return 1 if print_lint(report) else 0


def cmd_sheet(lab: Lab, args) -> int:
    report, pngs = lab.render()
    bad = {r["slide"] for r in report if is_bad(r)}
    tiles = [tag(thumb(p, args.width), f"#{i:02d}", i in bad) for i, p in pngs.items()]
    path = lab.out / "sheet.png"
    grid(tiles, args.cols).save(path)
    print_lint(report)
    print(f"\nsheet: {path.relative_to(ROOT)}  ({len(tiles)} slides, {len(bad)} with layout issues)")
    return 0


def cmd_baseline(lab: Lab, args) -> int:
    _, pngs = lab.render()
    dest = LAB / "baseline" / lab.out.name
    dest.mkdir(parents=True, exist_ok=True)
    for i, p in pngs.items():
        shutil.copy(p, dest / p.name)
    print(f"baseline: {len(pngs)} slides -> {dest.relative_to(ROOT)}")
    return 0


def cmd_diff(lab: Lab, args) -> int:
    base = LAB / "baseline" / lab.out.name
    if not base.is_dir():
        sys.exit("no baseline yet: run `uv run lab/swiss_lab.py baseline` first")
    report, pngs = lab.render()
    lint = {r["slide"]: r for r in report}
    rows = []
    for i, p in pngs.items():
        ref = base / p.name
        if not ref.exists():
            print(f"#{i:02d}  new slide (no baseline)")
            continue
        pct, ghost = diff_image(ref, p, args.threshold)
        if pct < args.min_change:
            continue
        print(f"#{i:02d}  {pct:6.2f}% changed   fill {lint[i]['fill']}%")
        tw = args.width
        rows.append([tag(thumb(ref, tw), f"#{i:02d} before"), tag(thumb(p, tw), f"#{i:02d} after"), tag(ghost.resize(thumb(p, tw).size), "diff")])
    if not rows:
        print("no visual changes")
        return 0
    path = lab.out / "diff.png"
    grid([t for row in rows for t in row], 3).save(path)
    print(f"\ndiff sheet: {path.relative_to(ROOT)}  ({len(rows)} changed slides)")
    return 0


def cmd_ab(lab: Lab, args) -> int:
    variants = [("base", None)] + [parse_variant(v) for v in args.variant]
    columns = []
    for name, css in variants:
        report, pngs = lab.render(variant=f"ab-{name}", css=css)
        bad = {r["slide"] for r in report if is_bad(r)}
        columns.append([tag(thumb(p, args.width), f"#{i:02d} {name}", i in bad) for i, p in pngs.items()])
        print(f"== {name}")
        print_lint(report)
    tiles = [col[k] for k in range(len(columns[0])) for col in columns]
    path = lab.out / "ab.png"
    grid(tiles, len(columns)).save(path)
    print(f"\nA/B sheet: {path.relative_to(ROOT)}  (rows = slides, columns = {', '.join(n for n, _ in variants)})")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["sheet", "lint", "baseline", "diff", "ab"])
    p.add_argument("--deck", default="demo-swiss.marp.md")
    p.add_argument("--theme", default="nobeamer-swiss.css")
    p.add_argument("-s", "--slides", help='subset, e.g. "1,3-5"')
    p.add_argument("-v", "--variant", action="append", default=[], help="ab: NAME=CSS or NAME=path.css (repeatable)")
    p.add_argument("--cols", type=int, default=4, help="sheet: thumbnails per row")
    p.add_argument("--width", type=int, default=480, help="thumbnail width in px")
    p.add_argument("--min-font", type=float, default=12, help="lint: flag text below this size (px)")
    p.add_argument("--threshold", type=int, default=24, help="diff: per-pixel luminance tolerance (0-255)")
    p.add_argument("--min-change", type=float, default=0.05, help="diff: ignore slides with less %% changed")
    p.add_argument("--json", action="store_true", help="lint: machine-readable output")
    p.add_argument("--offline", action="store_true", help="block remote requests (web fonts), like the VS Code preview")
    args = p.parse_args()

    lab = Lab(args)
    try:
        return {"sheet": cmd_sheet, "lint": cmd_lint, "baseline": cmd_baseline, "diff": cmd_diff, "ab": cmd_ab}[args.command](lab, args)
    finally:
        lab.close()


if __name__ == "__main__":
    sys.exit(main())
