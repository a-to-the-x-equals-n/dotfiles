# dotfiles

Personal shell config and tools for WSL (Ubuntu on Windows).

## Setup

```bash
git clone <repo> ~/.dotfiles
cd ~/.dotfiles
./setup.sh
source ~/.bashrc
```

`setup.sh` will:
- Append sourcing lines for `.bash_exports` and `.bash_functions` to `~/.bashrc`
- Symlink `micro/` configs into `~/.config/micro/`

Existing files are backed up with a `.bak` extension before being replaced.

## Shell Commands

| Command | Description |
|---|---|
| `mybash` / `helpfuls` | Open this repo in VS Code |
| `home` | `cd ~/xdev/` |
| `view [path]` | Open file or folder in Windows Explorer |
| `summon [-c\|+c]` | Move/copy latest screenshot from Windows to cwd |
| `winhome` / `desktop` / `whome` | Navigate Windows paths (`-ss` screenshots, `-d` downloads, `-o` desktop, `-r` raw path) |
| `fox [url]` | Open Firefox via PowerShell |
| `hw [course]` | Navigate to homework directory in `~/xdev/school/` |
| `ocr` / `tesseract` | Run Tesseract OCR on an image or PDF |
| `dezone` | Recursively remove `Zone.Identifier` files (Windows NTFS attribute cleanup) |
| `note` / `postit [text]` | Create a sticky note |
| `gamegenie` / `cheats` | Interactive cheat sheet viewer |
| `vim` | Alias for `nvim` |

## Tools

### runes
Python library for ANSI terminal control. Available for import in any script since `~/.dotfiles` is on PYTHONPATH.

```python
from runes.colors import Colors
from runes.cursor import Cursor
```

### gamegenie
Cheat sheet viewer with reference pages for: ANSI codes, Regex, Rust, C#, .NET, Lua, Micro editor.

```bash
gamegenie        # interactive mode
gamegenie RUST   # jump to a specific sheet
```

Sheets live in `gamegenie/cheats/*.md`.

## Micro Editor

Key bindings added on top of defaults:

| Key | Action |
|---|---|
| `Alt-/` or `Ctrl+_` | Toggle comment |

Colorscheme: **dracula**. Additional schemes available: `dracula-tc`, `dark2`, `gotham`, `radical`.
