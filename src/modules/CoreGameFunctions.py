'''
Provides core utility functions that are essential across various modules in Console Quest RPG.

This module contains foundational functions used throughout the game to handle common tasks such as
clearing the console, handling user input, and managing transitions back to gameplay. These functions 
are designed to be accessible and reusable by other modules to maintain consistency in core gameplay mechanics.

Functions:
- ConsoleInput: Prompts the user for input and returns it in a formatted manner.
- ClearConsole: Clears the console screen for a clean display.
- ReturnToGame: Resets user input and facilitates returning to the main game menu.
'''

import os

def ConsoleInput() -> str:
    """
    Prompts the user for input and returns it in a formatted manner.
    
    Returns:
        user_input(str): The string entered by the user.
    """

    user_input = str(input(" > "))

    return user_input

def ClearConsole()-> None:
    """
    Clears the console screen for a clean display.
    """

    os.system('cls' if os.name == 'nt' else 'clear')

def ReturnToGame(user_input: str) -> str:
    """
    Resets user input and facilitates returning to the main game menu.

    Parameters:
        user_input (str): User input.

    Returns:
        user_input (str): Empty string to continue playing.
    """

    user_input = ''

    return user_input