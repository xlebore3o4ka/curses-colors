import curses

"""
This module provides a simple interface for managing color pairs in a terminal using the curses library.
It defines a set of color constants and initializes color pairs for foreground and background combinations.
"""

class ColorsVariables:
    """
    A class that defines constants for color pairs used in the curses library.

    The constants are defined as class attributes, representing combinations of foreground and background colors.
    The colors are represented as integers in the range of 0 to 63, corresponding to the 64 possible color pairs.

    Attributes:
        BLACK_BLACK, BLACK_RED, ..., WHITE_WHITE: Integer constants representing color pairs.
    """
    BLACK_BLACK,   BLACK_RED,   BLACK_GREEN,   BLACK_YELLOW,   BLACK_BLUE,   BLACK_MAGENTA,   BLACK_CYAN,   BLACK_WHITE, \
    RED_BLACK,     RED_RED,     RED_GREEN,     RED_YELLOW,     RED_BLUE,     RED_MAGENTA,     RED_CYAN,     RED_WHITE, \
    GREEN_BLACK,   GREEN_RED,   GREEN_GREEN,   GREEN_YELLOW,   GREEN_BLUE,   GREEN_MAGENTA,   GREEN_CYAN,   GREEN_WHITE, \
    YELLOW_BLACK,  YELLOW_RED,  YELLOW_GREEN,  YELLOW_YELLOW,  YELLOW_BLUE,  YELLOW_MAGENTA,  YELLOW_CYAN,  YELLOW_WHITE, \
    BLUE_BLACK,    BLUE_RED,    BLUE_GREEN,    BLUE_YELLOW,    BLUE_BLUE,    BLUE_MAGENTA,    BLUE_CYAN,    BLUE_WHITE, \
    MAGENTA_BLACK, MAGENTA_RED, MAGENTA_GREEN, MAGENTA_YELLOW, MAGENTA_BLUE, MAGENTA_MAGENTA, MAGENTA_CYAN, MAGENTA_WHITE, \
    CYAN_BLACK,    CYAN_RED,    CYAN_GREEN,    CYAN_YELLOW,    CYAN_BLUE,    CYAN_MAGENTA,    CYAN_CYAN,    CYAN_WHITE, \
    WHITE_BLACK,   WHITE_RED,   WHITE_GREEN,   WHITE_YELLOW,   WHITE_BLUE,   WHITE_MAGENTA,   WHITE_CYAN,   WHITE_WHITE = \
    range(64)


class Colors(ColorsVariables):
    """
    A class that manages color initialization and provides access to color pairs.

    This class extends ColorsVariables and provides methods to initialize color pairs and access them.
    """

    _colors = [
        curses.COLOR_BLACK, curses.COLOR_RED,     curses.COLOR_GREEN, curses.COLOR_YELLOW,
        curses.COLOR_BLUE,  curses.COLOR_MAGENTA, curses.COLOR_CYAN,  curses.COLOR_WHITE
    ]
    _colors_names = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"]
    _length = len(_colors)

    @classmethod
    def init_colors(cls):
        """
        Initializes color pairs for all combinations of foreground and background colors.

        Raises:
            RuntimeError: If the terminal does not support colors.
        """
        if not curses.has_colors():
            raise RuntimeError("Colors not supported")

        for fg in range(cls._length):
            for bg in range(cls._length):
                pair_number = fg + bg * cls._length + 1
                curses.init_pair(pair_number, cls._colors[fg], cls._colors[bg])
                setattr(cls, f"{cls._colors_names[bg]}_{cls._colors_names[fg]}",
                        curses.color_pair(pair_number))
