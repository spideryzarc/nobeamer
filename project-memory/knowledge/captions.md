---
type: Concept
title: Captions
description: How tables and figures get captions in the nobeamer grammar - one marker, [](#cap), and why it replaced italic-based captions.
tags:
- grammar
- theme
- captions
resource: ../../nobeamer.css
---

# Captions

A caption is a paragraph that starts with the empty link `[](#cap)`, placed in its own paragraph (blank line before) right after a table or an image. The theme hides the marker and renders the rest as small, centred text close to the element.

## Why this marker

- It follows the grammar's existing convention of empty-link markers (`[](#d)`, `[](#i)`, `[](#card)`), so there is one idiom for "this block has a role".
- The first design keyed on an italic-only paragraph (`*Caption*`). It misfired: any paragraph with a single italic span after a table was styled as a caption, and italics could not be used inside captions. A marker removes the ambiguity and leaves bold, italic, code and links free.
- Tables carry a bottom margin, so their caption is pulled up with a negative margin; images have none, so their caption only gets a small gap. These are separate rules on purpose.
- The earlier handwritten caption (`![img](...)` followed by `*Caption*` on the next line) was removed so the grammar has a single syntax. Decks outside this repository that used it now show that line as plain text.

## Sources

- User decision recorded in `project-memory/events/` (task `captions`).
- `nobeamer.css` caption block; README section "Captions".
