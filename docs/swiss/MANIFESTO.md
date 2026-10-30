# `nobeamer-swiss` — manifesto

`nobeamer-swiss` brings the **International Typographic Style** to Marp: a modular grid, flush-left type, one
accent colour and a lot of order. It is printed, not digital: the slide is a sheet of paper with a fine grain,
and cards and code sit on it as card stock.

**Use case**: study material. Lecture notes, technical courses, derivations, tables and code that students read
again later, mostly as a PDF. The deck has to make the structure of the subject visible and survive the export
intact.

## Principles

- **Grid and measured asymmetry**: everything sits on modules. Asymmetry comes from proportion — the 2:3 and
  3:4:5 column grids — never from misalignment.
- **Typography makes the hierarchy**: scale and weight say what matters. Colour and objects are secondary.
- **One accent, ink and paper**: a minimal palette with a single configurable colour (`--accent`); everything else
  is ink on grained paper.
- **Made to be read later**: density and clarity for study. Whatever matters is on the page, in the PDF.

## `nobeamer-swiss` is

- **Structured**: content is organised by the grid; a slide reads top-left to bottom-right like a page.
- **Typographic**: Geist for text, Literata for card bodies and quotes, IBM Plex Mono for code and data,
  Chakra Petch for technical metadata.
- **Printed**: paper grain, card stock with a cast shadow, an accent field with its own grain. Warm, but ordered.
- **Configurable in one place**: `--accent` (per deck or per slide) recolours rules, tags, bullets, tables,
  patterns and the `accent` slide.
- **Family-compatible**: it shares its Markdown grammar with [`nobeamer`](../nobeamer/MANIFESTO.md); a deck
  switches theme by changing `theme:`.

## `nobeamer-swiss` is **not**

- **A live show**: nothing depends on animation, transitions or scrolling. The `swiss` transition is a quiet
  fade, and the content does not move.
- **Decorative**: patterns (`grid`, `tiles`) and colour are used when they structure the page or mark a rhythm
  between sections, never as loose ornament.
- **Empty minimalism**: white space organises; it does not replace content. Slides can be dense.
- **Messy**: no deliberate disorder, no rotated cards, no misaligned grids.

## Guidelines

### Let the grid carry the page

Use `cols-2` and `cols-3` for comparisons and parallel content; use the asymmetric `cols-2-a` (2:3) and
`cols-3-a` (3:4:5) when one column frames and the other develops. Headings span all columns.

### Hierarchy before colour

Mark importance with heading level and weight first. `**bold**` inside a heading or a table takes the accent;
use it for the one word that matters, not for whole sentences.

### A rhythm of grounds

A long document needs breaks. Use `lead` for section dividers, `invert` and `accent` for a statement or a summary,
and the `grid` and `tiles` watermarks to mark a chapter. Keep content-heavy slides on plain paper.

### Quotes are editorial

A plain blockquote (`>`) is a pull quote: a sentence lifted from the text, set large in Literata with an accent
opening mark. Use it for a definition you want remembered or a line from a source.

### Cards are structure

`#card` holds a definition, a theorem, a step: a tag (`DEF 01`, `THM 02`) and a title over a serif body. Status
cards (`#i`, `#a`, `#s`, `#d`) are notes in the margin of the argument: information, warning, result, aside.

### Check the PDF

Read the exported PDF before sharing it. Long code in `code-scroll` scrolls only on screen; split it across slides
when the deck is meant to be printed.
