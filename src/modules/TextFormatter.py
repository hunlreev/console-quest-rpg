'''
Contains functions for formatting console output to enhance the user interface in Console Quest RPG.

This module provides a set of utility functions specifically designed for printing formatted text in the console.
These functions create visual separation and structure within the game's menus, making it easier for players to navigate
and understand their options. The formatting includes lines, titles, and selection options that contribute to an 
engaging user experience.

Functions:
- MenuLine: Prints a decorative line for visual separation in the menu.
- MenuTitle: Displays the game title centered within the menu.
- MenuSelection: Prints the available options in the menu, including version information.
'''

def MenuLine(scalar: int = 73) -> None:
    """
    Prints a decorative line for visual separation in the menu.
    
    Parameters:
        scalar (int): Value for how many spaces go on either side of the title.
    """

    print("+" + "-" * scalar + "+")

def MenuTitle(scalar: int = 26) -> None:
    """
    Displays the game title centered within the menu.
    
    Parameters:
        scalar (int): Value for how many spaces go on either side of the title.
    """

    print(" " * scalar + "-- Console Quest RPG --" + " " * scalar)

def MenuSelection(scalar: int = 49, version: str = "(v0.2.2-pre)") -> None:
    """
    Prints the available options in the menu, including version information.
    
    Parameters:
        scalar (int): Value for how many spaces go on either side of the title.
        version (str): Current running version of the game.
    """

    quit_game = 4
    options = {"New Game": 1, "Load Game": 2, "About Game": 3, "Quit Game": 4}

    for option, number in options.items():
        if number == quit_game:
            print(f" {number}. {option}" + " " * scalar + version)
        else:
            print(f" {number}. {option}")