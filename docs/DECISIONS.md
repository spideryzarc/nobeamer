# Design decisions

The nobeamer project is a **family of two Marp themes** that share one Markdown grammar but follow two
different design concepts. This file records the decisions that separate them; every change to a theme,
its demo or its docs should be consistent with it.

## The family

| | `nobeamer` | `nobeamer-swiss` |
| :--- | :--- | :--- |
| Concept | Skeuomorphic, warm, intentionally messy | International Typographic Style, printed on paper |
| Use case | Long live teaching sessions (the marathon of a course) | Study material, read later as PDF |
| Medium | Live HTML deck, projector | PDF and screen reading |
| Movement | Entrance animations and the `nobeamer` transition | Nothing depends on animation, transition or scrolling |
| Colour | Fixed palette, zero-config | One configurable accent (`--accent`), ink and paper |
| Materiality | Paper photos, post-its, glossy objects | Pure-CSS paper grain, card stock with cast shadows |

Both themes live in this repository, share one installation and are named `nobeamer` and `nobeamer-swiss`.

## Decisions

1. **Swiss use case**: study material, read later as PDF.
2. **Grammar**: total compatibility. Switching `theme:` must never lose content or break a slide. The Swiss
   grammar is the reference; the original adapts to it. Neither theme keeps legacy compatibility code
   (no aliases, no HTML-class duplicates of Markdown syntax).
3. **Name**: one family, `nobeamer` and `nobeamer-swiss`.
4. **Swiss materiality**: "printed Swiss": paper grain, cards and code as card stock.
5. **`#step` / `#def`**: removed; their role is covered by `#card` (tag + title + body).
6. **Image modifiers** (`rounded`, `rounded-sm`, `rounded-lg`, `circle`, framed backgrounds, `drop-shadow`):
   part of the grammar; the Swiss theme implements them too. Using them is the author's choice.
7. **`code-scroll`**: stays as it is, in both themes.
8. **PDF weight**: the demo photos were the first cost (up to 7806px wide); they now stay under 1600px
   (images/: 30 MB to 5.8 MB; original demo PDF: 8.4 MB). The Swiss demo PDF is still 23 MB: Chrome rasterizes
   every area that uses a blend mode (the `multiply` lead field alone costs ~5 MB over 6 lead slides; the
   `soft-light` grain and card noise cost most of the rest). Open item: reduce blend modes in Swiss.
9. **Elements that only existed in Swiss** (`#card`, `cols-2-a`, `cols-3-a`, `lead`, `invert`, `accent`, `grid`,
   `tiles`, italic figure captions): the original implements all of them, in its own style.
10. **Syntax documentation**: one reference per theme (`docs/<theme>/REFERENCE.md`).
11. **Swiss principles**: grid and measured asymmetry; typography makes the hierarchy; one accent, ink and paper;
    made to be read later.
12. **Demo photos**: at most 1600px on the long side.
13. **Colour in the original**: it accepts the syntax (`--accent`, `_class: accent`) but keeps its fixed palette.
    It stays zero-config.
14. **Meaning of `>`**: only the syntax is shared; each theme's manifesto defines what a plain quote is for
    (the original: the teacher's voice; Swiss: an editorial pull quote).
15. **Swiss is not a live show**: whatever matters must survive the PDF export.
16. **Order of the refactor**: documents first, then the CSS.

## The shared grammar (contract)

Everything below works in both themes. A new element is added to both themes or to none.

| Kind | Syntax |
| :--- | :--- |
| Slide classes | `lead`, `invert`, `accent`, `cols-2`, `cols-3`, `cols-2-a`, `cols-3-a`, `grid`, `tiles` (combinable with `<!-- _class: a b -->`) |
| Column break | `![split]()` |
| Status cards | `> [](#i)`, `> [](#a)`, `> [](#s)`, `> [](#d)` |
| Structural card | `> [TAG](#card)` + `### Title` (or `### <!-- fit --> Title`, or `**Title**`) + body |
| Card alignment | suffix `-c` (centre) or `-r` (right) on any marker: `#i-c`, `#card-r`; `-l` is the default |
| Plain quote | `> text` (meaning defined per theme) |
| Figure | `![w:560 h:220](image.jpg)` followed on the next line by `*Caption*` |
| Image modifiers | `rounded`, `rounded-sm`, `rounded-lg`, `circle` in the alt text; Marp filters such as `drop-shadow` |
| Framed background | any word in the alt text of a `bg` image rounds it: `![bg rounded](image.jpg)`; with a size (`![bg 80% rounded](…)`) the clip follows the image |
| Lead metadata | a Markdown list on a `lead` slide: `- **Key**: value` |
| HTML blocks | `<div class="math-resolution">`, `<div class="code-scroll">` (the only two HTML classes) |
| Colour | `--accent` (Swiss uses it; the original ignores it) |
| Transition | `transition: nobeamer` or `transition: swiss` (per theme, not part of the grammar) |
