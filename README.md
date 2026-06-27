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

To use this theme locally in VS Code with the Marp for VS Code extension:

1. Ensure `nobeamer.css` is in your project root as well as `nb_img` folder. You don't need the `images` folder from the repo, it's just for sample slides.
2. Add the following configuration to your `.vscode/settings.json` file so Marp recognizes the custom theme:

```json
{
    "markdown.marp.themes": [
        "nobeamer.css"
    ]
}
```

1. Configure your Markdown file frontmatter to use the theme:

```yaml
---
marp: true
theme: nobeamer
transition: nobeamer
---
```

---

## Usage Guide

### Specialized Cards (Blockquotes)

Use specific links in standard blockquotes to trigger specialized card styles.

| Type | Syntax | Description |
| :--- | :--- | :--- |
| **Info** | `> [](#i) **Title**` | Yellow "Post-it" style for tips/notes. |
| **Alert** | `> [](#a) **Title**` | Red style for warnings. |
| **Success** | `> [](#s) **Title**` | Green style for solutions/results. |
| **Bento** | `> [](#d) **Title**` | Dark, digital style. Great for grids. |
| **Step** | `> [](#step) **Title**` | Glassmorphism card for timelines/syllabus. |
| **Definition** | `> [](#def) **Title**` | Glassmorphism card for definitions (purple-teal gradient). |

**Example:**

```markdown
> [](#i) **Pro Tip**
> This renders as a nice yellow card.
```

### Multi-Column Layouts

You can create 2 or 3 column layouts using section classes. Use the special image tag `![split]()` to force content into the next column.

**2 Columns:**

```markdown
<!-- _class: cols-2 -->

# Left Column
Content...

![split]()

# Right Column
Content...
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

### Print / PDF Export

All theme animations (code blocks, tables, dark blocks, lateral cards) are **automatically disabled** when exporting to PDF or printing. No manual class or configuration is needed — the theme uses `@media print` to strip animations, transitions, transforms, filters, and `backdrop-filter` globally, ensuring a clean static output.

### Slide Transitions — Per-Element "Magic Move"

The theme provides a custom `nobeamer` transition that animates **each component independently** instead of transitioning the entire slide as one block. The background stays static while titles, cards, code blocks, tables, and lists animate in and out with their own motion.

Enable it by adding `transition: nobeamer` to your frontmatter (or per-slide with `<!-- _transition: nobeamer -->`).

| Component | Exit | Enter |
| :--- | :--- | :--- |
| **Titles** (h1, h2, h3) | Fly upward | Rise from below |
| **Cards / Blockquotes** | Slide off-screen left | Slide in from right (staggered cascade) |
| **Code Blocks** | "Monitor power off" (brightness collapse) | "Monitor power on" (brightness restore) |
| **Tables / Math** | Sink downward | Rise upward |
| **Lists** (ul, ol) | Scatter to the left | Gather from the right |
| **Paragraphs** | Subtle fade | Subtle fade |
| **Page Number** | Quiet crossfade | Quiet crossfade |

Multiple cards on the same slide enter with **staggered delays**, creating a cascading effect.

> **Requirements:** Transitions work in the HTML output (Marp CLI `bespoke` template) viewed in a browser supporting the [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API) (Chrome 111+, Edge 111+, Firefox 144+, Safari 18.2+). They have no effect on PDF export.

You can also use any of Marp's [33 built-in transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md) (e.g., `fade`, `slide`, `cube`) — the per-element animations still apply on top of any directive.

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
