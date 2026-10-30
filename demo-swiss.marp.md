---
marp: true
theme: nobeamer-swiss
paginate: true
size: 16:9
math: mathjax
title: "nobeamer-swiss: Feature Guide & Test Deck"
transition: swiss
---

<!-- Single source for the theme: every feature rendered live next to its syntax, plus stress cases at the end.
     Doubles as the lab/swiss_lab.py test deck. Append new slides at the end to keep diff baselines aligned. -->

<!-- _class: lead -->

![bg right:46% saturate:0](images/scholar_portrait.jpg)

# <!--fit--> NoBeamer <br> **SWISS**

### *Feature Guide &* TEST DECK

- **Theme**: NOBEAMER-SWISS
- **Style**: International Typographic
- **Version**: 2.0

---

<!-- _class: cols-2 -->

## Contents

> [01](#card-r)
> ### <!--fit--> Typography
> Headings, body text, lists, and the paper-ink surface.

> [02](#card-r)
> ### <!--fit--> Grids
> Symmetric and asymmetric columns with `![split]()`.

![split]()

> [03](#card)
> ### <!--fit--> Cards
> `#card`, status cards (`#i`, `#a`, `#s`, `#d`), and alignment.

> [04](#card)
> ### <!--fit--> Data & Variants
> Tables, code, math, figures, accent, and invert.

---

## Heading Hierarchy

# Title H1 **strong**

## Section H2 **strong**

### Subsection H3

#### Micro-Label H4

Body text follows the heading stack with flush-left, ragged-right rhythm. Markdown: `#` to `####`; `**strong**` inside a heading takes the accent.

---

<!-- _class: cols-2 -->

## Body Text & Lists

Running text with **bold**, *italic*, `inline code`, and a [link](https://example.com). Long sentences wrap to expose the leading and measure.

- Unordered item with accent bullet
- Item that wraps onto a second line to check the hanging indent
  - Nested sub-item

1. Ordered step one
2. Ordered step two

> A plain quote: just `>`, with the red margin line.

![split]()

### Syntax

```markdown
Text with **bold**, *italic*, `code`, [link](url).

- Item
  - Nested item

1. Ordered step

> Plain quote
```

---

<!-- _class: lead -->

# <!--fit--> **GRIDS**

### *SECTION DIVIDER:* LEAD WITHOUT IMAGE

![bg right:46% saturate:0](images/blue_carnival.jpg)

---

<!-- _class: cols-2 -->

## Two Columns (`cols-2`)

Equal columns of **572px** with a **24px** gutter. Headings `h1` and `h2` span all columns.

Each `![split]()` starts the next column. Content that is too tall spills **downward**, never into a hidden column.

![split]()

### Syntax

```markdown
<!-- _class: cols-2 -->

## Title (spans all columns)

Left column...

![split]()

Right column...
```

---

<!-- _class: cols-3 -->

## Three Columns (`cols-3`)

> [01](#card)
> ### Column One
> Equal columns of 377.33px with an 18px gutter.

![split]()

> [02](#card)
> ### Column Two
> Two `![split]()` markers define three columns.

![split]()

> [03](#card)
> ### Column Three
> Use `<!-- _class: cols-3 -->` on the slide.

---

<!-- _class: cols-2-a -->

## Asymmetric Two Columns (`cols-2-a`)

> [2 PARTS](#card)
> ### Narrow Lead
> Short framing text or a key definition.

`<!-- _class: cols-2-a -->`

![split]()

### Wide Column: 3 Parts

Room for tables, code, and denser running text.

| Column | Ratio | Width |
| :--- | ---: | ---: |
| **1** | 2 | 457.6px |
| **2** | 3 | 686.4px |

---

<!-- _class: cols-3-a -->

## Asymmetric Three Columns (`cols-3-a`)

> [3 PARTS](#card)
> ### Narrow
> 283px.

![split]()

> [4 PARTS](#card)
> ### Medium
> 377.33px.

![split]()

> [5 PARTS](#card)
> ### Wide
> 471.67px: the widest module, for the main content.

`<!-- _class: cols-3-a -->`

---

<!-- _class: lead -->

# <!--fit--> **CARDS**

### *SECTION DIVIDER:* LEAD WITHOUT IMAGE


![bg right:46% saturate:0](images/pexels-hikaique-775201.jpg)

---

<!-- _class: cols-2 -->

## The Swiss Card (`#card`)

> [DEF 01](#card)
> ### <!-- fit --> Grid Topology
> Let $G = (V, E)$ denote an orthogonal modular grid where interval $\delta$ is invariant across subdivisions:
> $$\delta(x, y) = \kappa \cdot \sqrt{\Delta x^2 + \Delta y^2}$$

![split]()

### Syntax

```markdown
> [DEF 01](#card)
> ### <!-- fit --> Grid Topology
> Body in justified serif.
> $$ ...centered math... $$
```

- **Tag first**: `[TAG](#card)` must open the card.
- **Fit title**: `### <!-- fit -->` fills the width up to the tag.
- **No tag**: `[](#card)` renders without the badge.

---

<!-- _class: cols-2 -->

## Card Headers

> [THM 02](#card)
> ### <!-- fit --> Auto-Scaling Header
> `### <!-- fit -->` title with a hairline underneath.

> [DEF 03](#card)
> **Static Bold Header**
> `**Title**` fallback: tag, title, and body in one paragraph.

![split]()

### Syntax

```markdown
> [THM 02](#card)
> ### <!-- fit --> Auto-Scaling Header
> Body text.

> [DEF 03](#card)
> **Static Bold Header**
> Body text.
```

---

<!-- _class: cols-2 -->

## Content Alignment (`-l`, `-c`, `-r`)

> [LEFT](#card-l)
> ### Left (default)
> Flush-left header, tag on the right.

> [CENTER](#card-c)
> ### Centered
> Centered header and last line.

> [RIGHT](#card-r)
> **Right, Mirrored**
> Right-aligned header, tag on the left.

![split]()

### Syntax

Cards always fill the column; the suffix only aligns the content.

```markdown
> [TAG](#card-l)    > [TAG](#card-c)
> [TAG](#card-r)
> [](#i-r)  > [](#a-c)  > [](#s-l)
```

> [](#i-r) **Status Right (`#i-r`)**
> The suffix works on status cards too.

---

<!-- _class: cols-2 -->

## Status Cards (`#i`, `#a`, `#s`, `#d`)

> [](#i) **Information (`#i`)**
> Neutral notice on orange card stock.

> [](#a) **Alert (`#a`)**
> Warning on accent-coloured card stock.

> [](#s) **Success (`#s`)**
> Verified result on forest-green card stock.

> [](#d) **Dark (`#d`)**
> Neutral **emphasis** on charcoal card stock.

![split]()

### Syntax

```markdown
> [](#i) **Title**
> Body text.
```

> [](#a-c) **Alert Centered (`#a-c`)**
> Centered content.

> [](#s-r) **Success Right (`#s-r`)**
> Right-aligned content.

---

<!-- _class: lead -->

# <!--fit--> **DATA &** VARIANTS

### *SECTION DIVIDER:* LEAD WITHOUT IMAGE

![bg right:46% saturate:0](images/pexels-aronvisuals-1743165.jpg)

---

## Tables

| Benchmark | Sample ($N$) | Latency (ms) | Efficiency | Status |
| :--- | ---: | ---: | ---: | :--- |
| **MODULAR-GRID-A** | $12,500$ | $1.42 \pm 0.04$ | $0.984$ | **VERIFIED** |
| **ASYM-HIERARCHY-B** | $28,400$ | $2.15 \pm 0.08$ | $0.961$ | **VERIFIED** |
| **GROTESQUE-TYPE-C** | $45,000$ | $0.88 \pm 0.02$ | $0.997$ | **OPTIMAL** |

Uppercase headers, tabular monospace figures, and row shading. Align numbers right with `---:`:

```markdown
| Parameter | Value |
| :--- | ---: |
| **Sample A** | $1,250$ |
```

---

<!-- _class: cols-2 -->

## Code Blocks

Standard fenced block, auto-shrunk to fit:

```python
def modular_bounds(canvas_w=1280, cols=12):
    usable = canvas_w - 2 * 56
    return (usable - (cols - 1) * 48) / cols
```

Wrap long code in `<div class="code-scroll">` to keep full size; long lines wrap instead of clipping.

![split]()

<div class="code-scroll">

```python
# Long block inside .code-scroll: lines wrap, not clip
def calculate_modular_bounds_with_a_long_name(canvas_width: int = 1280, columns: int = 12, gutter: int = 48) -> dict:
    margin_x = 56
    usable = canvas_width - 2 * margin_x
    col_w = (usable - (columns - 1) * gutter) / columns
    return {"col_width": round(col_w, 2), "gutter": gutter}
```

</div>

---

## Math

Inline math $e^{i\pi} + 1 = 0$ in running text. Wrap key equations in `<div class="math-resolution">`:

<div class="math-resolution">

$$
\mathcal{L}(\theta) = \sum_{k=1}^K \left[ \alpha \log \left( 1 + \frac{C(k)}{N(k)} \right) - \beta \|\nabla \Phi(k)\|_2^2 \right]
$$

</div>

Plain display math stays unframed:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

---

<!-- _class: cols-2 -->

## Figures

![w:560 h:220](images/helvetica_poster.jpg)
*FIG. 01 / HELVETICA SPECIMEN*

![split]()

### Syntax

```markdown
![w:560 h:220](image.jpg)
*FIG. 01 / CAPTION*
```

Size with Marp's `w:` / `h:`; the italic line under the image is the caption.

---

<!-- _class: cols-2 -->
<!-- _style: "--accent: #0066CC;" -->

## Accent Override (`--accent`)

- Bullets, **bold**, and borders inherit `--accent`.
- This slide sets `--accent: #0066CC`.

> [TAG](#card)
> ### Accent Card
> Tag and rule follow the accent.

![split]()

### Syntax

```markdown
<!-- per slide -->
<!-- _style: "--accent: #0066CC;" -->

# front matter, whole deck
style: ":root { --accent: #0066CC; }"
```

> [](#a) **Accent Alert**
> Alert tint follows the accent.

---

<!-- _class: invert cols-2 -->

## Inverted Mode (`invert`)

### Subsection on Dark

- White type with accent highlights.
- `inline code` and **bold** on dark ground.

> [TAG](#card)
> ### Card on Dark
> Hairlines adapt to the inverted ground.

![split]()

> [](#d) **Dark Card on Dark**
> Must stay distinguishable from the ground.

| Key | Value |
| :--- | ---: |
| **class** | `invert cols-2` |

---

<!-- _class: accent cols-2 -->

## Accent Field (`accent`)

### Subsection on Accent

- White type on the accent colour, with fibre noise.
- `inline code`, **bold** and [links](https://example.com) stay readable.

> A plain quote keeps its mark, now white.

![split]()

> [TAG](#card)
> ### Card on Accent
> Rules and cards adapt to the field.

> [](#d) **Dark Card on Accent**
> Charcoal stock stays distinguishable.

| Key | Value |
| :--- | ---: |
| **class** | `accent cols-2` |

---

<!-- _class: cols-2 -->

## Quick Reference

| Feature | Syntax |
| :--- | :--- |
| **Title / Divider** | `_class: lead` (+ `![bg right:46%]`) |
| **Columns** | `cols-2`, `cols-3` + `![split]()` |
| **Asymmetric** | `cols-2-a`, `cols-3-a` |
| **Card** | `> [TAG](#card)` + `### <!-- fit -->` |
| **Alignment** | `#card-c`, `#card-r`, `#i-r` |
| **Status** | `> [](#i)`, `[](#a)`, `[](#s)`, `[](#d)` |
| **Variants** | `invert`, `accent`, `--accent` |

![split]()

### Design Rules

- **No icons or emojis**: Typography and numeric identifiers only.
- **Flat geometry**: Square corners, no shadows. Status cards and code blocks are the exception: paper card stock.
- **No centered body text**: Flush-left, ragged-right.
- **Controlled bold**: Contrast comes from scale.

---

<!-- _class: lead -->

# <!--fit--> **STRESS** TESTS

### *EDGE CASES FOR* LAB/SWISS_LAB.PY

![bg right:60% saturate:0](images/light_desk.jpg)

---

## Stress: A Deliberately Long Section Title That Must Wrap Gracefully Across Two Lines

The heading underline and the spacing to the body must stay consistent when the title wraps.

- First point with moderately long text to fill the measure of the line.
- Second point with moderately long text to fill the measure of the line.
- Third point with moderately long text to fill the measure of the line.

---

<!-- _class: cols-3 -->

## Stress: Dense Three Columns

> [A](#card)
> ### Alpha
> Short body text for the first card in column one.

> [](#i) **Note**
> Information card stacked under a card.

![split]()

| K | V |
| :--- | ---: |
| **a** | 1.00 |
| **b** | 2.50 |
| **c** | 3.75 |

```python
x = [i * 2 for i in range(9)]
```

![split]()

- Item one in a narrow column
- Item two wraps across lines in a narrow column

> [](#a) **Limit**
> Last block near the bottom edge.

---

<!-- _class: cols-2 lab-expect -->

## Stress: Column Overflow (expected)

> [](#i) **Overfull Column**
> This column is deliberately taller than the slide.

> [](#a) **Second Card**
> Excess must spill downward and stay visible.

> [](#s) **Third Card**
> Keeps pushing past the bottom edge.

> [](#i) **Fourth Card**
> Still in the first column.

> [](#a) **Fifth Card**
> Past the bottom edge.

![split]()

### Second Column

Must stay in place next to the first one. `lab-expect` tells the lab that the overflow on this slide is intentional.

---

<!-- _class: accent grid -->

## Overlay: Grid (`grid` on `accent`)

An irregular skyline of square dots bleeding off the bottom and right edges, under the content. It also works with `invert` and on plain paper.

| Module | Width |
| :--- | ---: |
| **A** | 1 |
