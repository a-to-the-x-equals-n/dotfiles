#!/usr/bin/env python3
import sys
from pathlib import Path
import subprocess
import time

from runes import RUNE


DIR = Path.home() / 'xdev' / 'school'
COURSES = [f.name for f in DIR.iterdir()]
ARGS = ['-vs'] + COURSES
USAGE = f'  {RUNE.fg_256(129)}[USAGE]{RUNE.RESET}: hw <school folder> -vs (optional flag)'

# Ƹ̵̡Ӝ̵̨̄Ʒ
THUMBS_UP = '''\n\n\t\t\t("'`\( 一_一)/`'")\n'''

def eprint(*args, **kwargs) -> None:
    '''
    Prints to stderr.
    '''
    print(*args, file = sys.stderr, **kwargs)

def resolve(course: str | None, dir: Path = DIR) -> Path:
    '''
    Resolves the full path to a homework directory if it exists.

    Parameters:
    -----------
    course : str | None
        The name of the class.

    dir : Path
        The DIR directory: ~/xdev/school.

    Returns:
    --------
    Path
        Resolved path.
    '''
    if course not in [f.name for f in DIR.iterdir() if f.is_dir()]:
        eprint(f'  {RUNE.FG_BRIGHT_RED}[ERROR]{RUNE.RESET}: \'{course}\' not valid dir.')
        time.sleep(.5)
        eprint(f'  {RUNE.FG_BRIGHT_YELLOW}[REDIRECTING]{RUNE.RESET}', end = '', flush = True)

        for i in range(0, 4):
            sys.stdout.write(f'.' * i)
            sys.stdout.flush()
            time.sleep(.4)
            # erase
            sys.stdout.write('\b' * i)
        eprint()
        return dir

    if (DIR / course).is_dir():
        return dir / course

def code(path: Path) -> None:
    '''
    Launches VS Code with the given path.

    Parameters:
    -----------
    path : Path
        Directory to open.
    '''
    subprocess.run(['code', str(path)], check = False)

def validate(args: list) -> tuple[str | None, bool]:
    '''
    Parses and validates command-line arguments.

    Parameters:
    -----------
    args : list
        Command-line argument list (sys.argv).

    Returns:
    --------
    tuple[str | None, bool]
        Course name (or None) and whether to open VS Code.
    '''
    course = None
    vs = False

    if not (1 <= len(args) <= 3):
        eprint(f'  {RUNE.FG_BRIGHT_RED}[ERROR]{RUNE.RESET}: invalid input.')
        eprint(USAGE)
        time.sleep(.4)
        eprint(f'{RUNE.FG_BRIGHT_RED}[EXITING]{RUNE.RESET}')
        time.sleep(.3)
        sys.exit(1)

    for arg in args[1:]:
        if arg not in ARGS:
            eprint(f'  {RUNE.FG_BRIGHT_RED}[ERROR]{RUNE.RESET}: \'{arg}\' is not a valid arg.')
            time.sleep(.4)
            eprint(USAGE)
            time.sleep(.4)
            eprint(f'{RUNE.FG_BRIGHT_RED}[EXITING]{RUNE.RESET}')
            time.sleep(.3)
            sys.exit(1)

        if arg == '-vs':
            vs = True
        if arg in COURSES:
            course = arg

    return course, vs


if __name__ == '__main__':
    eprint(RUNE.CLEAR_SCREEN)
    eprint(f'\n\t\t{RUNE.FG_BRIGHT_RED}(╹_╹)凸{RUNE.RESET}\n\t     {RUNE.fg_256(129)}[good morning]{RUNE.RESET}\n')
    time.sleep(.4)

    # parse args
    course, vs = validate(sys.argv)
    target = resolve(course) if course else DIR

    if vs:
        code(target)
    else:
        print(str(target))

    # time.sleep(.2)
    # eprint(f'{GR}{THUMBS_UP}{_X}', end = '')
    # time.sleep(.2)
    # eprint('  \t' + '=' * 54)
    # eprint(f'\t\t{MG}    Welcome... to the real world{_X}')
    # eprint('  \t' + '=' * 54)
    # time.sleep(.2)
