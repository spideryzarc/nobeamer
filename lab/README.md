# Theme Design Lab

Fast feedback loop for refining `nobeamer-swiss.css` without manual screenshot hunting.

```bash
uv run lab/swiss_lab.py sheet       # render fixtures + lint + contact sheet -> lab/out/<deck>/sheet.png
uv run lab/swiss_lab.py lint        # numeric layout checks only (exit 1 on layout errors)
uv run lab/swiss_lab.py baseline    # freeze current renders as reference
uv run lab/swiss_lab.py diff        # changed slides only: before | after | diff -> diff.png
uv run lab/swiss_lab.py ab -s 4,18 -v tight=":root{--gutter:24px}" -v wide=lab/wide.css   # -> ab.png
```

Options: `--deck` (default `fixtures-swiss.marp.md`), `-s "1,3-5"` slide subset, `--cols`, `--width`.

## Fixture deck

[`fixtures-swiss.marp.md`](../fixtures-swiss.marp.md) holds one slide per component plus stress cases.
Baselines are keyed by slide number: append new fixtures at the end, then re-run `baseline`.

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
