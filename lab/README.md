# Theme Design Lab

Fast feedback loop for refining `nobeamer-swiss.css` without manual screenshot hunting.

```bash
uv run lab/swiss_lab.py sheet       # render deck + lint + contact sheet -> lab/out/<deck>/sheet.png
uv run lab/swiss_lab.py lint        # numeric layout checks only (exit 1 on layout errors)
uv run lab/swiss_lab.py baseline    # freeze current renders as reference
uv run lab/swiss_lab.py diff        # changed slides only: before | after | diff -> diff.png
uv run lab/swiss_lab.py ab -s 4,18 -v tight=":root{--gutter:24px}" -v wide=lab/wide.css   # -> ab.png
```

Options: `--deck` (default `demo-swiss.marp.md`), `--offline` (block web fonts like the VS Code preview), `-s "1,3-5"` slide subset, `--cols`, `--width`.

## Test deck

[`demo-swiss.marp.md`](../demo-swiss.marp.md) is both the feature guide and the test deck: every feature rendered live,
plus stress cases at the end. Baselines are keyed by slide number: append new slides at the end, then re-run `baseline`.

Add the class `lab-expect` to a slide whose issues are intentional (e.g. the overflow stress test):
they are still listed but do not fail `lint` or mark the slide red.

## Lint checks

| Kind | Meaning |
| :--- | :--- |
| `overflow-bottom/right/left` | Block crosses the slide padding box (in `cols-*`, `overflow-right` means content spilled into an off-screen column) |
| `escapes-parent` | Block extends below its container, usually an uncleared float collapsing a card |
| `overlap` | Sibling blocks intersect |
| `clipped-x/y` | Content hidden by `overflow` (expected for `.code-scroll`, but invisible in PDF) |
| `small-font` | Text below `--min-font` px (warning only) |

`fill` is the share of the content box height used by the slide, for density balancing.

Live preview for visual judgment: `marp -s . --theme-set nobeamer-swiss.css --html`.
