# `nobeamer` — manifesto

`nobeamer` stands as a lively alternative to the rigid sterility of **LaTeX Beamer** and the stark minimalism of
the **standard Marp theme**.

Designed for the marathon rather than the sprint, it prioritizes visual warmth and texture to keep engagement
high during extensive lectures, workshops and deep-dive sessions.

**Use case**: long live teaching sessions — a course, a workshop, three hours in front of a class with a tired
projector. The deck is shown live, in the browser, by the person who wrote it.

## `nobeamer` is

- **Native Foundation**: extends the rock-solid default Marp theme for maximum reliability and compatibility.
- **Skeuomorphic**: unapologetically inspired by real-world objects and textures — paper, post-its, index cards.
- **Built for Endurance**: tailored for frequent, heavy-content presentations (like courses), ensuring
  consistency without boring the audience.
- **High Contrast**: optimized for low-quality projection environments (bright rooms, older projectors) where
  readability is critical.
- **Intentionally Messy**: a touch of organic disorder breaks visual monotony, keeping the audience's brain
  active and attentive during long sessions.
- **Alive on screen**: cards, tables and code enter with their own small animations, and slides dissolve into
  each other. All of it switches off for PDF and print.

## `nobeamer` is **not**

- **LaTeX Beamer**: free from the complexity and sterile, rigid aesthetic of traditional TeX slides.
- **Minimalist**: rejects the trend of empty whitespace in favor of warmth and visual texture.
- **A Sales Pitch Deck**: not for 5-minute lightning talks, but for the marathon of teaching.
- **Rigidly Corporate/Academic**: trades the buttoned-up, standardized look for a friendly, approachable
  atmosphere.
- **Configurable**: an opinionated, zero-config theme with a fixed palette. It accepts the family's colour
  syntax (`--accent`, `_class: accent`) so a deck written for `nobeamer-swiss` still renders, but it keeps its
  own colours.

## Part of a family

`nobeamer` shares its Markdown grammar with [`nobeamer-swiss`](../swiss/MANIFESTO.md): a deck can switch theme
by changing `theme:` in the front matter and nothing is lost. Each theme draws the same elements its own way;
the [reference](REFERENCE.md) shows how `nobeamer` draws them.

## Guidelines

### The "Teacher's Voice"

Use plain blockquotes (`>`) for informal remarks, anecdotes or spoken-word emphasis. In `nobeamer` they look
like a handwritten note on paper, which breaks the robotic flow of formal content and re-engages the audience.

### Fight the White Space

Empty white space is the enemy of engagement in long sessions.

- **Visual Vibe Checks**: images don't always need to be informative diagrams. Teaching matrix determinants? A
  side image of a perfectly aligned tray of apples captures the *vibe* of a matrix while giving the brain a break
  from formulas.
- **Side Backgrounds**: use `![bg left:40%](…)` to fill voids with these thematic visuals.
- **Mental Palette Cleansers**: use full backgrounds, `invert` or `accent` slides to separate major sections.

### The "Proto-Bento" Grid

When using multi-column layouts, avoid perfect alignment.

- Use **Dark Blocks** (`#d`) with their built-in slight negative margins to create organic, misaligned grids.
- A slightly messy layout looks less like a spreadsheet and more like a scrapbook, which feels more human and
  less fatiguing over time.

### Index cards for structure

Definitions, steps, theorems and syllabus items are `#card`s: a tag (`DEF 01`, `STEP 2`) and a title on an index
card. They replace the old `#step` and `#def` cards.

### Contrast is King

"Dark mode" is great for coding, but often terrible for cheap classroom projectors. `nobeamer` embraces
high-contrast, light backgrounds so the back row can read every word without squinting. Keep `invert` for
section breaks, not for content-heavy slides.
