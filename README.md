> "Não os esconderemos dos seus filhos; contaremos à geração vindoura os louvores do Senhor, e o seu poder, e as maravilhas que fez." (Salmo 78:4)

# nobeamer

`nobeamer` is a family of two [Marp](https://marp.app/) themes for teaching, built as an alternative to the rigid
sterility of **LaTeX Beamer** and the stark minimalism of the **standard Marp theme**. Both themes read the same
Markdown: a deck switches from one to the other by changing `theme:` in its front matter.

| | [`nobeamer`](docs/nobeamer/MANIFESTO.md) | [`nobeamer-swiss`](docs/swiss/MANIFESTO.md) |
| :--- | :--- | :--- |
| **For** | Long live teaching sessions, shown on a projector | Study material, read later as PDF |
| **Concept** | Skeuomorphic, warm, intentionally messy | International Typographic Style, printed on paper |
| **Looks like** | Paper, post-its, index cards, handwritten notes | Modular grid, flush-left type, one accent colour |
| **Moves** | Entrance animations and a dissolve between slides | Nothing depends on motion; everything survives the PDF |
| **Colour** | Fixed palette, zero-config | One configurable accent (`--accent`) |

## Which one?

- Teaching **live**, for hours, to a tired room with an old projector? Use **`nobeamer`**.
- Writing material people will **read again**, print or study from a PDF? Use **`nobeamer-swiss`**.

Since the grammar is shared, you can teach with `nobeamer` and hand out the same deck rendered with
`nobeamer-swiss`.

## Demos

- **[`nobeamer` features tour](https://spideryzarc.github.io/nobeamer/demo.marp.html)** ([source](demo.marp.md))
- **[`nobeamer` applied: the quadratic formula](https://spideryzarc.github.io/nobeamer/bhaskara.marp.html)** ([source](bhaskara.marp.md))
- **[`nobeamer-swiss` feature guide](https://spideryzarc.github.io/nobeamer/demo-swiss.marp.html)** ([source](demo-swiss.marp.md))

## Documentation

| | |
| :--- | :--- |
| [Installation and setup](docs/INSTALL.md) | Files, VS Code, front matter, CLI, transitions, PDF (both themes) |
| [`nobeamer` manifesto](docs/nobeamer/MANIFESTO.md) | What the original theme is and is not, and how to use it |
| [`nobeamer` reference](docs/nobeamer/REFERENCE.md) | The full syntax, as `nobeamer` draws it |
| [`nobeamer-swiss` manifesto](docs/swiss/MANIFESTO.md) | What the Swiss theme is and is not, and how to use it |
| [`nobeamer-swiss` reference](docs/swiss/REFERENCE.md) | The full syntax, as `nobeamer-swiss` draws it |
| [Design decisions](docs/DECISIONS.md) | Why the family is split this way, and the shared grammar both themes implement |

## Quick start

```yaml
---
marp: true
theme: nobeamer        # or: nobeamer-swiss
paginate: true
transition: nobeamer   # or: swiss
---
```

Copy the theme CSS next to your decks (plus `nb_img/` for `nobeamer`) and register it in VS Code; the
[installation guide](docs/INSTALL.md) has the details, or let an AI assistant do it with [MARP_INIT.md](MARP_INIT.md).
