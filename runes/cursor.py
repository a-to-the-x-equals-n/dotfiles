#!/usr/bin/env python3
'''
Complete ANSI/ASCII terminal manipulation codes for reference and import.
'''

from dataclasses import dataclass


@dataclass(frozen = True)
class RUNE:
    '''
    Frozen dataclass containing all ANSI/ASCII terminal codes.
    '''

    # ========================================================================
    # CURSOR MOVEMENT
    # ========================================================================

    # move cursor - lambdas as static methods
    CURSOR_UP = staticmethod(lambda n = 1: f'\033[{n}A')
    CURSOR_DOWN = staticmethod(lambda n = 1: f'\033[{n}B')
    CURSOR_FORWARD = staticmethod(lambda n = 1: f'\033[{n}C')
    CURSOR_BACK = staticmethod(lambda n = 1: f'\033[{n}D')

    CURSOR_NEXT_LINE = staticmethod(lambda n = 1: f'\033[{n}E')
    CURSOR_PREV_LINE = staticmethod(lambda n = 1: f'\033[{n}F')
    CURSOR_COLUMN = staticmethod(lambda n = 1: f'\033[{n}G')

    CURSOR_POS = staticmethod(lambda row = 1, col = 1: f'\033[{row};{col}H')
    CURSOR_HOME = '\033[H'

    # save/restore cursor position
    CURSOR_SAVE = '\033[s'
    CURSOR_RESTORE = '\033[u'

    # cursor visibility
    CURSOR_HIDE = '\033[?25l'
    CURSOR_SHOW = '\033[?25h'

    # ========================================================================
    # SCROLLING
    # ========================================================================

    SCROLL_UP = staticmethod(lambda n = 1: f'\033[{n}S')
    SCROLL_DOWN = staticmethod(lambda n = 1: f'\033[{n}T')
    
    # ========================================================================
    # SCREEN CLEARING
    # ========================================================================

    CLEAR_SCREEN = '\033c'
    CLEAR_SCREEN_FROM_CURSOR = '\033[0J'
    CLEAR_SCREEN_TO_CURSOR = '\033[1J'

    CLEAR_LINE = '\033[2K'
    CLEAR_LINE_FROM_CURSOR = '\033[0K'
    CLEAR_LINE_TO_CURSOR = '\033[1K'

    # ========================================================================
    # TEXT FORMATTING / STYLES
    # ========================================================================

    # styles
    X = RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'

    # reset styling
    RESET_BOLD = '\033[22m'
    RESET_DIM = '\033[22m'
    RESET_ITALIC = '\033[23m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'

    # ========================================================================
    # FOREGROUND COLORS (Standard)
    # ========================================================================

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

    # bright / bold colors
    FG_BRIGHT_BLACK = '\033[90m'
    FG_BRIGHT_RED = '\033[91m'
    FG_BRIGHT_GREEN = '\033[92m'
    FG_BRIGHT_YELLOW = '\033[93m'
    FG_BRIGHT_BLUE = '\033[94m'
    FG_BRIGHT_MAGENTA = '\033[95m'
    FG_BRIGHT_CYAN = '\033[96m'
    FG_BRIGHT_WHITE = '\033[97m'

    # ========================================================================
    # TRUE RGB COLORS
    # ========================================================================

    # primary colors
    TRUE_RED = '\033[38;2;255;0;0m'
    TRUE_GREEN = '\033[38;2;0;255;0m'
    TRUE_BLUE = '\033[38;2;0;0;255m'

    # secondary colors
    TRUE_YELLOW = '\033[38;2;255;255;0m'
    TRUE_CYAN = '\033[38;2;0;255;255m'
    TRUE_MAGENTA = '\033[38;2;255;0;255m'

    # grayscale
    TRUE_BLACK = '\033[38;2;0;0;0m'
    TRUE_WHITE = '\033[38;2;255;255;255m'
    TRUE_GRAY = '\033[38;2;128;128;128m'

    # additional common colors
    TRUE_ORANGE = '\033[38;2;255;165;0m'
    TRUE_PURPLE = '\033[38;2;160;32;240m'
    TRUE_PINK = '\033[38;2;255;20;147m'
    TRUE_BROWN = '\033[38;2;139;69;19m'
    TRUE_LIME = '\033[38;2;0;255;0m'
    TRUE_NAVY = '\033[38;2;0;0;128m'
    TRUE_TEAL = '\033[38;2;0;128;128m'
    TRUE_MAROON = '\033[38;2;128;0;0m'
    TRUE_OLIVE = '\033[38;2;128;128;0m'
    TRUE_SILVER = '\033[38;2;192;192;192m'
    TRUE_GOLD = '\033[38;2;255;215;0m'
    TRUE_INDIGO = '\033[38;2;75;0;130m'
    TRUE_VIOLET = '\033[38;2;238;130;238m'
    TRUE_CORAL = '\033[38;2;255;127;80m'
    TRUE_TURQUOISE = '\033[38;2;64;224;208m'

    # ========================================================================
    # SPECIAL CHARACTERS (ASCII Box Drawing)
    # ========================================================================

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
    
    # ========================================================================
    # BACKGROUND COLORS (Standard)
    # ========================================================================

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


    # ========================================================================
    # 256-COLOR MODE
    # ========================================================================

    @staticmethod
    def fg_256(n: int, /) -> str:
        '''
        Set foreground color using 256-color palette.

        Parameters:
        -----------
        n : int
            Color index (0-255).

        Returns:
        --------
        str
            ANSI escape sequence for the foreground color.
        '''
        return f'\033[38;5;{n}m'

    @staticmethod
    def bg_256(n: int, /) -> str:
        '''
        Set background color using 256-color palette.

        Parameters:
        -----------
        n : int
            Color index (0-255).

        Returns:
        --------
        str
            ANSI escape sequence for the background color.
        '''
        return f'\033[48;5;{n}m'


    # ========================================================================
    # RGB/TRUE COLOR MODE
    # ========================================================================

    @staticmethod
    def fg_rgb(*, r: int, g: int, b: int) -> str:
        '''
        Set foreground color using RGB values.

        Parameters:
        -----------
        r : int
            Red channel (0-255).

        g : int
            Green channel (0-255).

        b : int
            Blue channel (0-255).

        Returns:
        --------
        str
            ANSI escape sequence for the RGB foreground color.
        '''
        return f'\033[38;2;{r};{g};{b}m'

    @staticmethod
    def bg_rgb(*, r: int, g: int, b: int) -> str:
        '''
        Set background color using RGB values.

        Parameters:
        -----------
        r : int
            Red channel (0-255).

        g : int
            Green channel (0-255).

        b : int
            Blue channel (0-255).

        Returns:
        --------
        str
            ANSI escape sequence for the RGB background color.
        '''
        return f'\033[48;2;{r};{g};{b}m'


    # ========================================================================
    # UTILITY FUNCTIONS
    # ========================================================================

    @staticmethod
    def clear_screen() -> None:
        '''
        Clears the entire screen and moves the cursor to home position.
        '''
        print(RUNE.CLEAR_SCREEN + RUNE.CURSOR_HOME, end = '')
    
    @staticmethod
    def clear_line() -> None:
        '''
        Clears the current line.
        '''
        print(RUNE.CLEAR_LINE, end = '')

    @staticmethod
    def move_cursor(*, row: int, col: int) -> None:
        '''
        Moves the cursor to a specific row and column position.

        Parameters:
        -----------
        row : int
            Row position (1-based).

        col : int
            Column position (1-based).
        '''
        print(RUNE.CURSOR_POS()(row, col), end = '')

    @staticmethod
    def hide_cursor() -> None:
        '''
        Hides the cursor.
        '''
        print(RUNE.CURSOR_HIDE, end = '')

    @staticmethod
    def show_cursor() -> None:
        '''
        Shows the cursor.
        '''
        print(RUNE.CURSOR_SHOW, end = '')

    @staticmethod
    def colorize(text: str, /, *, fg: str = '', bg: str = '', style: str = '') -> str:
        '''
        Colorize text with foreground, background, and style.

        Parameters:
        -----------
        text : str
            Text to colorize.

        fg : str
            Foreground color code (e.g., RUNE.FG_RED).

        bg : str
            Background color code (e.g., RUNE.BG_BLUE).

        style : str
            Style code (e.g., RUNE.BOLD).

        Returns:
        --------
        str
            Formatted string with ANSI codes.
        '''
        return f'{style}{fg}{bg}{text}{RUNE.RESET}'

    @staticmethod
    def enchant(text: str, /, *, fg: str = '', bg: str = '', style: str = '') -> str:
        '''
        Alias for colorize - enchant text with foreground, background, and style.

        Parameters:
        -----------
        text : str
            Text to enchant.

        fg : str
            Foreground color code (e.g., RUNE.FG_RED).

        bg : str
            Background color code (e.g., RUNE.BG_BLUE).

        style : str
            Style code (e.g., RUNE.BOLD).

        Returns:
        --------
        str
            Formatted string with ANSI codes.
        '''
        return RUNE.colorize(text, fg = fg, bg = bg, style = style)


# ============================================================================
# BACKWARD COMPATIBILITY - Module-level aliases
# ============================================================================

CURSOR_UP = RUNE.CURSOR_UP
CURSOR_DOWN = RUNE.CURSOR_DOWN
CURSOR_FORWARD = RUNE.CURSOR_FORWARD
CURSOR_BACK = RUNE.CURSOR_BACK
CURSOR_NEXT_LINE = RUNE.CURSOR_NEXT_LINE
CURSOR_PREV_LINE = RUNE.CURSOR_PREV_LINE
CURSOR_COLUMN = RUNE.CURSOR_COLUMN
CURSOR_POS = RUNE.CURSOR_POS
CURSOR_HOME = RUNE.CURSOR_HOME
CURSOR_SAVE = RUNE.CURSOR_SAVE
CURSOR_RESTORE = RUNE.CURSOR_RESTORE
CURSOR_HIDE = RUNE.CURSOR_HIDE
CURSOR_SHOW = RUNE.CURSOR_SHOW

CLEAR_SCREEN = RUNE.CLEAR_SCREEN
CLEAR_SCREEN_FROM_CURSOR = RUNE.CLEAR_SCREEN_FROM_CURSOR
CLEAR_SCREEN_TO_CURSOR = RUNE.CLEAR_SCREEN_TO_CURSOR
CLEAR_LINE = RUNE.CLEAR_LINE
CLEAR_LINE_FROM_CURSOR = RUNE.CLEAR_LINE_FROM_CURSOR
CLEAR_LINE_TO_CURSOR = RUNE.CLEAR_LINE_TO_CURSOR

X = RESET = RUNE.RESET
BOLD = RUNE.BOLD
DIM = RUNE.DIM
ITALIC = RUNE.ITALIC
UNDERLINE = RUNE.UNDERLINE
BLINK = RUNE.BLINK
REVERSE = RUNE.REVERSE
HIDDEN = RUNE.HIDDEN
STRIKETHROUGH = RUNE.STRIKETHROUGH
RESET_BOLD = RUNE.RESET_BOLD
RESET_DIM = RUNE.RESET_DIM
RESET_ITALIC = RUNE.RESET_ITALIC
RESET_UNDERLINE = RUNE.RESET_UNDERLINE
RESET_BLINK = RUNE.RESET_BLINK
RESET_REVERSE = RUNE.RESET_REVERSE
RESET_HIDDEN = RUNE.RESET_HIDDEN

FG_BLACK = RUNE.FG_BLACK
FG_RED = RUNE.FG_RED
FG_GREEN = RUNE.FG_GREEN
FG_YELLOW = RUNE.FG_YELLOW
FG_BLUE = RUNE.FG_BLUE
FG_MAGENTA = RUNE.FG_MAGENTA
FG_CYAN = RUNE.FG_CYAN
FG_WHITE = RUNE.FG_WHITE
FG_DEFAULT = RUNE.FG_DEFAULT
FG_BRIGHT_BLACK = RUNE.FG_BRIGHT_BLACK
FG_BRIGHT_RED = RUNE.FG_BRIGHT_RED
FG_BRIGHT_GREEN = RUNE.FG_BRIGHT_GREEN
FG_BRIGHT_YELLOW = RUNE.FG_BRIGHT_YELLOW
FG_BRIGHT_BLUE = RUNE.FG_BRIGHT_BLUE
FG_BRIGHT_MAGENTA = RUNE.FG_BRIGHT_MAGENTA
FG_BRIGHT_CYAN = RUNE.FG_BRIGHT_CYAN
FG_BRIGHT_WHITE = RUNE.FG_BRIGHT_WHITE

TRUE_RED = RUNE.TRUE_RED
TRUE_GREEN = RUNE.TRUE_GREEN
TRUE_BLUE = RUNE.TRUE_BLUE
TRUE_YELLOW = RUNE.TRUE_YELLOW
TRUE_CYAN = RUNE.TRUE_CYAN
TRUE_MAGENTA = RUNE.TRUE_MAGENTA
TRUE_BLACK = RUNE.TRUE_BLACK
TRUE_WHITE = RUNE.TRUE_WHITE
TRUE_GRAY = RUNE.TRUE_GRAY
TRUE_ORANGE = RUNE.TRUE_ORANGE
TRUE_PURPLE = RUNE.TRUE_PURPLE
TRUE_PINK = RUNE.TRUE_PINK
TRUE_BROWN = RUNE.TRUE_BROWN
TRUE_LIME = RUNE.TRUE_LIME
TRUE_NAVY = RUNE.TRUE_NAVY
TRUE_TEAL = RUNE.TRUE_TEAL
TRUE_MAROON = RUNE.TRUE_MAROON
TRUE_OLIVE = RUNE.TRUE_OLIVE
TRUE_SILVER = RUNE.TRUE_SILVER
TRUE_GOLD = RUNE.TRUE_GOLD
TRUE_INDIGO = RUNE.TRUE_INDIGO
TRUE_VIOLET = RUNE.TRUE_VIOLET
TRUE_CORAL = RUNE.TRUE_CORAL
TRUE_TURQUOISE = RUNE.TRUE_TURQUOISE

BG_BLACK = RUNE.BG_BLACK
BG_RED = RUNE.BG_RED
BG_GREEN = RUNE.BG_GREEN
BG_YELLOW = RUNE.BG_YELLOW
BG_BLUE = RUNE.BG_BLUE
BG_MAGENTA = RUNE.BG_MAGENTA
BG_CYAN = RUNE.BG_CYAN
BG_WHITE = RUNE.BG_WHITE
BG_DEFAULT = RUNE.BG_DEFAULT
BG_BRIGHT_BLACK = RUNE.BG_BRIGHT_BLACK
BG_BRIGHT_RED = RUNE.BG_BRIGHT_RED
BG_BRIGHT_GREEN = RUNE.BG_BRIGHT_GREEN
BG_BRIGHT_YELLOW = RUNE.BG_BRIGHT_YELLOW
BG_BRIGHT_BLUE = RUNE.BG_BRIGHT_BLUE
BG_BRIGHT_MAGENTA = RUNE.BG_BRIGHT_MAGENTA
BG_BRIGHT_CYAN = RUNE.BG_BRIGHT_CYAN
BG_BRIGHT_WHITE = RUNE.BG_BRIGHT_WHITE

fg_256 = RUNE.fg_256
bg_256 = RUNE.bg_256
fg_rgb = RUNE.fg_rgb
bg_rgb = RUNE.bg_rgb

SCROLL_UP = RUNE.SCROLL_UP
SCROLL_DOWN = RUNE.SCROLL_DOWN

BOX_LIGHT_HORIZONTAL = RUNE.BOX_LIGHT_HORIZONTAL
BOX_LIGHT_VERTICAL = RUNE.BOX_LIGHT_VERTICAL
BOX_LIGHT_DOWN_RIGHT = RUNE.BOX_LIGHT_DOWN_RIGHT
BOX_LIGHT_DOWN_LEFT = RUNE.BOX_LIGHT_DOWN_LEFT
BOX_LIGHT_UP_RIGHT = RUNE.BOX_LIGHT_UP_RIGHT
BOX_LIGHT_UP_LEFT = RUNE.BOX_LIGHT_UP_LEFT
BOX_LIGHT_VERTICAL_RIGHT = RUNE.BOX_LIGHT_VERTICAL_RIGHT
BOX_LIGHT_VERTICAL_LEFT = RUNE.BOX_LIGHT_VERTICAL_LEFT
BOX_LIGHT_DOWN_HORIZONTAL = RUNE.BOX_LIGHT_DOWN_HORIZONTAL
BOX_LIGHT_UP_HORIZONTAL = RUNE.BOX_LIGHT_UP_HORIZONTAL
BOX_LIGHT_VERTICAL_HORIZONTAL = RUNE.BOX_LIGHT_VERTICAL_HORIZONTAL
BOX_HEAVY_HORIZONTAL = RUNE.BOX_HEAVY_HORIZONTAL
BOX_HEAVY_VERTICAL = RUNE.BOX_HEAVY_VERTICAL
BOX_HEAVY_DOWN_RIGHT = RUNE.BOX_HEAVY_DOWN_RIGHT
BOX_HEAVY_DOWN_LEFT = RUNE.BOX_HEAVY_DOWN_LEFT
BOX_HEAVY_UP_RIGHT = RUNE.BOX_HEAVY_UP_RIGHT
BOX_HEAVY_UP_LEFT = RUNE.BOX_HEAVY_UP_LEFT

CHECKMARK = RUNE.CHECKMARK
CROSS = RUNE.CROSS
BULLET = RUNE.BULLET
ARROW_RIGHT = RUNE.ARROW_RIGHT
ARROW_LEFT = RUNE.ARROW_LEFT
ARROW_UP = RUNE.ARROW_UP
ARROW_DOWN = RUNE.ARROW_DOWN

clear_screen = RUNE.clear_screen
clear_line = RUNE.clear_line
move_cursor = RUNE.move_cursor
hide_cursor = RUNE.hide_cursor
show_cursor = RUNE.show_cursor
colorize = RUNE.colorize
enchant = RUNE.enchant


# ============================================================================
# EXPORTS
# ============================================================================

__all__ = [
    'RUNE',

    # Cursor movement
    'CURSOR_UP', 'CURSOR_DOWN', 'CURSOR_FORWARD', 'CURSOR_BACK',
    'CURSOR_NEXT_LINE', 'CURSOR_PREV_LINE', 'CURSOR_COLUMN',
    'CURSOR_POS', 'CURSOR_HOME',
    'CURSOR_SAVE', 'CURSOR_RESTORE',
    'CURSOR_HIDE', 'CURSOR_SHOW',

    # Screen clearing
    'CLEAR_SCREEN', 'CLEAR_SCREEN_FROM_CURSOR', 'CLEAR_SCREEN_TO_CURSOR',
    'CLEAR_LINE', 'CLEAR_LINE_FROM_CURSOR', 'CLEAR_LINE_TO_CURSOR',

    # Text formatting
    'RESET', 'X', 'BOLD', 'DIM', 'ITALIC', 'UNDERLINE', 'BLINK', 'REVERSE',
    'HIDDEN', 'STRIKETHROUGH',
    'RESET_BOLD', 'RESET_DIM', 'RESET_ITALIC', 'RESET_UNDERLINE',
    'RESET_BLINK', 'RESET_REVERSE', 'RESET_HIDDEN',

    # Foreground colors
    'FG_BLACK', 'FG_RED', 'FG_GREEN', 'FG_YELLOW', 'FG_BLUE',
    'FG_MAGENTA', 'FG_CYAN', 'FG_WHITE', 'FG_DEFAULT',
    'FG_BRIGHT_BLACK', 'FG_BRIGHT_RED', 'FG_BRIGHT_GREEN',
    'FG_BRIGHT_YELLOW', 'FG_BRIGHT_BLUE', 'FG_BRIGHT_MAGENTA',
    'FG_BRIGHT_CYAN', 'FG_BRIGHT_WHITE',

    # True RGB colors
    'TRUE_RED', 'TRUE_GREEN', 'TRUE_BLUE',
    'TRUE_YELLOW', 'TRUE_CYAN', 'TRUE_MAGENTA',
    'TRUE_BLACK', 'TRUE_WHITE', 'TRUE_GRAY',
    'TRUE_ORANGE', 'TRUE_PURPLE', 'TRUE_PINK', 'TRUE_BROWN',
    'TRUE_LIME', 'TRUE_NAVY', 'TRUE_TEAL', 'TRUE_MAROON',
    'TRUE_OLIVE', 'TRUE_SILVER', 'TRUE_GOLD', 'TRUE_INDIGO',
    'TRUE_VIOLET', 'TRUE_CORAL', 'TRUE_TURQUOISE',

    # Background colors
    'BG_BLACK', 'BG_RED', 'BG_GREEN', 'BG_YELLOW', 'BG_BLUE',
    'BG_MAGENTA', 'BG_CYAN', 'BG_WHITE', 'BG_DEFAULT',
    'BG_BRIGHT_BLACK', 'BG_BRIGHT_RED', 'BG_BRIGHT_GREEN',
    'BG_BRIGHT_YELLOW', 'BG_BRIGHT_BLUE', 'BG_BRIGHT_MAGENTA',
    'BG_BRIGHT_CYAN', 'BG_BRIGHT_WHITE',

    # Color functions
    'fg_256', 'bg_256', 'fg_rgb', 'bg_rgb',

    # Scrolling
    'SCROLL_UP', 'SCROLL_DOWN',

    # Box drawing
    'BOX_LIGHT_HORIZONTAL', 'BOX_LIGHT_VERTICAL',
    'BOX_LIGHT_DOWN_RIGHT', 'BOX_LIGHT_DOWN_LEFT',
    'BOX_LIGHT_UP_RIGHT', 'BOX_LIGHT_UP_LEFT',
    'BOX_LIGHT_VERTICAL_RIGHT', 'BOX_LIGHT_VERTICAL_LEFT',
    'BOX_LIGHT_DOWN_HORIZONTAL', 'BOX_LIGHT_UP_HORIZONTAL',
    'BOX_LIGHT_VERTICAL_HORIZONTAL',
    'BOX_HEAVY_HORIZONTAL', 'BOX_HEAVY_VERTICAL',
    'BOX_HEAVY_DOWN_RIGHT', 'BOX_HEAVY_DOWN_LEFT',
    'BOX_HEAVY_UP_RIGHT', 'BOX_HEAVY_UP_LEFT',

    # Symbols
    'CHECKMARK', 'CROSS', 'BULLET',
    'ARROW_RIGHT', 'ARROW_LEFT', 'ARROW_UP', 'ARROW_DOWN',

    # Utility functions
    'clear_screen', 'clear_line', 'move_cursor',
    'hide_cursor', 'show_cursor', 'colorize', 'enchant',
]


# ============================================================================
# DEMO / TESTING
# ============================================================================

if __name__ == '__main__':
    # Standard foreground colors
    print(f"{FG_BLACK}FG_BLACK{RESET}")
    print(f"{FG_RED}FG_RED{RESET}")
    print(f"{FG_GREEN}FG_GREEN{RESET}")
    print(f"{FG_YELLOW}FG_YELLOW{RESET}")
    print(f"{FG_BLUE}FG_BLUE{RESET}")
    print(f"{FG_MAGENTA}FG_MAGENTA{RESET}")
    print(f"{FG_CYAN}FG_CYAN{RESET}")
    print(f"{FG_WHITE}FG_WHITE{RESET}")

    # Bright foreground colors
    print(f"{FG_BRIGHT_BLACK}FG_BRIGHT_BLACK{RESET}")
    print(f"{FG_BRIGHT_RED}FG_BRIGHT_RED{RESET}")
    print(f"{FG_BRIGHT_GREEN}FG_BRIGHT_GREEN{RESET}")
    print(f"{FG_BRIGHT_YELLOW}FG_BRIGHT_YELLOW{RESET}")
    print(f"{FG_BRIGHT_BLUE}FG_BRIGHT_BLUE{RESET}")
    print(f"{FG_BRIGHT_MAGENTA}FG_BRIGHT_MAGENTA{RESET}")
    print(f"{FG_BRIGHT_CYAN}FG_BRIGHT_CYAN{RESET}")
    print(f"{FG_BRIGHT_WHITE}FG_BRIGHT_WHITE{RESET}")

    # True RGB colors
    print(f"{TRUE_RED}TRUE_RED{RESET}")
    print(f"{TRUE_GREEN}TRUE_GREEN{RESET}")
    print(f"{TRUE_BLUE}TRUE_BLUE{RESET}")
    print(f"{TRUE_YELLOW}TRUE_YELLOW{RESET}")
    print(f"{TRUE_CYAN}TRUE_CYAN{RESET}")
    print(f"{TRUE_MAGENTA}TRUE_MAGENTA{RESET}")
    print(f"{TRUE_BLACK}TRUE_BLACK{RESET}")
    print(f"{TRUE_WHITE}TRUE_WHITE{RESET}")
    print(f"{TRUE_GRAY}TRUE_GRAY{RESET}")
    print(f"{TRUE_ORANGE}TRUE_ORANGE{RESET}")
    print(f"{TRUE_PURPLE}TRUE_PURPLE{RESET}")
    print(f"{TRUE_PINK}TRUE_PINK{RESET}")
    print(f"{TRUE_BROWN}TRUE_BROWN{RESET}")
    print(f"{TRUE_LIME}TRUE_LIME{RESET}")
    print(f"{TRUE_NAVY}TRUE_NAVY{RESET}")
    print(f"{TRUE_TEAL}TRUE_TEAL{RESET}")
    print(f"{TRUE_MAROON}TRUE_MAROON{RESET}")
    print(f"{TRUE_OLIVE}TRUE_OLIVE{RESET}")
    print(f"{TRUE_SILVER}TRUE_SILVER{RESET}")
    print(f"{TRUE_GOLD}TRUE_GOLD{RESET}")
    print(f"{TRUE_INDIGO}TRUE_INDIGO{RESET}")
    print(f"{TRUE_VIOLET}TRUE_VIOLET{RESET}")
    print(f"{TRUE_CORAL}TRUE_CORAL{RESET}")
    print(f"{TRUE_TURQUOISE}TRUE_TURQUOISE{RESET}")

    # Background colors
    print(f"{BG_BLACK}BG_BLACK{RESET}")
    print(f"{BG_RED}BG_RED{RESET}")
    print(f"{BG_GREEN}BG_GREEN{RESET}")
    print(f"{BG_YELLOW}BG_YELLOW{RESET}")
    print(f"{BG_BLUE}BG_BLUE{RESET}")
    print(f"{BG_MAGENTA}BG_MAGENTA{RESET}")
    print(f"{BG_CYAN}BG_CYAN{RESET}")
    print(f"{BG_WHITE}BG_WHITE{RESET}")

    # Bright background colors
    print(f"{BG_BRIGHT_BLACK}BG_BRIGHT_BLACK{RESET}")
    print(f"{BG_BRIGHT_RED}BG_BRIGHT_RED{RESET}")
    print(f"{BG_BRIGHT_GREEN}BG_BRIGHT_GREEN{RESET}")
    print(f"{BG_BRIGHT_YELLOW}BG_BRIGHT_YELLOW{RESET}")
    print(f"{BG_BRIGHT_BLUE}BG_BRIGHT_BLUE{RESET}")
    print(f"{BG_BRIGHT_MAGENTA}BG_BRIGHT_MAGENTA{RESET}")
    print(f"{BG_BRIGHT_CYAN}BG_BRIGHT_CYAN{RESET}")
    print(f"{BG_BRIGHT_WHITE}BG_BRIGHT_WHITE{RESET}")
