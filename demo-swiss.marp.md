---
marp: true
theme: nobeamer-swiss
paginate: true
size: 16:9
title: "nobeamer-swiss: International Typographic Style"
transition: swiss
style: ":root { --accent: #e85951; }"
---

<!-- _class: lead -->

![bg right:46% saturate:0](images/scholar_portrait.jpg)

# <!--fit--> NOBEAMER <br> **SWISS**

### *LECTURE 02 :* EMPIRICAL METHODS & EPISTEMOLOGY

- *INSTITUTE*: ETH ZÜRICH
- *COURSE*: SCI-204
- *PROF*: DR. E. VOGEL
- *YEAR*: 2026



---

<!-- _class: cols-2 -->

## Modular Grid Systems in Typography

> [DEF. 01](#def) **Grid Topology**
> Let $G = (V, E)$ denote an orthogonal modular grid where interval $\delta$ is invariant across subdivisions:
> $$\delta(x, y) = \kappa \cdot \sqrt{\Delta x^2 + \Delta y^2}$$

![split]()

### Architectural Principles

The baseline grid dictates alignment, scale, and spatial tension:

- **Asymmetry**: Flush-left, ragged-right typography establishes dynamic balance without centering.
- **Hierarchical Contrast**: Extreme scale differential between massive titles and crisp body text.
- **White Space**: Empty space functions as an active structural boundary, not passive emptiness.

---

<!-- _class: cols-2 -->

## Empirical Readability & Retention

<div style="padding-top: 10px;">
  <div class="metric">99.4%</div>
  <div class="metric-label">READABILITY INDEX</div>
  <p style="margin-top: 10px; font-size: 0.95rem; line-height: 1.28; color: #555;">
    Quantitative evaluation across technical seminars, peer defense sessions, and mathematical lecture environments.
  </p>
</div>

![split]()

> [](#step) **01 / Rational Layout**
> Information architecture based on mathematical proportion and strict horizontal baselines.

> [](#step) **02 / Cognitive Retention**
> Clean Neo-Grotesque letterforms maximize instant comprehension during lectures and defense sessions.

---

<!-- _class: cols-2 -->

## Integration of Objective Imagery

<figure>
  <img src="scratch/helvetica_alphabet_poster_2193x3348.jpg" alt="Helvetica Typographic Specimen" style="height: 380px; width: 100%; object-fit: cover;">
  <figcaption>FIG. 04.1 / HELVETICA TYPE SPECIMEN & MODULAR SPATIAL EQUILIBRIUM</figcaption>
</figure>

![split]()

### Functional Imagery

In the Swiss Style, imagery is not decorative; it documents reality with objective precision:

- **Grid Alignment**: Images align precisely to column boundaries with zero border radius.
- **Technical Captions**: Compact uppercase monospace metadata anchored to each visual asset.

<div class="callout-specs">
RATIO: 1.618 GOLDEN MEAN<br>
GRID: 12-UNIT MODULAR SYSTEM<br>
OPTICAL DENSITY: HIGH ACCURACY
</div>

---

<!-- _class: cols-2 -->

## Information Architecture Cards

> [](#i) **Technical Notice (`#i`)**
> Structured bulletin anchored to modular rules for neutral informational notes.

> [](#a) **Critical Constraint (`#a`)**
> High-priority warning rendered with the authentic Swiss Red accent bar.

![split]()

> [](#s) **Empirical Validation (`#s`)**
> Verified result or theorem conclusion with disciplined green indicator.

> [](#d) **Inverted Module (`#d`)**
> High-contrast black panel for **vital theorems**, definitions, or inline `parameter` callouts.

---

## Quantitative Data & Formal Logic

### Empirical Benchmark Summary

| Benchmark Identifier | Sample Size ($N$) | Latency (ms) | Efficiency Ratio | Validation Status |
| :--- | :--- | :--- | :--- | :--- |
| **MODULAR-GRID-A** | $12,500$ | $1.42 \pm 0.04$ | $0.984$ | **VERIFIED** |
| **ASYM-HIERARCHY-B** | $28,400$ | $2.15 \pm 0.08$ | $0.961$ | **VERIFIED** |
| **GROTESQUE-TYPE-C** | $45,000$ | $0.88 \pm 0.02$ | $0.997$ | **OPTIMAL** |

<div class="math-resolution">

$$
\mathcal{L}_{\text{swiss}}(\theta) = \sum_{k=1}^K \left[ \alpha \cdot \log \left( 1 + \frac{\text{Contrast}(k)}{\text{Noise}(k)} \right) - \beta \cdot \|\nabla_{\text{grid}} \Phi(k)\|_2^2 \right]
$$

</div>

---

<!-- _class: cols-2 -->

## Code Presentation & Architecture

- **Clean Syntax**: High legibility monospace with zero skeuomorphic gloss or scanlines.
- **Hairline Framing**: 1.5px black container with a solid Swiss Red accent bar.

<div class="code-scroll">

```python
# Swiss Grid Transformation Engine
import numpy as np

def compute_modular_grid(width: int = 1920, height: int = 1080, columns: int = 12) -> dict:
    """
    Calculates exact mathematical grid intervals for Swiss layout generation.
    """
    gutter = 24
    margin_x = 56
    usable_width = width - (2 * margin_x)
    total_gutters = (columns - 1) * gutter
    col_width = (usable_width - total_gutters) / columns
    
    col_boundaries = [
        margin_x + i * (col_width + gutter)
        for i in range(columns)
    ]
    
    return {
        "columns": columns,
        "column_width": round(col_width, 2),
        "gutter": gutter,
        "boundaries": col_boundaries,
        "aspect_ratio": "16:9"
    }

# Execute calculation
grid_spec = compute_modular_grid()
print(f"Computed Swiss Grid: {grid_spec['column_width']}px per module")
```

</div>

---

<!-- _class: cols-2 -->

## Definitive Swiss Typographic Stack

| Layer | Font Family | Role & Execution |
| :--- | :--- | :--- |
| **Display & Titles** | **Geist** (800 / 900 Black) | Monumental impact, uppercase, tight tracking ($-4\%$) |
| **Body & Content** | **Geist** (Regular / 400) | Maximum on-screen neutrality and optical balance |
| **Grid & Metadata** | **IBM Plex Mono** (600 / 700) | Slide numbers, tabular data, tags (`01 // INTRO`) |

<div class="callout-specs" style="margin-top: 24px;">
TRACKING: -2% TO -4% FOR TITLES<br>
TABULAR NUMS: LINING NUMERICS<br>
PRIMARY: GEIST SANS (VERCEL)
</div>

![split]()

### Architectural Principles

The International Typographic Style eliminates arbitrary ornaments in favor of structural clarity:

- **Objective Neutrality**: Sem serifas neo-grotescas puras desenhadas para legibilidade máxima em telas e apresentações.
- **Hierarchical Tension**: Contraste monumental entre títulos em caixa-alta e corpo de texto corrido.
- **Mathematical Precision**: Numeração técnica, tags de metadados e dados tabulares estritamente alinhados ao grid modular.

---

<!-- _class: cols-2 -->
<!-- _style: "--accent: #0066CC;" -->

## Theme Parameterization & Accent Colors

### Dynamic Semantic Palette

The primary accent color (default Swiss Red `#E30613`) is controlled directly by the single CSS custom property `--accent`:

- **Global Frontmatter Override**:
  `style: ":root { --accent: #FF5500; }"`
- **Single Slide Override**:
  `<!-- _style: "--accent: #0066CC;" -->`

Zero helper classes, zero layout conflicts — everything inherits from `--accent` directly.

![split]()

> [](#a) **Single Variable Control**
> This slide sets `<!-- _style: "--accent: #0066CC;" -->`. The alert card, headline strong text, and rules inherit `#0066CC` automatically.

<div class="callout-specs">
VARIABLE: --accent<br>
SLIDE OVERRIDE: #0066CC<br>
ARCHITECTURE: PURE CSS VARIABLE
</div>

---

<!-- _class: invert cols-2 -->

## Inverted Contrast Mode

### High-Contrast Visual Balance

The `invert` class provides an uncompromising deep black (`#111111`) environment suited for dramatic conclusions, keynote openers, or evening presentations.

<div class="callout-specs" style="color: #FFFFFF; border-left-color: var(--swiss-red); margin: 18px 0;">
STATUS: PRODUCTION-READY<br>
COMPATIBILITY: MARP CLI & VS CODE<br>
IDENTITY: NOBEAMER-SWISS
</div>

![split]()

> [](#d) **Core Tenet of Swiss Modernism**
> *"Design is the method of putting form and content together. Design, just as art, has multiple definitions; there is no single definition. Design can be art. Design can be aesthetics. Design is so simple, that's why it is so complicated."*
> — Paul Rand
