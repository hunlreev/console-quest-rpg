'''
Module Name: format.py
Description: Contains all the print console formatting functions
Author: Hunter Reeves
Date: 2024-02-17
'''

def menu_line(scalar = 73):
    """
    Prints an artistic line for separation within the menu.
    
    Parameters:
        scalar (int):
            Value for how many spaces go on either side of the title.
    
    Returns:
        None.
    """

    print("+" + "-" * scalar + "+")

def menu_title(scalar = 26):
    """
    Prints the title of the game in the menu.
    
    Parameters:
        scalar (int):
            Value for how many spaces go on either side of the title.
    
    Returns:
        None.
    """

    print(" " * scalar + "-- Console Quest RPG --" + " " * scalar)

def menu_selection(scalar = 49, version = "(v0.0.1-pre)"):
    """
    Prints the options in the menu for the player to choose from.
    
    Parameters:
        scalar (int):
            Value for how many spaces go on either side of the title.
    
    Returns:
        None.
    """

    # Options for the menu selection
    options = {"New Game": 1, "Load Game": 2, "About Game": 3, "Quit Game": 4}

    # Display options in the menu
    for option, number in options.items():
        if number == 4:  # Print version information only for "Quit Game"
            print(f" {number}. {option}" + " " * scalar + version)
        else:
            print(f" {number}. {option}")