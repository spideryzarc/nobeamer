# nobeamer — working notes for Claude

nobeamer is a family of two Marp themes that share one Markdown grammar: `nobeamer.css` (original:
skeuomorphic, for live teaching) and `nobeamer-swiss.css` (Swiss design, for study material read as PDF).
Development happens on branch `feat-swiss`.

**Read [docs/DECISIONS.md](docs/DECISIONS.md) before changing a theme.** It holds the shared grammar both themes
must implement: a new element goes into both themes (each in its own style) or into none, and neither theme keeps
legacy compatibility code.

## Documentation map

| File | Content |
| :--- | :--- |
| `README.md` | Family overview: which theme for what, demos, links |
| `docs/INSTALL.md` | Technical setup for both themes (files, VS Code, CLI, transitions, PDF) |
| `docs/<theme>/MANIFESTO.md` | Concept, use case, is / is not, usage guidelines (`nobeamer`, `swiss`) |
| `docs/<theme>/REFERENCE.md` | Full syntax as that theme draws it |
| `MARP_INIT.md` | AI scaffolding prompt; asks which theme to install |

When the grammar or a theme's look changes, update both references and the demos.

## Review loop

After every change to a theme or a demo:

1. Check with the lab (see `lab/README.md`): `uv run lab/swiss_lab.py lint` and `diff` (take a `baseline` before
   editing). Use `ab` to compare variants before touching the theme.
   - Swiss (default deck/theme): lint must be clean.
   - Original: `--deck demo.marp.md --theme nobeamer.css` (and `bhaskara.marp.md`). Its bleeding blocks report
     `overflow-left/right` of 32-40px and code reports `clipped`: those are by design; look for anything else.
   - Cross-render (the shared-grammar promise: switching `theme:` loses nothing): copy each demo with its
     `theme:`/`transition:` swapped (e.g. `sed 's/^theme: nobeamer-swiss$/theme: nobeamer/'`) and lint it with
     the other theme. Passing only `--theme` is not enough: Marp falls back to the default theme when the deck
     asks for a theme that is not loaded.
2. Rebuild the compiled demos (stdin must be closed, or marp-cli waits on it forever):
   `marp demo-swiss.marp.md --html --theme-set nobeamer-swiss.css -o demo-swiss.marp.html < /dev/null`
   `marp demo.marp.md --html --theme-set nobeamer.css -o demo.marp.html < /dev/null` (same for `bhaskara`)
3. Republish the Swiss demo as the review page, keeping the same URL:
   https://claude.ai/artifact/P5YoKg9BxNzW25j6sPJqnx
   Publish `demo-swiss.marp.html` with `url` set to that link and the deck's images (`images/*.jpg` referenced in
   the HTML) passed as `files`. This live HTML deck is the user's primary way to review; PNG contact sheets are
   secondary.

## Environment

- marp-cli is not preinstalled in cloud sessions: `npm i -g @marp-team/marp-cli`. PDF export needs
  `CHROME_PATH=/opt/pw-browsers/chromium`.
- The lab finds Chrome at `/usr/bin/google-chrome` or `/opt/pw-browsers/chromium`; override with `NOBEAMER_CHROME`.
- The lab's `baseline` does not delete images of slides that no longer exist: after removing slides, clear
  `lab/baseline/<deck>/` before taking a new baseline.
- Comparison pages (variant CSS injected into the compiled HTML, toggled by buttons) bypass Marp's CSS processing:
  code blocks are `<marp-pre>` at runtime there, so write `:is(pre, marp-pre)`, never bare `pre`; and theme rules
  win on specificity, so variant rules need `!important`.
- An SVG background cannot read CSS custom properties: anything that must follow `--accent` (e.g. the `tiles`
  circles) is a separate gradient layer.
- Demo images stay under 1600px on the long side. In PDF, Chrome rasterizes areas with blend modes, which is what
  makes the Swiss PDF heavy.
