---
marp: true
theme: nobeamer-swiss
paginate: true
size: 16:9
title: "Fixtures: nobeamer-swiss"
---

<!-- Component fixture deck for lab/swiss_lab.py. One component per slide, plus stress cases at the end. Keep slide order stable: baselines are keyed by slide number. -->

<!-- _class: lead -->

![bg right:46% saturate:0](images/scholar_portrait.jpg)

# <!--fit--> FIXTURE <br> **DECK**

### *LEAD &* TITLE SLIDE

- *THEME*: NOBEAMER-SWISS
- *PURPOSE*: VISUAL REGRESSION
- *SLIDES*: 18

---

## Heading Hierarchy

# Title H1 **strong**

## Section H2 **strong**

### Subsection H3

#### Micro-Label H4

Body paragraph right after the heading stack, to check vertical rhythm between headings and running text.

---

## Body Text & Lists

Running paragraph with **bold emphasis**, *italic nuance*, `inline code`, and a [hyperlink](https://example.com). Second sentence to force a line wrap and expose the leading and measure of body text.

- Unordered item with accent bullet
- Second item with a longer sentence that wraps onto a second line to check hanging indentation
  - Nested sub-item
  - Another nested sub-item

1. Ordered step one
2. Ordered step two
3. Ordered step three

---

<!-- _class: cols-2 -->

## Two Columns: Fit Card + Text

> [DEF 01](#card)
> ### <!-- fit --> Grid Topology
> Let $G = (V, E)$ denote an orthogonal modular grid where interval $\delta$ is invariant across subdivisions:
> $$\delta(x, y) = \kappa \cdot \sqrt{\Delta x^2 + \Delta y^2}$$

![split]()

### Right Column

- Paragraph and list content in the second column.
- The H2 must span both columns.
- Column tops must align with the card top.

---

<!-- _class: cols-3 -->

## Three Columns: Workflow Cards

> [01](#card)
> ### Rational Layout
> Establish orthogonal baseline and horizontal margin bounds.

![split]()

> [02](#card)
> ### Typographic Tension
> Set monumental title contrast against high-density data.

![split]()

> [03](#card)
> ### Objective Imagery
> Use photography as documentation, never as ornament.

---

## Card Alignment Variants

> [LEFT](#card-l)
> ### Left Card
> Content flush-left, accent rule on the left.

> [CENTER](#card-c)
> ### Centered Card
> Content centered, accent rule on top.

> [RIGHT](#card-r)
> **Static Bold Header**
> Aligned flush-right, with the bold-header fallback.

---

<!-- _class: cols-2 -->

## Status Cards

> [](#i) **Informational (`#i`)**
> Neutral notice framed with a solid black top border.

> [](#a) **Alert (`#a`)**
> High-priority warning with accent border and tinted ground.

> [](#s) **Success (`#s`)**
> Verified result marked with a forest green border.

![split]()

> [](#i-r) **Info Right (`#i-r`)**
> Right-aligned status card.

> [](#a-c) **Alert Centered (`#a-c`)**
> Centered status card.

> [](#s-l) **Success Left (`#s-l`)**
> Left-aligned status card.

---

<!-- _class: cols-2 -->

## Dark Module

> [](#d) **The Axiom of Form & Content**
> *"Design is the method of putting form and content together."*
> — Paul Rand
>
> Inline `grid_ratio = 1.618` pill and **bold accent** inside the dark module.

![split]()

> [TIP](#card) **Contrast Strategy**
> Use at most one `#d` module per slide.

Plain paragraph below the card to check spacing after blockquotes.

---

## Table

| Benchmark Identifier | Sample Size ($N$) | Latency (ms) | Efficiency | Status |
| :--- | ---: | ---: | ---: | :--- |
| **MODULAR-GRID-A** | $12,500$ | $1.42 \pm 0.04$ | $0.984$ | **VERIFIED** |
| **ASYM-HIERARCHY-B** | $28,400$ | $2.15 \pm 0.08$ | $0.961$ | **VERIFIED** |
| **GROTESQUE-TYPE-C** | $45,000$ | $0.88 \pm 0.02$ | $0.997$ | **OPTIMAL** |
| **NEUE-HAAS-D** | $9,800$ | $3.01 \pm 0.11$ | $0.912$ | **PENDING** |

Caption paragraph after the table.

---

<!-- _class: cols-2 -->

## Code Blocks

```python
def modular_bounds(canvas_w: int = 1920, cols: int = 12) -> dict:
    """Column widths under Swiss grid discipline."""
    usable = canvas_w - 2 * 56
    col_w = (usable - (cols - 1) * 48) / cols
    return {"col_width": round(col_w, 2)}
```

![split]()

<div class="code-scroll">

```python
# Long scrollable block: lines must wrap, not clip
def calculate_modular_bounds_with_a_very_long_function_name(canvas_width: int = 1920, columns: int = 12, gutter: int = 48) -> dict:
    margin_x = 56
    usable = canvas_width - (2 * margin_x)
    col_w = (usable - (columns - 1) * gutter) / columns
    return {"col_width": round(col_w, 2), "gutter": gutter, "margin": margin_x}
```

</div>

---

## Math

Inline math $e^{i\pi} + 1 = 0$ inside running text, followed by a resolution block:

<div class="math-resolution">

$$
\mathcal{L}(\theta) = \sum_{k=1}^K \left[ \alpha \log \left( 1 + \frac{C(k)}{N(k)} \right) - \beta \|\nabla \Phi(k)\|_2^2 \right]
$$

</div>

Plain display math outside the block:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

---

<!-- _class: cols-2 -->

## Inline Metric

<div class="metric">99.4%</div>
<div class="metric-label">READABILITY INDEX</div>

Monumental numbers for quantitative impact inside standard slides.

![split]()

<div class="metric">4.2×</div>
<div class="metric-label">THROUGHPUT RATIO</div>

Second metric for side-by-side comparison.

---

<!-- _class: stat -->

<div class="metric">4.2×</div>
<div class="metric-label">THROUGHPUT RATIO</div>

Quantitative benchmark outcome across full deployment clusters.

---

<!-- _class: cols-2 -->

## Figure & Specs

<figure>
  <img src="images/helvetica_poster.jpg" alt="Helvetica Specimen" style="height: 240px; width: 100%; object-fit: cover;">
  <figcaption>FIG. 01 / HELVETICA SPECIMEN</figcaption>
</figure>

![split]()

### Technical Metadata

<div class="callout-specs">
ASPECT: 16:9 RATIO<br>
GRID: 12-UNIT ORTHOGONAL MODULE<br>
GRAIN: UNCOATED COTTON FIBER
</div>

Body text after the specs block.

---

<!-- _class: cols-2 -->
<!-- _style: "--accent: #0066CC;" -->

## Accent Override

- Bullets, **bold**, and borders inherit `--accent`.
- This slide sets `--accent: #0066CC`.

> [TAG](#card)
> ### Accent Card
> Tag and left rule follow the accent.

![split]()

> [](#a) **Accent Alert**
> Alert border follows the accent.

| Key | Value |
| :--- | ---: |
| **accent** | `#0066CC` |

---

<!-- _class: invert cols-2 -->

## Inverted Mode

### Subsection on Dark

- Typography flips to white with accent highlights.
- `inline code` and **bold** on dark ground.

> [TAG](#card)
> ### Card on Dark
> Card hairlines on the inverted ground.

![split]()

> [](#d) **Dark Module on Dark**
> Module must stay distinguishable from the inverted ground.

| Key | Value |
| :--- | ---: |
| **mode** | invert |

---

## Stress: A Deliberately Long Section Title That Must Wrap Gracefully Across Two Lines

Paragraph below a two-line heading. The heading underline and the spacing to the body must stay consistent when the title wraps.

- First point with moderately long text to fill the measure of the line.
- Second point with moderately long text to fill the measure of the line.
- Third point with moderately long text to fill the measure of the line.
- Fourth point with moderately long text to fill the measure of the line.

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
- Item three

> [](#a) **Limit**
> Last block near the bottom edge.
