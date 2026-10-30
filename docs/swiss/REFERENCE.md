# `nobeamer-swiss` — syntax reference

The full syntax of the nobeamer family, as `nobeamer-swiss` draws it. The same Markdown works in
[`nobeamer`](../nobeamer/REFERENCE.md); what changes is the look. For when to use each element, see the
[manifesto](MANIFESTO.md); for setup, the [installation guide](../INSTALL.md). Every element is rendered live in
the [demo deck](../../demo-swiss.marp.md).

## Front matter

```yaml
---
marp: true
theme: nobeamer-swiss
paginate: true
transition: swiss
math: mathjax
style: ":root { --accent: #0066CC; }"   # optional: recolour the whole deck
---
```

## Slide classes

Set per slide with `<!-- _class: name -->`; combine with spaces (`<!-- _class: accent cols-2 -->`).

| Class | Look in `nobeamer-swiss` |
| :--- | :--- |
| `lead` | Title or section divider: monumental title, accent field across the lower half, optional photo (`![bg right:46%](…)`) turned duotone. A Markdown list becomes the metadata bar at the bottom. |
| `invert` | Charcoal ground, white type; status cards and code lift a step. |
| `accent` | The slide printed in the accent colour (stepped toward black for contrast), with paper grain and white type. The `#card` tag turns white with accent text. |
| `cols-2`, `cols-3` | Equal columns (24px / 18px gutter); `![split]()` starts the next column. |
| `cols-2-a`, `cols-3-a` | Asymmetric columns, 2:3 and 3:4:5. |
| `grid` | A skyline of white square dots bleeding off the bottom-right corner. |
| `tiles` | A full-slide watermark of modular rounded tiles with three accent circles. |

`grid` and `tiles` work on paper and combined with `invert` or `accent`.

### Lead metadata

```markdown
<!-- _class: lead -->

# Course **Title**
### *Lecture 3:* Subtitle

- **Course**: Algorithms
- **Date**: 2026-10-30

![bg right:46% saturate:0](images/photo.jpg)
```

## Text

| Syntax | Look |
| :--- | :--- |
| `#` … `####` | Neo-grotesque (Geist) hierarchy; `##` carries a hairline. `**bold**` inside a heading takes the accent. |
| Body, lists | Flush-left, ragged-right; accent bullets. |
| `> quote` | Editorial pull quote: Literata italic, large, with an accent opening mark hanging in the gutter. No frame. |

## Cards

### Status cards

Card stock with a cast shadow, monospaced text.

| Syntax | Card |
| :--- | :--- |
| `> [](#i) **Title**` | Information — orange stock, charcoal text |
| `> [](#a) **Title**` | Alert — accent stock |
| `> [](#s) **Title**` | Success — forest green stock |
| `> [](#d) **Title**` | Dark — charcoal stock |

The first line after the marker is the title; the next lines are the body.

### Structural card (`#card`)

```markdown
> [DEF 01](#card)
> ### <!-- fit --> Grid Topology
> Body in justified serif.
> $$ \delta(x,y) = \kappa \cdot \sqrt{\Delta x^2 + \Delta y^2} $$
```

No sheet: the card sits on the paper, with a red tag (`[TAG](#card)`, or `[](#card)` for none), a title with a
hairline and a justified Literata body; display math is centred. `### <!-- fit -->` makes the title fill the width up to the tag; a
`**Title**` on the first line is the static fallback.

### Alignment

Add `-c` (centre) or `-r` (right) to any marker: `#i-c`, `#a-r`, `#d-c`, `#card-r`. Cards always fill their
column; the suffix aligns the content (a right card mirrors: tag on the left). `-l` is the default.

## Columns

```markdown
<!-- _class: cols-2 -->

## Title (spans all columns)

Left column…

![split]()

Right column…
```

Content that is too tall spills downward (visible), never into a hidden column. `cols-2-a` gives the first column 2/5
of the width and the second 3/5; `cols-3-a` splits 3:4:5.

## Images and figures

| Syntax | Result |
| :--- | :--- |
| `![w:560 h:220](image.jpg)` + `*FIG. 01 / CAPTION*` on the next line | Figure cropped to the box; the italic line becomes a mono caption with an accent rule. |
| `![w:240 rounded](…)`, `rounded-sm`, `rounded-lg`, `circle` | Rounded corners (16 / 8 / 28px) or a circular crop. Square corners are the default. |
| `![w:300 drop-shadow](…)`, `saturate:0`, `sepia`, … | Marp's native image filters. |
| `![bg right:40%](…)`, `![bg left:56%](…)` | Side backgrounds (Marp). |
| `![bg right:45% 80% framed](…)` | Framed background: any word in the alt text rounds it; with a size the clip follows the image. |

## Tables

Compact and centred in their space (slide or column). Accent rules top and bottom, an ink rule under the header,
a soft accent zebra, no row fill; `**bold**` in a cell takes the accent. Align numbers right with `---:`.

## Code

Fenced blocks print on charcoal card stock with a language label (`PYTHON`, `HTML`, …) and a syntax palette drawn
from the theme. Inline `` `code` `` is a light chip.

Long code that must keep its full size:

````html
<div class="code-scroll">

```python
# long code
```

</div>
````

It scrolls on screen; in a PDF only the visible part is printed.

## Math

Inline `$…$` and display `$$…$$` (MathJax). To frame a derivation:

```html
<div class="math-resolution">

$$ … $$

</div>
```

## Colour

`--accent` recolours rules, tags, bullets, table rules and zebra, the quote mark, the `accent` slide, the `lead`
field and the `tiles` circles. Per slide: `<!-- _style: "--accent: #0066CC;" -->`.

## Pagination and transitions

`paginate: true` prints `7 / 26` vertically on the right edge in Chakra Petch Light, under an accent tick.
`transition: swiss` is a quiet fade; nothing in the content moves.
