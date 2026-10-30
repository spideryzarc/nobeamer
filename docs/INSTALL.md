# Installation and technical setup

This guide covers both themes of the family. For what each theme is for, read its manifesto
([`nobeamer`](nobeamer/MANIFESTO.md), [`nobeamer-swiss`](swiss/MANIFESTO.md)); for the syntax, its reference
([`nobeamer`](nobeamer/REFERENCE.md), [`nobeamer-swiss`](swiss/REFERENCE.md)).

> 💡 **Automated setup with AI**: with Antigravity, GitHub Copilot, Cursor or a similar tool you can scaffold the
> whole environment by running the prompt in [MARP_INIT.md](../MARP_INIT.md). It asks which theme to install.

## 1. Files

| Theme | Files to copy next to your decks | External resources |
| :--- | :--- | :--- |
| `nobeamer` | `nobeamer.css` and the `nb_img/` folder (paper textures) | Google Fonts (Caveat, Cousine, Josefin Sans) |
| `nobeamer-swiss` | `nobeamer-swiss.css` only (the paper is pure CSS) | Google Fonts (Geist, Literata, IBM Plex Mono, Chakra Petch) |

The `images/` folder of this repository only holds the demo pictures; you don't need it.

Without internet access the fonts fall back to system fonts (Helvetica/Arial, Times, Courier). Layouts are
designed to survive that, but the look is only right with the web fonts.

## 2. VS Code (Marp for VS Code)

Register the themes in `.vscode/settings.json`. Register both if you want to switch between them:

```json
{
    "markdown.marp.themes": [
        "nobeamer.css",
        "nobeamer-swiss.css"
    ],
    "markdown.marp.enableHtml": true
}
```

`enableHtml` is needed for the two HTML blocks of the grammar (`math-resolution`, `code-scroll`).

## 3. Front matter

```yaml
---
marp: true
theme: nobeamer        # or: nobeamer-swiss
paginate: true
transition: nobeamer   # or: swiss
math: mathjax
---
```

Both themes read the same Markdown, so switching is a change of `theme:` (and of the matching `transition:`).

## 4. Marp CLI

```bash
npx @marp-team/marp-cli deck.md --html --theme-set nobeamer.css nobeamer-swiss.css -o deck.html
```

```bash
npx @marp-team/marp-cli deck.md --pdf --allow-local-files --theme-set nobeamer.css nobeamer-swiss.css -o deck.pdf
```

`--allow-local-files` lets the PDF renderer read local images and the `nb_img/` textures.

## 5. Transitions

`transition: nobeamer` (a dissolve that settles into place) and `transition: swiss` (a quiet fade) work in the HTML
output (Marp CLI `bespoke` template) in browsers with the
[View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API) (Chrome/Edge 111+,
Firefox 144+, Safari 18.2+). They have no effect on PDF. With *reduce motion* enabled in the OS, Marp falls back to a
plain fade. The duration can be tuned per directive, e.g. `transition: nobeamer 0.4s`. Marp's
[built-in transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md) also work.

## 6. PDF and print

- `nobeamer` disables every animation, transition, transform and filter under `@media print`, so the PDF is static.
- `nobeamer-swiss` has no element animations to begin with.
- In both, `code-scroll` only scrolls on screen: in a PDF the hidden part of a long block is not printed.
- Areas that use CSS blend modes (the Swiss lead photo field, grain and card stock) are rasterized by Chrome when
  printing, which makes PDFs heavier. Keep photos at a reasonable size (the demo images are at most 1600px).
