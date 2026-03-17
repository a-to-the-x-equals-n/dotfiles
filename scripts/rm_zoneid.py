#!/usr/bin/env python3
from pathlib import Path

from runes import RUNE


def delete_zone_identifier_files(directory: str | Path) -> int:
    '''
    Recursively deletes all files ending with 'Zone.Identifier' in the given directory and its subdirectories.

    Parameters:
    -----------
    directory : str | Path
        Path to search (relative or absolute).

    Returns:
    --------
    int
        Number of files successfully deleted.
    '''
    dir = Path(directory).resolve()
    deleted = 0

    print(f'\n{RUNE.FG_BRIGHT_YELLOW}[RESOLVED]{RUNE.RESET}: {RUNE.fg_256(129)}{directory}{RUNE.RESET} to {RUNE.FG_BRIGHT_MAGENTA}{dir}{RUNE.RESET}.')
    print(f'{RUNE.FG_BRIGHT_YELLOW}[SEARCHING]{RUNE.RESET}: {RUNE.fg_256(129)}*Zone.Identifier{RUNE.RESET} in {RUNE.FG_BRIGHT_MAGENTA}{dir}{RUNE.RESET}.')

    for fpath in dir.rglob('*Zone.Identifier'):
        try:
            fpath.unlink()
            print(f'{RUNE.FG_BRIGHT_YELLOW}[DELETED]{RUNE.RESET}: {RUNE.fg_256(129)}{fpath}{RUNE.RESET}')
            deleted += 1
        except PermissionError:
            print(f'{RUNE.FG_BRIGHT_RED}[PERMISSION DENIED]{RUNE.RESET}: {RUNE.fg_256(129)}{fpath}{RUNE.RESET}.')
        except Exception as e:
            print(f'{RUNE.FG_BRIGHT_RED}[ERROR]{RUNE.RESET} {RUNE.fg_256(129)}{fpath}: {RUNE.FG_BRIGHT_YELLOW}{str(e)}{RUNE.RESET}.')

    return deleted


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 2:
        print(f'{RUNE.FG_BRIGHT_YELLOW}[USAGE]{RUNE.RESET}: python rm_identifier.py [directory]')
        sys.exit(1)

    dir = Path(sys.argv[1]) if len(sys.argv) == 2 else Path.cwd()

    if not dir.is_dir():
        print(f"{RUNE.FG_BRIGHT_RED}[ERROR]{RUNE.RESET}: '{RUNE.FG_BRIGHT_MAGENTA}{dir}{RUNE.RESET}' is not a valid directory.")
        sys.exit(1)

    if (ct := delete_zone_identifier_files(dir)) == 0:
        print(f'{RUNE.FG_BRIGHT_GREEN}[SUCCESS]{RUNE.RESET}: No files found with {RUNE.fg_256(129)}*Zone.Identifier{RUNE.RESET}.')
    else:
        print(f'{RUNE.FG_BRIGHT_GREEN}[SUCCESS]{RUNE.RESET}: {RUNE.FG_BRIGHT_MAGENTA}{ct}{RUNE.RESET} files deleted with {RUNE.fg_256(129)}*Zone.Identifier{RUNE.RESET}.')
