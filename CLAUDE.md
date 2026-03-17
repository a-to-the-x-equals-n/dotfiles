# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
./setup.sh       # Symlinks micro config and injects bash sourcing into ~/.bashrc
source ~/.bashrc # Reload shell after setup
```

`setup.sh` symlinks `micro/` configs to `~/.config/micro/` and appends sourcing lines for `.bash_exports` and `.bash_functions` to `~/.bashrc`. It has backup logic that moves existing configs to `.bak` before overwriting.

## Repository Structure

This is a WSL-focused personal dotfiles and tooling repo. The `.gitignore` ignores all files (`*`), meaning new files must be explicitly force-added with `git add -f`.

**Bash config** (`/.bash_exports`, `/.bash_functions`, `/.bash_colors`):
- `.bash_colors` defines ANSI escape codes in two formats: prompt-safe (with `\[` `\]` escapes) and echo-safe. Also defines `OK_MSG`, `ERR_MSG`, `SKIP_MSG`, `WARN`, `USAGE` templates.
- `.bash_exports` sets up PATH (includes `~/.dotfiles`), PYTHONPATH (includes `~/.dotfiles`), SSH agent socket, and sources Rust toolchain.
- `.bash_functions` defines all shell aliases and functions.

**`runes/`** — importable Python library for ANSI/terminal control:
- `runes.colors` — foreground/background color codes, 256-color support
- `runes.cursor` — cursor movement, screen clearing, scrolling
- Available via PYTHONPATH; used by multiple scripts for consistent terminal styling.

**`scripts/`** — standalone utility scripts:
- `hw.py` — homework directory navigator for `~/xdev/school/` courses
- `ocr.py` — Tesseract OCR wrapper (requires Tesseract, Pillow, pymupdf)
- `rm_zoneid.py` — recursively removes Windows `Zone.Identifier` alternate data streams (WSL interop)
- `what_colr.py` — interactive color reference tool
- `note.lua` — sticky note creator

**`gamegenie/`** — interactive cheat sheet viewer:
- Run via `gamegenie` alias (defined in `.bash_functions`)
- Cheat sheets in `gamegenie/cheats/*.md` covering ANSI, Regex, Rust, C#, .NET, Lua, Micro

**`micro/`** — Micro text editor config (symlinked to `~/.config/micro/`):
- `settings.json` — colorscheme (dracula), softwrap, wordwrap
- `bindings.json` — `Alt-/` and `Ctrl_Underscore` for commenting
- `colorschemes/` — dracula, dracula-tc, dark2, gotham, radical

## WSL Integration

Many shell functions are WSL-aware and bridge to Windows:
- `view` — opens files/folders in Windows Explorer
- `summon` — moves latest screenshot from Windows Desktop to current directory
- `winhome`/`desktop`/`whome` — path helpers with flags (`-o` open, `-ss` screenshot dir, `-d` desktop, `-r` raw path)
- `fox` — launches Firefox via PowerShell
- `WINDOWS_HOST=10.255.255.254` is set as the WSL Windows host

## Key Conventions

- **Color output**: Use `runes` library in Python scripts, or source `.bash_colors` in shell scripts for consistent styling.
- **PATH/PYTHONPATH**: Scripts in `~/.dotfiles/` are directly executable; Python modules (like `runes`) are importable without install.
