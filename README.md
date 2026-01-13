# nobeamer

`nobeamer` is a presentation theme for Marp, designed for long presentations, lectures, and workshops where readability and visual engagement are key.

## `nobeamer` is

- Based on the default Marp theme
- Modern and "Organic" (mix of paper and digital textures)
- Aimed for classes and comprehensive decks
- **High Contrast**: Optimized for low-quality projection environments (bright rooms, older projectors) where readability is critical

## `nobeamer` is **not**

- LaTeX Beamer
- Minimalist
- Aimed for 5-minute sales pitches
- Designed for rigid corporate environments (it prioritizes a friendly, organic vibe)

## Installation & Setup

To use this theme locally in VS Code with the Marp for VS Code extension:

1. Ensure `nobeamer.css` is in your project root.
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
---
```

---

## Usage Guide

### specialized Cards (Blockquotes)

Use specific links in standard blockquotes to trigger specialized card styles.

| Type | Syntax | Description |
| :--- | :--- | :--- |
| **Info** | `> [](#i) **Title**` | Yellow "Post-it" style for tips/notes. |
| **Alert** | `> [](#a) **Title**` | Red style for warnings. |
| **Success** | `> [](#s) **Title**` | Green style for solutions/results. |
| **Bento** | `> [](#d) **Title**` | Dark, digital style. Great for grids. |

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

### Protocol "Bento" Grids

Combine the **3-column layout** (`cols-3`) with **Bento Cards** (`#d`) to create modern grid layouts. The negative margins on the Bento cards allow them to fill the column width perfectly.
