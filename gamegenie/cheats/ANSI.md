# ANSI / TERMINAL COMMANDS


## CURSOR MOVEMENT

```py
# move cursor
CURSOR_UP = lambda n=1: f'\033[{n}A'           # move cursor up n lines
CURSOR_DOWN = lambda n=1: f'\033[{n}B'         # move cursor down n lines
CURSOR_FORWARD = lambda n=1: f'\033[{n}C'      # move cursor forward n columns
CURSOR_BACK = lambda n=1: f'\033[{n}D'         # move cursor back n columns

CURSOR_NEXT_LINE = lambda n=1: f'\033[{n}E'    # move to beginning of line n lines down
CURSOR_PREV_LINE = lambda n=1: f'\033[{n}F'    # move to beginning of line n lines up
CURSOR_COLUMN = lambda n=1: f'\033[{n}G'       # move cursor to column n

CURSOR_POS = lambda row=1, col=1: f'\033[{row};{col}H'  # move cursor to position (row, col)
CURSOR_HOME = '\033[H'                          # move cursor to home (0, 0)

# save/restore cursor position
CURSOR_SAVE = '\033[s'
CURSOR_RESTORE = '\033[u'

# cursor visibility
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'
```

## SCREEN CLEARING

```py
CLEAR_SCREEN = '\033c'                          # clear entire screen
CLEAR_SCREEN_FROM_CURSOR = '\033[0J'            # clear from cursor to end of screen
CLEAR_SCREEN_TO_CURSOR = '\033[1J'              # clear from cursor to beginning of screen

CLEAR_LINE = '\033[2K'                          # clear entire line
CLEAR_LINE_FROM_CURSOR = '\033[0K'              # clear from cursor to end of line
CLEAR_LINE_TO_CURSOR = '\033[1K'                # clear from cursor to beginning of line
```

## TEXT FORMATTING / STYLES

```py
# basic styles
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
HIDDEN = '\033[8m'
STRIKETHROUGH = '\033[9m'

# reset specific attributes
RESET_BOLD = '\033[22m'
RESET_DIM = '\033[22m'
RESET_ITALIC = '\033[23m'
RESET_UNDERLINE = '\033[24m'
RESET_BLINK = '\033[25m'
RESET_REVERSE = '\033[27m'
RESET_HIDDEN = '\033[28m'
```

## FOREGROUND COLORS (Standard)

```py
# normal intensity
FG_BLACK = '\033[30m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_YELLOW = '\033[33m'
FG_BLUE = '\033[34m'
FG_MAGENTA = '\033[35m'
FG_CYAN = '\033[36m'
FG_WHITE = '\033[37m'
FG_DEFAULT = '\033[39m'

# bright/bold colors
FG_BRIGHT_BLACK = '\033[90m'    # gray
FG_BRIGHT_RED = '\033[91m'
FG_BRIGHT_GREEN = '\033[92m'
FG_BRIGHT_YELLOW = '\033[93m'
FG_BRIGHT_BLUE = '\033[94m'
FG_BRIGHT_MAGENTA = '\033[95m'
FG_BRIGHT_CYAN = '\033[96m'
FG_BRIGHT_WHITE = '\033[97m'
```

## BACKGROUND COLORS (Standard)

```py
# normal intensity
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'
BG_DEFAULT = '\033[49m'

# bright backgrounds
BG_BRIGHT_BLACK = '\033[100m'
BG_BRIGHT_RED = '\033[101m'
BG_BRIGHT_GREEN = '\033[102m'
BG_BRIGHT_YELLOW = '\033[103m'
BG_BRIGHT_BLUE = '\033[104m'
BG_BRIGHT_MAGENTA = '\033[105m'
BG_BRIGHT_CYAN = '\033[106m'
BG_BRIGHT_WHITE = '\033[107m'
```


## 256-COLOR MODE

```py
def fg_256(n: int) -> str:
    '''Set foreground color using 256-color palette (0-255)'''
    return f'\033[38;5;{n}m'

def bg_256(n: int) -> str:
    '''Set background color using 256-color palette (0-255)'''
    return f'\033[48;5;{n}m'
```

## RGB/TRUE COLOR MODE

```py
def fg_rgb(r: int, g: int, b: int) -> str:
    '''Set foreground color using RGB values (0-255 each)'''
    return f'\033[38;2;{r};{g};{b}m'

def bg_rgb(r: int, g: int, b: int) -> str:
    '''Set background color using RGB values (0-255 each)'''
    return f'\033[48;2;{r};{g};{b}m'
```

## SCROLLING

```py
SCROLL_UP = lambda n=1: f'\033[{n}S'            # scroll up n lines
SCROLL_DOWN = lambda n=1: f'\033[{n}T'          # scroll down n lines
```

## SPECIAL CHARACTERS (ASCII Box Drawing)

```py
# single-line box drawing
BOX_LIGHT_HORIZONTAL = '─'
BOX_LIGHT_VERTICAL = '│'
BOX_LIGHT_DOWN_RIGHT = '┌'
BOX_LIGHT_DOWN_LEFT = '┐'
BOX_LIGHT_UP_RIGHT = '└'
BOX_LIGHT_UP_LEFT = '┘'
BOX_LIGHT_VERTICAL_RIGHT = '├'
BOX_LIGHT_VERTICAL_LEFT = '┤'
BOX_LIGHT_DOWN_HORIZONTAL = '┬'
BOX_LIGHT_UP_HORIZONTAL = '┴'
BOX_LIGHT_VERTICAL_HORIZONTAL = '┼'

# double-line box drawing
BOX_HEAVY_HORIZONTAL = '═'
BOX_HEAVY_VERTICAL = '║'
BOX_HEAVY_DOWN_RIGHT = '╔'
BOX_HEAVY_DOWN_LEFT = '╗'
BOX_HEAVY_UP_RIGHT = '╚'
BOX_HEAVY_UP_LEFT = '╝'

# symbols
CHECKMARK = '✓'
CROSS = '✗'
BULLET = '•'
ARROW_RIGHT = '→'
ARROW_LEFT = '←'
ARROW_UP = '↑'
ARROW_DOWN = '↓'
```

## UTILITY FUNCTIONS

```py
def clear_screen():
    '''Clear the entire screen and move cursor to home'''
    print(CLEAR_SCREEN + CURSOR_HOME, end='')

def clear_line():
    '''Clear the current line'''
    print(CLEAR_LINE, end='')

def move_cursor(row: int, col: int):
    '''Move cursor to specific position'''
    print(CURSOR_POS(row, col), end='')

def hide_cursor():
    '''Hide the cursor'''
    print(CURSOR_HIDE, end='')

def show_cursor():
    '''Show the cursor'''
    print(CURSOR_SHOW, end='')

def colorize(text: str, fg: str = '', bg: str = '', style: str = '') -> str:
    '''
    Colorize text with foreground, background, and style.

    Args:
        text: Text to colorize
        fg: Foreground color code (e.g., FG_RED)
        bg: Background color code (e.g., BG_BLUE)
        style: Style code (e.g., BOLD)

    Returns:
        Formatted string with ANSI codes
    '''
    return f'{style}{fg}{bg}{text}{RESET}'
```

