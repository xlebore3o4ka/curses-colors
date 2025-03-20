# curses-colors

`curses-colors` is a Python module that provides a simple interface for managing color pairs in a terminal using the `curses` library. This module allows you to easily initialize and access various color combinations for terminal applications.

## Installation

To use the `curses-colors` module, ensure you have Python installed on your system. The `curses` library is included with Python on Unix-like systems. For Windows, you may need to install a compatible version of the `curses` library, such as `windows-curses`.

## Usage

### Importing the Module

To use the `curses-colors` module, you need to import it into your Python script:

```python
import curses
from curses_colors import Colors
```

### Initializing Colors

Before using any color pairs, you must initialize them. This is done by calling the `init_colors` method of the `Colors` class. Make sure to do this after initializing the `curses` screen.

```python
def main(stdscr):
    # Initialize colors
    Colors.init_colors()
    
    # Example usage of color pairs
    stdscr.addstr(0, 0, "Hello, World!", Colors.RED_BLACK)
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
```

### Accessing Color Pairs

The color pairs are defined as class attributes in the `Colors` class. You can access them using the format `Colors.<BACKGROUND>_<FOREGROUND>`. Here are the available color pairs:

- `Colors.BLACK_BLACK`
- `Colors.BLACK_RED`
- `Colors.BLACK_GREEN`
- `Colors.BLACK_YELLOW`
- `Colors.BLACK_BLUE`
- `Colors.BLACK_MAGENTA`
- `Colors.BLACK_CYAN`
- `Colors.BLACK_WHITE`
- `Colors.RED_BLACK`
- `Colors.RED_RED`
- `Colors.RED_GREEN`
- `Colors.RED_YELLOW`
- `Colors.RED_BLUE`
- `Colors.RED_MAGENTA`
- `Colors.RED_CYAN`
- `Colors.RED_WHITE`
- `Colors.GREEN_BLACK`
- `Colors.GREEN_RED`
- `Colors.GREEN_GREEN`
- `Colors.GREEN_YELLOW`
- `Colors.GREEN_BLUE`
- `Colors.GREEN_MAGENTA`
- `Colors.GREEN_CYAN`
- `Colors.GREEN_WHITE`
- `Colors.YELLOW_BLACK`
- `Colors.YELLOW_RED`
- `Colors.YELLOW_GREEN`
- `Colors.YELLOW_YELLOW`
- `Colors.YELLOW_BLUE`
- `Colors.YELLOW_MAGENTA`
- `Colors.YELLOW_CYAN`
- `Colors.YELLOW_WHITE`
- `Colors.BLUE_BLACK`
- `Colors.BLUE_RED`
- `Colors.BLUE_GREEN`
- `Colors.BLUE_YELLOW`
- `Colors.BLUE_BLUE`
- `Colors.BLUE_MAGENTA`
- `Colors.BLUE_CYAN`
- `Colors.BLUE_WHITE`
- `Colors.MAGENTA_BLACK`
- `Colors.MAGENTA_RED`
- `Colors.MAGENTA_GREEN`
- `Colors.MAGENTA_YELLOW`
- `Colors.MAGENTA_BLUE`
- `Colors.MAGENTA_MAGENTA`
- `Colors.MAGENTA_CYAN`
- `Colors.MAGENTA_WHITE`
- `Colors.CYAN_BLACK`
- `Colors.CYAN_RED`
- `Colors.CYAN_GREEN`
- `Colors.CYAN_YELLOW`
- `Colors.CYAN_BLUE`
- `Colors.CYAN_MAGENTA`
- `Colors.CYAN_CYAN`
- `Colors.CYAN_WHITE`
- `Colors.WHITE_BLACK`
- `Colors.WHITE_RED`
- `Colors.WHITE_GREEN`
- `Colors.WHITE_YELLOW`
- `Colors.WHITE_BLUE`
- `Colors.WHITE_MAGENTA`
- `Colors.WHITE_CYAN`
- `Colors.WHITE_WHITE`

### Example

Here is a complete example of how to use the `curses-colors` module:

```python
import curses
from curses_colors import Colors

def main(stdscr):
    # Initialize colors
    Colors.init_colors()
    
    # Clear the screen
    stdscr.clear()
    
    # Display text with different color pairs
    stdscr.addstr(0, 0, "This is black text on a white background", Colors.WHITE_BLACK)
    stdscr.addstr(1, 0, "This is red text on a black background", Colors.RED_BLACK)
    stdscr.addstr(2, 0, "This is green text on a yellow background", Colors.GREEN_YELLOW)
    
    # Refresh the screen to show changes
    stdscr.refresh()
    
    # Wait for user input
    stdscr.getch()

curses.wrapper(main)
```

## License

This module is released under the MIT License. See the LICENSE file for more details.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue for any bugs or feature requests.

## Acknowledgments

This module utilizes the `curses` library,
