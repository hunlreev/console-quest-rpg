'''
Module Name: menu.py
Description: Displays the menu at the start of the game as well as implements all of the options for the user.
Author: Hunter Reeves
Date: 2024-03-01
'''

from modules.core import console_input, clear_console
from modules.format import menu_line, menu_selection, menu_title
from modules.console_art import art_dragon

def return_to_menu():
    """
    Helper Function: Returns to the main menu by user entering any key.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    print(" * Press enter to return to the main menu...")
    menu_line()
    console_input()

def pause_menu():
    """
    Prints a menu of options with continue, save, or quit
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    clear_console()
    art_dragon()
    menu_line()
    print(" ^ Game Paused")
    menu_line()
    
    options = {"Continue Playing": 1, "Save And Continue": 2, "Save and Quit": 3, "Quit Without Saving": 4, "Delete A Save": 5}

    for option, number in options.items():
        print(f" {number}. {option}")

    menu_line()

def main_menu():
    """
    Displays the main menu at the start of the gameplay loop.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    art_dragon()
    menu_line()
    menu_title()
    menu_line()
    menu_selection()
    menu_line()