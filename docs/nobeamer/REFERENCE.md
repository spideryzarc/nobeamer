# `nobeamer` — syntax reference

The full syntax of the nobeamer family, as `nobeamer` draws it. The same Markdown works in
[`nobeamer-swiss`](../swiss/REFERENCE.md); what changes is the look. For when to use each element, see the
[manifesto](MANIFESTO.md); for setup, the [installation guide](../INSTALL.md). See it live in the
[demo deck](../../demo.marp.md) and the [quadratic formula example](../../bhaskara.marp.md).

## Front matter

```yaml
---
marp: true
theme: nobeamer
paginate: true
transition: nobeamer
math: mathjax
---
```

`lead` is a title slide: set it per slide (`<!-- _class: lead -->`), not for the whole deck.

## Slide classes

Set per slide with `<!-- _class: name -->`; combine with spaces (`<!-- _class: accent grid -->`).

| Class | Look in `nobeamer` |
| :--- | :--- |
| `lead` | Title slide: centred, large title with its gold bar, handwritten subtitle; a Markdown list becomes the metadata line at the bottom. Works with side backgrounds (`![bg left:50%](…)`). |
| `invert` | A chalkboard: dark slate with chalk dust, chalk-white text, yellow chalk for bold in titles. Paper notes and post-its stick to it. |
| `accent` | A sheet of blue construction paper with white text. `nobeamer` keeps its own palette: `--accent` is ignored. |
| `cols-2`, `cols-3` | Columns; `![split]()` starts the next one. Post-its bleed to the slide edges, dark blocks stay misaligned on purpose. |
| `cols-2-a`, `cols-3-a` | Asymmetric columns, 2:3 and 3:4:5. |
| `grid` | Notebook graph paper with a red margin line under the content. |
| `tiles` | A faint watermark of modular rounded tiles with three gold circles. |

`grid` and `tiles` also work with `invert` (chalk lines) and `accent`.

### Lead metadata

```markdown
<!-- _class: lead -->

# The Quadratic Formula
## Making the Boring Beautiful

- **Course**: Algebra I
- **Date**: 2026-10-30

![bg left:50%](images/parabola_arch.png)
```

## Text

| Syntax | Look |
| :--- | :--- |
| `#` … `####` | Josefin Sans; `#` has a gold bar under it. `**bold**` in a heading turns blue. |
| `> quote` | The teacher's voice: a handwritten note (Caveat) on paper, in pen blue; `**bold**` in pen red. It bleeds to the slide edges. |

## Cards

### Post-its and dark block

| Syntax | Card |
| :--- | :--- |
| `> [](#i) **Title**` | Information — yellow post-it |
| `> [](#a) **Title**` | Alert — red post-it |
| `> [](#s) **Title**` | Success — green post-it |
| `> [](#d) **Title**` | Dark block — glossy, rounded, for "proto-bento" grids |

Post-its are attached to the slide edge and slide in when the slide appears. Alignment suffixes position them:

| Suffix | Post-it | Dark block |
| :--- | :--- | :--- |
| none or `-l` (`#i`, `#i-l`) | attached to the left edge | content left |
| `-c` (`#i-c`) | floating in the centre | content centred |
| `-r` (`#i-r`) | attached to the right edge | content right |

```markdown
> [](#i) **Left Post-it**
> Stuck to the left margin.

> [](#a-r) **Right Alert**
> Stuck to the right margin.
```

### Index card (`#card`)

```markdown
> [DEF 01](#card)
> ### Algorithm
> A finite sequence of well-defined instructions…
```

A plain cream index card with softly rounded corners and a red header rule; the tag (`[TAG](#card)`, or `[](#card)` for none) is a slightly crooked
gold sticker. The title is an optional `###` heading (`### <!-- fit -->` fills the width up to the tag); without it the card
has no title and **bold** is just bold (`> [TAG](#card) body text`). `#card-c` centres the content; `#card-r` aligns it right and moves the sticker to the left. Use it for
definitions, theorems, steps and syllabus items.

## Columns

```markdown
<!-- _class: cols-2 -->

## Title (spans all columns)

Left column…

![split]()

Right column…
```

```markdown
<!-- _class: cols-3 -->
Column 1
![split]()
Column 2
![split]()
Column 3
```

`cols-2-a` gives the first column 2/5 of the width and the second 3/5; `cols-3-a` splits 3:4:5. Content that is
too tall spills downward (visible), never into a hidden column; blocks sit closer together inside columns.

## Images and figures

| Syntax | Result |
| :--- | :--- |
| `![w:420 h:200](image.jpg)` + `*Caption*` on the next line | Figure with a handwritten caption under it. |
| `![w:300 rounded](…)`, `rounded-sm`, `rounded-lg`, `circle` | Rounded corners (16 / 8 / 28px) or a circular crop. |
| `![w:300 opacity:80% sepia:50% drop-shadow](…)` | Marp's native filters (`opacity`, `sepia`, `saturate`, `grayscale`, `blur`, `brightness`, `contrast`, `drop-shadow`). |
| `![bg left:56%](…)`, `![bg right:40%](…)` | Side backgrounds (Marp), the "fight the white space" tool. |
| `![bg left:45% 85% rounded](…)` | Framed background: any word in the alt text rounds it; with a size the clip follows the image. |

## Tables

Scientific / APA style: no vertical lines, strong horizontal rules, monospaced data, a subtle zebra and a shadow.
Tables slide up when the slide appears.

## Code

Fenced code blocks are glossy, macOS-like cards that "power on" with a light scan when the slide appears.

For long code that must keep its full size, wrap the block in `<div class="code-scroll">`:

````html
<div class="code-scroll">

```python
# extended code snippet (no '>' prefix)
def process_data(records: list[dict]) -> dict:
    ...
```

</div>
````

- **Uncompressed font**: Marp's auto-scaling is neutralised, so the code stays sharp.
- **Line wrapping**: long lines wrap inside the card, no horizontal scroll.
- **Vertical scrollbar**: scroll with the mouse during the talk without changing slide.
- **Syntax highlighting**: Marp's `highlight.js` colours are kept.

## Math

Inline `$…$` and display `$$…$$`. For long derivations, a paper-styled block:

```html
<div class="math-resolution">

$$
\begin{aligned}
    P(X \le x) &= \sum_{i=0}^x \binom{n}{i} p^i (1-p)^{n-i}
\end{aligned}
$$

</div>
```

## Colour

`nobeamer` is zero-config: its palette is fixed. `--accent` and `_class: accent` are accepted (the grammar is shared
with `nobeamer-swiss`), but the colour is ignored.

## Transitions and PDF

`transition: nobeamer` is a quiet dissolve: the next slide fades in over the current one and settles into place
from slightly larger going forward, slightly smaller going back; cards, tables and code still play their own entrance
animations. It animates the slide as a whole on purpose: per-element morphing froze browsers in fullscreen when a card
overflowed a column. Requirements are in the [installation guide](../INSTALL.md#5-transitions).

When exporting to PDF or printing, every animation, transition, transform and filter is disabled (`@media print`),
so the output is static. In a PDF, `code-scroll` prints only its visible part.
