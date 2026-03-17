#!/usr/bin/env python3
import sys
import re
import shutil
from pathlib import Path

from runes import RUNE


def terminal_width() -> int:
    '''
    Returns the current terminal column width.

    Returns:
    --------
    int
        Number of columns in the terminal.
    '''
    return shutil.get_terminal_size().columns


def visible_len(text: str) -> int:
    '''
    Returns the visible length of text after stripping ANSI escape codes.

    Parameters:
    -----------
    text : str
        String potentially containing ANSI escape sequences.

    Returns:
    --------
    int
        Length of the string with escape codes removed.
    '''
    return len(re.sub(r'\033\[[0-9;]*m', '', text))


def strip_inline_md(text: str) -> str:
    '''
    Strips inline markdown syntax, returning plain visible text.

    Parameters:
    -----------
    text : str
        String containing inline markdown (links, bold, italic, code).

    Returns:
    --------
    str
        Plain text with markdown syntax removed.
    '''
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)   # links
    text = re.sub(r'`([^`]+)`', r'\1', text)               # inline code
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)           # bold (**)
    text = re.sub(r'__(.+?)__', r'\1', text)               # bold (__)
    text = re.sub(r'\*(.+?)\*', r'\1', text)               # italic (*)
    text = re.sub(r'_([^_]+)_', r'\1', text)               # italic (_)
    return text


def render_inline(text: str) -> str:
    '''
    Applies ANSI formatting for inline markdown elements.

    Parameters:
    -----------
    text : str
        String containing inline markdown (links, bold, italic, code).

    Returns:
    --------
    str
        String with ANSI escape codes applied.
    '''
    # links: show text, dim the URL hint
    text = re.sub(r'\[([^\]]+)\]\(([^)]*)\)', lambda m: m.group(1), text)
    # inline code
    text = re.sub(r'`([^`]+)`', lambda m: f'{RUNE.FG_BRIGHT_GREEN}{m.group(1)}{RUNE.RESET}', text)
    # bold
    text = re.sub(r'\*\*(.+?)\*\*', lambda m: f'{RUNE.BOLD}{RUNE.FG_BRIGHT_WHITE}{m.group(1)}{RUNE.RESET}', text)
    text = re.sub(r'__(.+?)__', lambda m: f'{RUNE.BOLD}{RUNE.FG_BRIGHT_WHITE}{m.group(1)}{RUNE.RESET}', text)
    # italic
    text = re.sub(r'\*(.+?)\*', lambda m: f'{RUNE.DIM}{m.group(1)}{RUNE.RESET}', text)
    text = re.sub(r'_([^_]+)_', lambda m: f'{RUNE.DIM}{m.group(1)}{RUNE.RESET}', text)
    return text


def render_heading(level: int, text: str) -> str:
    '''
    Renders a markdown heading with ANSI styling.

    Parameters:
    -----------
    level : int
        Heading level (1-4).

    text : str
        Heading content.

    Returns:
    --------
    str
        ANSI-formatted heading string.
    '''
    width = terminal_width()
    text = text.strip()
    if level == 1:
        bar = '━' * width
        return f'\n{RUNE.BOLD}{RUNE.FG_BRIGHT_YELLOW}{bar}\n {text}\n{bar}{RUNE.RESET}\n'
    elif level == 2:
        underline = '─' * len(text)
        return f'\n{RUNE.BOLD}{RUNE.FG_BRIGHT_CYAN}{text}\n{RUNE.FG_CYAN}{underline}{RUNE.RESET}\n'
    elif level == 3:
        return f'\n{RUNE.BOLD}{RUNE.FG_CYAN}{text}{RUNE.RESET}\n'
    else:
        return f'\n{RUNE.BOLD}{text}{RUNE.RESET}\n'


def render_table(table_lines: list[str]) -> str:
    '''
    Renders a markdown table with aligned columns and ANSI styling.

    Parameters:
    -----------
    table_lines : list[str]
        Raw markdown table lines including header and separator rows.

    Returns:
    --------
    str
        ANSI-formatted table string.
    '''
    rows = []
    for line in table_lines:
        stripped = line.strip().strip('|')
        cells = [c.strip() for c in stripped.split('|')]
        rows.append(cells)

    # find separator row
    sep_idx = None
    for i, row in enumerate(rows):
        if all(re.match(r'^:?-+:?$', c) for c in row if c):
            sep_idx = i
            break

    if sep_idx is None:
        # no header separator — just render plainly
        out = []
        for row in rows:
            out.append('  ' + f'  {RUNE.DIM}│{RUNE.RESET}  '.join(render_inline(c) for c in row))
        return '\n'.join(out)

    header_rows = rows[:sep_idx]
    data_rows   = rows[sep_idx + 1:]
    all_rows    = header_rows + data_rows

    num_cols = max(len(r) for r in all_rows)

    # measure column widths using visible plain text
    col_widths = [0] * num_cols
    for row in all_rows:
        for i, cell in enumerate(row):
            if i < num_cols:
                col_widths[i] = max(col_widths[i], len(strip_inline_md(cell)))

    def fmt_row(row: list[str], bold: bool = False) -> str:
        '''
        Formats a single table row with padding and optional bold styling.

        Parameters:
        -----------
        row : list[str]
            Cell values for the row.

        bold : bool
            Whether to apply bold ANSI styling to cells.

        Returns:
        --------
        str
            Formatted row string with aligned, styled cells.
        '''
        cells = []
        for i in range(num_cols):
            cell = row[i] if i < len(row) else ''
            plain_len = len(strip_inline_md(cell))
            pad = ' ' * (col_widths[i] - plain_len)
            rendered = render_inline(cell)
            if bold:
                cells.append(f'{RUNE.BOLD}{RUNE.FG_BRIGHT_WHITE}{rendered}{RUNE.RESET}{pad}')
            else:
                cells.append(rendered + pad)
        sep = f'  {RUNE.DIM}│{RUNE.RESET}  '
        return '  ' + sep.join(cells)

    sep_line = '  ' + f'──{RUNE.DIM}┼{RUNE.RESET}──'.join('─' * w for w in col_widths)

    out = []
    for row in header_rows:
        out.append(fmt_row(row, bold=True))
    out.append(sep_line)
    for row in data_rows:
        out.append(fmt_row(row))
    return '\n'.join(out)


def _is_table_sep(line: str) -> bool:
    '''
    Returns True if the line is a markdown table separator row.

    Parameters:
    -----------
    line : str
        A single line of text to inspect.

    Returns:
    --------
    bool
        True if the line matches the pattern of a table separator.
    '''
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    return bool(cells) and all(re.match(r'^:?-+:?$', c) for c in cells if c)


def render_markdown(content: str) -> str:
    '''
    Renders a full markdown string to an ANSI-formatted terminal string.

    Parameters:
    -----------
    content : str
        Raw markdown content.

    Returns:
    --------
    str
        ANSI-formatted string ready for terminal output.
    '''
    lines = content.splitlines()
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # fenced code block
        if re.match(r'^```', line.strip()):
            lang = line.strip()[3:].strip()
            i += 1
            code_lines = []
            while i < len(lines) and not re.match(r'^```', lines[i].strip()):
                code_lines.append(lines[i])
                i += 1
            i += 1  # consume closing ```

            if lang:
                out.append(f'  {RUNE.FG_BRIGHT_BLACK}{lang}{RUNE.RESET}')
            for cl in code_lines:
                out.append(f'  {RUNE.FG_GREEN}{cl}{RUNE.RESET}')
            out.append('')
            continue

        # table: current line has | and next line is a separator row
        if '|' in line and i + 1 < len(lines) and _is_table_sep(lines[i + 1]):
            table_lines = [line]
            i += 1
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            out.append(render_table(table_lines))
            out.append('')
            continue

        # headings
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            out.append(render_heading(len(m.group(1)), m.group(2)))
            i += 1
            continue

        # horizontal rule
        if re.match(r'^[-*_]{3,}\s*$', line.strip()) and line.strip():
            out.append(f'{RUNE.DIM}{"─" * terminal_width()}{RUNE.RESET}')
            i += 1
            continue

        # unordered list item
        m = re.match(r'^(\s*)[*\-+]\s+(.*)', line)
        if m:
            depth = len(m.group(1)) // 2
            bullet = '  ' * depth + f'{RUNE.FG_BRIGHT_CYAN}•{RUNE.RESET} '
            out.append(bullet + render_inline(m.group(2)))
            i += 1
            continue

        # ordered list item
        m = re.match(r'^(\s*)(\d+)\.\s+(.*)', line)
        if m:
            depth = len(m.group(1)) // 2
            prefix = '  ' * depth + f'{RUNE.FG_BRIGHT_CYAN}{m.group(2)}.{RUNE.RESET} '
            out.append(prefix + render_inline(m.group(3)))
            i += 1
            continue

        # blank line
        if not line.strip():
            out.append('')
            i += 1
            continue

        # regular text
        out.append(render_inline(line))
        i += 1

    return '\n'.join(out)


def find_markdown_file(search_name: str, cheats_dir: str | Path) -> Path | None:
    '''
    Finds a markdown file in the cheats directory by name (case-insensitive).

    Parameters:
    -----------
    search_name : str
        The cheat name to look up (without extension).

    cheats_dir : str | Path
        Directory to search for .md files.

    Returns:
    --------
    Path | None
        Path to the matched .md file, or None if not found.
    '''
    search_lower = search_name.lower()
    for md_file in Path(cheats_dir).glob('*.md'):
        if md_file.stem.lower() == search_lower:
            return md_file
    return None


def main() -> None:
    '''
    Entry point — parses the argument and renders the requested markdown cheat sheet.
    '''
    script_dir = Path(__file__).parent
    cheats_dir = script_dir / 'cheats'

    if len(sys.argv) < 2:
        print(f'{RUNE.BOLD}{RUNE.FG_BRIGHT_CYAN}Usage:{RUNE.RESET} gamegenie <cheat_name|file_path>')
        print(f'\nAvailable cheats in {cheats_dir}:')
        if cheats_dir.exists():
            for md_file in sorted(cheats_dir.glob('*.md')):
                print(f'  {RUNE.FG_BRIGHT_CYAN}•{RUNE.RESET} {md_file.stem}')
        sys.exit(1)

    arg = sys.argv[1]
    arg_path = Path(arg).expanduser()

    if '/' in arg or arg_path.exists():
        if not arg_path.exists():
            print(f'{RUNE.BOLD}Error:{RUNE.RESET} File not found: {arg}')
            sys.exit(1)
        if not arg_path.is_file():
            print(f'{RUNE.BOLD}Error:{RUNE.RESET} Not a file: {arg}')
            sys.exit(1)
        md_file = arg_path
    else:
        md_file = find_markdown_file(arg, cheats_dir)
        if md_file is None:
            print(f'{RUNE.BOLD}Error:{RUNE.RESET} Cheat \'{arg}\' not found')
            print(f'\nAvailable cheats in {cheats_dir}:')
            if cheats_dir.exists():
                for md in sorted(cheats_dir.glob('*.md')):
                    print(f'  {RUNE.FG_BRIGHT_CYAN}•{RUNE.RESET} {md.stem}')
            sys.exit(1)

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(render_markdown(content))


if __name__ == '__main__':
    main()
