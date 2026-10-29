# nobeamer — working notes for Claude

Two Marp themes live here: `nobeamer.css` (original, skeuomorphic) and `nobeamer-swiss.css` (Swiss design,
under development on branch `dev`). `demo-swiss.marp.md` is both the Swiss feature guide and the test deck.

## Default review loop (Swiss theme)

After every change to `nobeamer-swiss.css` or `demo-swiss.marp.md`:

1. Check with the lab (see `lab/README.md`): `uv run lab/swiss_lab.py lint` and `diff` (take a `baseline` before editing).
   Use `ab` to compare variants before touching the theme.
2. Rebuild the compiled demo:
   `marp demo-swiss.marp.md --html --theme-set nobeamer-swiss.css -o demo-swiss.marp.html < /dev/null`
   (stdin must be closed, or marp-cli waits on it forever).
3. Republish it as the review page, keeping the same URL: https://claude.ai/artifact/P5YoKg9BxNzW25j6sPJqnx
   Publish `demo-swiss.marp.html` with `url` set to that link and the deck's images (`images/*.jpg` referenced
   in the HTML) passed as `files`. This live HTML deck is the user's primary way to review; PNG contact sheets
   are secondary.

## Environment

- marp-cli is not preinstalled in cloud sessions: `npm i -g @marp-team/marp-cli`.
- The lab finds Chrome at `/usr/bin/google-chrome` or `/opt/pw-browsers/chromium`; override with `NOBEAMER_CHROME`.
