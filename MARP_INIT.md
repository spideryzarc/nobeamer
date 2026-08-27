# Marp Project Initialization (`/marp-init`)

**Role**: Marp Environment & Architecture Specialist  
**Objective**: Scaffold or initialize a standardized Marp presentation environment in the active project directory, ensuring `marp/` folder structure, theme assets, and native IDE configuration are ready.

---

## 1. Directory Structure

Ensure the following directory structure exists in the project root:

```text
<project-root>/
├── .vscode/
│   ├── settings.json       # VS Code / IDE settings for Marp extension
│   └── tasks.json          # Optional: Native IDE build tasks using npx @marp-team/marp-cli
├── marp.config.js          # Marp CLI configuration (theme & engine options)
├── marp/
│   ├── nobeamer.css        # nobeamer custom theme stylesheet
│   ├── README_nobeamer.md  # nobeamer documentation & reference (avoids conflict with project README)
│   ├── nb_img/             # Theme texture assets (paper.jpg, paper2.jpg)
│   │   ├── paper.jpg
│   │   └── paper2.jpg
│   ├── images/             # Presentation image assets directory
│   └── starter.marp.md     # Initial slide deck template (if no slide deck exists)
```

---

## 2. Theme & Asset Setup

Execute or automate the asset retrieval using `marp_init_theme.py` (or fetching from GitHub if local cache is absent):

```bash
uv run ~/.agents/shared/scripts/marp_init_theme.py marp/ --no-vscode
```

Or manually ensure files are downloaded from GitHub (`spideryzarc/nobeamer`):
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/nobeamer.css` -> `marp/nobeamer.css`
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/README.md` -> `marp/README_nobeamer.md`
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/nb_img/paper.jpg` -> `marp/nb_img/paper.jpg`
- `https://raw.githubusercontent.com/spideryzarc/nobeamer/main/nb_img/paper2.jpg` -> `marp/nb_img/paper2.jpg`

Ensure directory `marp/images/` is created for presentation graphics.

---

## 3. Configuration Files

### A. `.vscode/settings.json`
Configure the Marp IDE extension to recognize the theme:

```json
{
  "markdown.marp.themes": [
    "marp/nobeamer.css",
    "nobeamer.css"
  ],
  "markdown.marp.enableHtml": true
}
```

### B. `marp.config.js`
Provide root CLI configuration for Marp:

```javascript
module.exports = {
  themeSet: ['./marp/nobeamer.css', './nobeamer.css'],
  html: true,
  allowLocalFiles: true
};
```

### C. `.vscode/tasks.json` (Native IDE Tasks)
Configure native build tasks invoking standard Marp CLI directly without custom wrappers:

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

Scaffold a starter presentation in `marp/starter.marp.md`:

```markdown
---
marp: true
theme: nobeamer
class: lead
paginate: true
size: 16:9
title: "Presentation Title"
author: "Author"
description: "Presentation description"
transition: nobeamer
---

# Presentation Title
## Subtitle or Topic

- Key Objective 1
- Key Objective 2
```

---

## 5. Execution Summary
When invoked:
1. Create `marp/`, `marp/images/`, `marp/nb_img/` and `.vscode/` if missing.
2. Ensure `nobeamer.css` and background textures (`paper.jpg`, `paper2.jpg`) are placed inside `marp/`.
3. Create/update `.vscode/settings.json`, `marp.config.js`, and `.vscode/tasks.json`.
4. Inform the user that the environment is ready for slide authoring and native compilation via IDE shortcuts (`Ctrl+Shift+B` or Marp extension).
