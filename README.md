> "Não os esconderemos dos seus filhos; contaremos à geração vindoura os louvores do Senhor, e o seu poder, e as maravilhas que fez." (Salmo 78:4)

# nobeamer

`nobeamer` stands as a lively alternative to the rigid sterility of **LaTeX Beamer** and the stark minimalism of the **standard Marp theme**.

Designed for the marathon rather than the sprint, it prioritizes visual warmth and texture to keep engagement high during extensive lectures, workshops, and deep-dive sessions.

## `nobeamer` is

- **Native Foundation**: Extends the rock-solid default Marp theme for maximum reliability and compatibility
- **Skeuomorphic**: Unapologetically inspired by real-world objects and textures
- **Built for Endurance**: Tailored for frequent, heavy-content presentations (like courses), ensuring consistency without boring the audience
- **High Contrast**: Optimized for low-quality projection environments (bright rooms, older projectors) where readability is critical
- **Intentionally Messy**: A touch of organic disorder breaks visual monotony, keeping the audience's brain active and attentive during long sessions

## `nobeamer` is **not**

- **LaTeX Beamer**: Free from the complexity and sterile, rigid aesthetic of traditional TeX slides
- **Minimalist**: Rejects the trend of empty whitespace in favor of warmth and visual texture
- **A Sales Pitch Deck**: Not for 5-minute lightning talks, but for the marathon of teaching
- **Rigidly Corporate/Academic**: Trades the buttoned-up, standardized look for a friendly, approachable atmosphere
- **Endlessly Configurable**: An opinionated, zero-config theme. No parameters or color schemes to fiddle with—it works perfectly out of the box (though you are free to fork)

## Demos

Check out the compiled HTML examples included in this repository:

- **[Theme Features Tour](https://spideryzarc.github.io/nobeamer/demo.marp.html)**
- **[The Quadratic Formula](https://spideryzarc.github.io/nobeamer/bhaskara.marp.html)** (Applied example: Making math visual)

## Installation & Setup

> 💡 **Automated Setup with AI:** If you are using Antigravity, GitHub Copilot, Cursor, or similar tools, you can scaffold your entire presentation environment automatically by running the prompt in **[MARP_INIT.md](MARP_INIT.md)**.


To use this theme locally in VS Code with the Marp for VS Code extension:

1. Ensure `nobeamer.css` is in your project root as well as `nb_img` folder. You don't need the `images` folder from the repo, it's just for sample slides.
2. Add the following configuration to your `.vscode/settings.json` file so Marp recognizes the custom theme:

```json
{
    "markdown.marp.themes": [
        "nobeamer.css"
    ],
    "markdown.marp.enableHtml": true
}
```

3. Configure your Markdown file frontmatter to use the theme:

```yaml
---
marp: true
theme: nobeamer
transition: nobeamer
---
```


---

## Usage Guide

### Slide Classes

Set per slide with `<!-- _class: name -->`; combine with spaces (`<!-- _class: accent grid -->`).

| Class | Look |
| :--- | :--- |
| `lead` | Title slide: flush-left, large title with its gold bar, handwritten subtitle; a Markdown list becomes the metadata line at the bottom. Works with side backgrounds (`![bg left:50%](…)`). |
| `invert` | A chalkboard: dark slate with chalk dust, chalk-white text, yellow chalk for bold in titles. Paper notes and post-its stick to it. |
| `accent` | A sheet of blue construction paper with white text. |
| `cols-2`, `cols-3` | Columns; `![split]()` starts the next one. |
| `cols-2-a`, `cols-3-a` | Asymmetric columns, 2:3 and 3:4:5. |
| `grid` | Notebook graph paper with a red margin line under the content. |
| `tiles` | A faint watermark of modular rounded tiles with three gold circles. |

`grid` and `tiles` also work with `invert` (chalk lines) and `accent`.

`lead` is a title slide: set it per slide (`<!-- _class: lead -->`), not for the whole deck in the front matter.

```markdown
<!-- _class: lead -->

# The Quadratic Formula
## Making the Boring Beautiful

- **Course**: Algebra I
- **Date**: 2026-10-30

![bg left:50%](images/parabola_arch.png)
```

### Specialized Cards (Blockquotes)

Use specific links in standard blockquotes to trigger specialized card styles.

| Syntax | Card |
| :--- | :--- |
| `> [](#i) **Title**` | Information — yellow post-it |
| `> [](#a) **Title**` | Alert — red post-it |
| `> [](#s) **Title**` | Success — green post-it |
| `> [](#d) **Title**` | Dark block — glossy, rounded, for "proto-bento" grids |
| `> [TAG](#card)` | Index card — definitions, theorems, steps, syllabus items |

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

**Index card (`#card`):** a plain cream card with softly rounded corners and a red header rule. The tag (`[TAG](#card)`, or `[](#card)` for none) is a slightly crooked gold sticker. The title is an optional `###` heading (`### <!--fit-->` fills the width up to the tag); without it the card has no title and **bold** is just bold. `#card-c` centres the content; `#card-r` aligns it right and moves the sticker to the left.

```markdown
> [DEF 01](#card)
> ### Algorithm
> A finite sequence of well-defined instructions…
```

### Multi-Column Layouts

You can create 2 or 3 column layouts using section classes. Use the special image tag `![split]()` to force content into the next column. The slide title spans all columns.

**2 Columns:**

```markdown
<!-- _class: cols-2 -->

## Title (spans all columns)

Left column…

![split]()

Right column…
```

**3 Columns:**

```markdown
<!-- _class: cols-3 -->
Column 1
![split]()
Column 2
![split]()
Column 3
```

**Asymmetric columns:** `cols-2-a` gives the first column 2/5 of the width and the second 3/5; `cols-3-a` splits 3:4:5. Content that is too tall spills downward (visible), never into a hidden column.

### Image Modifiers & Formatting

`nobeamer` supports Marp's native CSS filters alongside custom theme keywords for corner rounding within image tags (`![...]`).

| Modifier | Example Syntax | Description |
| :--- | :--- | :--- |
| **Rounded** | `![w:300 rounded](image.jpg)` | Standard rounded corners (`16px`). |
| **Small Round** | `![w:300 rounded-sm](image.jpg)` | Slightly rounded corners (`8px`). |
| **Large Round** | `![w:300 rounded-lg](image.jpg)` | Pronounced rounded corners (`28px`). |
| **Circle** | `![w:200 circle](image.jpg)` | Circular crop (`50%` border-radius). |
| **Native Filters** | `![w:300 opacity:80% sepia:50%](image.jpg)` | Native Marp CSS filters (`opacity`, `sepia`, `saturate`, `grayscale`, `blur`, `brightness`, `contrast`). |
| **Caption** | `![w:420 h:200](image.jpg)` + `*Caption*` on the next line | Figure with a handwritten caption under it. |
| **Framed Background** | `![bg left:45% 85% rounded](image.jpg)` | Rounded side background; with a size, the clip follows the image. |

**Example:**

```markdown
![w:250 rounded drop-shadow](images/photo.jpg)
![w:200 circle](images/profile.jpg)
```

### Math & Formulas

For extensive mathematical derivations, use the `.math-resolution` class. This creates a focused, paper-styled block distinct from standard slides.

```html
<div class="math-resolution">
$$
\begin{aligned}
    P(X \le x) &= \sum_{i=0}^x \binom{n}{i} p^i (1-p)^{n-i}
\end{aligned}
$$
</div>
```

### Scientific Tables

Tables are automatically styled to resemble APA/Scientific publication standards—minimal vertical lines, strong horizontal delimiters, and monospaced data for precision.

### Visual Code Blocks

Code blocks (`pre`) are styled with a glossy, Mac-OS inspired aesthetic to pop against paper backgrounds. No special class is required.

### Scrollable Long Code Blocks (`<div class="code-scroll">`)

For exceptionally long code snippets that need to be presented without being compressed or scaled down by Marp, wrap your standard code block inside a `<div class="code-scroll">` container.

- **Uncompressed Font**: Neutralizes automatic downscaling, keeping the font 100% sharp and readable.
- **Automatic Line Wrapping**: Long lines wrap naturally within the card boundaries (`word-break: break-word`), eliminating unwanted horizontal scrolling.
- **Dedicated Vertical Scrollbar**: Styled scrollbar allowing mouse/trackpad scrolling during interactive presentations without changing slides.
- **Full Syntax Highlighting**: Fully preserves Marp's native syntax highlighting (`highlight.js`).

```html
<div class="code-scroll">

```python
# Extended code snippet (paste directly without any '>' prefix)
def process_data(records: list[dict]) -> dict:
    ...
```

</div>
```
### Print / PDF Export

All theme animations (code blocks, tables, dark blocks, lateral cards) are **automatically disabled** when exporting to PDF or printing. No manual class or configuration is needed — the theme uses `@media print` to strip animations, transitions, transforms, filters, and `backdrop-filter` globally, ensuring a clean static output.

### Slide Transitions — Dissolve

The theme provides a custom `nobeamer` transition: a quiet dissolve where the next slide fades in over the current one and settles into place from slightly larger going forward, slightly smaller going back. Inside each slide, cards, tables and code blocks still play their own entrance animations.

Enable it by adding `transition: nobeamer` to your frontmatter (or per-slide with `<!-- _transition: nobeamer -->`). The duration can be tuned per directive, e.g. `transition: nobeamer 0.4s`.

The transition animates the slide as a whole on purpose. Per-element morphing ("magic move") was removed because it froze browsers in fullscreen when a card overflowed a `cols-2`/`cols-3` column.

> **Requirements:** Transitions work in the HTML output (Marp CLI `bespoke` template) viewed in a browser supporting the [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API) (Chrome 111+, Edge 111+, Firefox 144+, Safari 18.2+). They have no effect on PDF export. With *reduce motion* enabled in the OS, Marp falls back to a plain fade.

You can also use any of Marp's [33 built-in transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md) (e.g., `fade`, `slide`, `cube`).

## Guidelines

### The "Teacher's Voice"

Use standard blockquotes (`>`) for informal remarks, anecdotes, or spoken-word emphasis. This mimics a handwritten note and helps break the robotic flow of formal content, re-engaging the audience's attention.

### Fight the White Space

Empty white space is the enemy of engagement in long sessions.

- **Visual Vibe Checks**: Images don't always need to be informative diagrams. Teaching matrix determinants? A side image of a perfectly aligned tray of apples captures the *vibe* of a matrix while giving the brain a break from formulas.
- **Side Backgrounds**: Use `bg left:xxx` to fill voids with these thematic visuals.
- **Mental Palette Cleansers**: Use full backgrounds to separate major sections.

### The "Proto-Bento" Grid

When using multi-column layouts, avoid perfect alignment.

- Use **Dark Blocks** (`#d`) with slight negative margins (builtin) to create organic, misaligned grids.
- A slightly messy layout looks less like a spreadsheet and more like a scrapbook, which feels more human and less fatiguing over time.

### Contrast is King

"Dark mode" is great for coding, but often terrible for cheap classroom projectors. `nobeamer` embraces high-contrast, light backgrounds to ensure that even the back row can read every word without squinting.
