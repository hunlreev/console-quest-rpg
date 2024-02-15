'''
Module Name: menu.py
Description: Displays the menu at the start of the game as well as implements all of the options for the user.
Author: Hunter Reeves
Date: 2024-02-15
'''

# Modules
from modules.core import console_input, clear_console
from modules.console_art import art_main_menu, art_race, art_birthsign
from modules.creation import select_race, select_birthsign

# Imports
import os

def return_to_menu():
    """
    Helper Function: Returns to the main menu by user entering any key.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # Wait for any key to be pressed before returning to the main menu
    print("Press enter to return to the main menu...")
    console_input()

def about_game():
    """
    Prints some information and background about the game, how to play, etc.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # Clears existing console
    clear_console()

    # Start 'About Game' section
    art_main_menu()
    menu_line()
    print(" > About Console Quest RPG")
    menu_line()
    print("Console Quest RPG is an ASCII-based, text RPG inspired by several")
    print("games such as the Elder Scrolls series, and classic ASCII games.")
    print("\nTo play, simply follow along as you go and enter commands as needed.")
    print("The game will guide you as you progress, so please... adventure on!")
    print("\nIf you find any bugs, please let me know by shooting me a message")
    print("over Discord. My username is SaxyButters! I welcome all messages!")
    print("\nConsole Quest RPG was developed by Hunter Reeves. All rights reserved.")
    menu_line()

    return_to_menu()

def load_game():
    """
    Loads an existing character save file and starts the game.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # Clears existing console
    clear_console()

    # Start 'Load Game' section
    art_main_menu()
    menu_line()
    print(" > Load Game")
    menu_line()

    print("Not yet implemented.")
    menu_line()

    return_to_menu()

def new_game():
    """
    Creates a new character save file and starts the game.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # Clears existing console
    clear_console()

    # Start 'New Game' section
    art_main_menu()
    menu_line()
    print(" > New Game")
    menu_line()

    # Enter character name
    name = input("\nEnter thy name: ")

    # Clears existing console
    clear_console()

    # Select the character's race (starts the character's attributes off)
    race, attributes = select_race(name, art_race, menu_line)

    # Select the character's birthsign (affects the attributes)
    birth_sign, attributes = select_birthsign(name, attributes, art_birthsign, menu_line)

    return name, race, birth_sign, attributes

def main_menu():
    """
    Displays the main menu at the start of the gameplay loop.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # Display the menu art at the top
    art_main_menu()
    # Header/TItle
    menu_line()
    menu_title()
    menu_line()
    # Menu Selection
    menu_selection()
    menu_line()

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

def menu_selection(scalar = 50, version = "(v0.0.1-pre)"):
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