# Marp Project Initialization (`/marp-init`)

**Role**: Marp Environment & Architecture Specialist
**Objective**: Scaffold or initialize a standardized Marp presentation environment in the active project directory
with one (or both) themes of the nobeamer family, ensuring the `marp/` folder structure, theme assets and native IDE
configuration are ready.

---

## 0. Choose the theme

Ask the user which theme to install (default: `nobeamer`):

| Theme | Use case | Assets |
| :--- | :--- | :--- |
| `nobeamer` | Long live teaching sessions on a projector | `nobeamer.css` + `nb_img/` (paper textures) |
| `nobeamer-swiss` | Study material, read later as PDF | `nobeamer-swiss.css` only |
| both | Teach with `nobeamer`, hand out with `nobeamer-swiss` | all of the above |

Both themes read the same Markdown, so installing both lets the user switch with `theme:`.

---

## 1. Directory Structure

```text
<project-root>/
├── .vscode/
│   ├── settings.json         # VS Code / IDE settings for the Marp extension
│   └── tasks.json            # Optional: native IDE build tasks using npx @marp-team/marp-cli
├── marp.config.js            # Marp CLI configuration (themes & engine options)
├── marp/
│   ├── nobeamer.css          # if nobeamer is installed
│   ├── nb_img/               # if nobeamer is installed (paper.jpg, paper2.jpg)
│   ├── nobeamer-swiss.css    # if nobeamer-swiss is installed
│   ├── REFERENCE_<theme>.md  # syntax reference of each installed theme
│   ├── images/               # presentation image assets
│   └── starter.marp.md       # initial slide deck template (if no slide deck exists)
```

---

## 2. Theme & Asset Setup

Fetch from GitHub (`spideryzarc/nobeamer`, branch `main`) only what the chosen theme needs:

**`nobeamer`**
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/nobeamer.css` → `marp/nobeamer.css`
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/nb_img/paper.jpg` → `marp/nb_img/paper.jpg`
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/nb_img/paper2.jpg` → `marp/nb_img/paper2.jpg`
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/docs/nobeamer/REFERENCE.md` → `marp/REFERENCE_nobeamer.md`

**`nobeamer-swiss`**
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/nobeamer-swiss.css` → `marp/nobeamer-swiss.css`
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/docs/swiss/REFERENCE.md` → `marp/REFERENCE_nobeamer-swiss.md`

Create `marp/images/` for presentation graphics. If a local helper is available, it may be used instead:

```bash
uv run ~/.agents/shared/scripts/marp_init_theme.py marp/ --no-vscode
```

---

## 3. Configuration Files

List only the installed theme files in the settings below.

### A. `.vscode/settings.json`

```json
{
  "markdown.marp.themes": [
    "marp/nobeamer.css",
    "marp/nobeamer-swiss.css"
  ],
  "markdown.marp.enableHtml": true
}
```

### B. `marp.config.js`

```javascript
module.exports = {
  themeSet: ['./marp/nobeamer.css', './marp/nobeamer-swiss.css'],
  html: true,
  allowLocalFiles: true
};
```

### C. `.vscode/tasks.json` (Native IDE Tasks)

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Marp: Export current file to HTML",
      "type": "shell",
      "command": "npx -y @marp-team/marp-cli \"${file}\" --config-file marp.config.js --html -o \"${fileDirname}/${fileBasenameNoExtension}.html\"",
      "group": "build",
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    },
    {
      "label": "Marp: Export current file to PDF",
      "type": "shell",
      "command": "npx -y @marp-team/marp-cli \"${file}\" --config-file marp.config.js --pdf --allow-local-files -o \"${fileDirname}/pdf/${fileBasenameNoExtension}.pdf\"",
      "group": "build",
      "problemMatcher": [],
      "presentation": {
        "reveal": "always",
        "panel": "shared"
      }
    },
    {
      "label": "Marp: Preview (Watch)",
      "type": "shell",
      "command": "npx -y @marp-team/marp-cli \"${file}\" --config-file marp.config.js --preview",
      "group": "build",
      "problemMatcher": []
    }
  ]
}
```

---

## 4. Starter Presentation

Scaffold `marp/starter.marp.md` with the chosen theme (`nobeamer` + `transition: nobeamer`, or `nobeamer-swiss` +
`transition: swiss`):

```markdown
---
marp: true
theme: nobeamer
paginate: true
size: 16:9
title: "Presentation Title"
author: "Author"
description: "Presentation description"
transition: nobeamer
---

<!-- _class: lead -->

# Presentation Title
## Subtitle or Topic

- **Author**: Name
- **Course**: Topic
```

---

## 5. Execution Summary

When invoked:
1. Ask which theme to install (`nobeamer`, `nobeamer-swiss` or both).
2. Create `marp/`, `marp/images/` and `.vscode/` (and `marp/nb_img/` for `nobeamer`) if missing.
3. Download the chosen theme files and their references into `marp/`.
4. Create/update `.vscode/settings.json`, `marp.config.js` and `.vscode/tasks.json` with the installed themes.
5. Tell the user the environment is ready, and point to the reference of the installed theme(s).
