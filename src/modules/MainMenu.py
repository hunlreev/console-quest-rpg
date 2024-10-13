'''
Handles displaying various game menus and user options for Console Quest RPG.

This module is responsible for managing the display of key menus in the game, including:
- The main menu shown at the start of the game.
- The in-game pause menu with options for saving, quitting, or continuing gameplay.
- Functionality for returning to the main menu from other parts of the game.

The module is crucial for facilitating user interaction with the game, allowing them to control the flow of the gameplay.

Functions:
- ReturnToMainMenu: Prompts the user to press enter to return to the main menu.
- PauseMenu: Displays a pause menu with options to save, quit, or delete a save file.
- MainMenu: Displays the main menu with game title and options at the start of the game.
'''

from src.modules.CoreGameFunctions import ConsoleInput, ClearConsole
from src.modules.TextFormatter import MenuLine, MenuSelection, MenuTitle
from src.modules.ArtAssets import DisplayDragon

def ReturnToMainMenu() -> None:
    """
    Returns to the main menu by prompting the user to press a key.
    """

    print(" * Press enter to return to the main menu...")
    MenuLine()
    ConsoleInput()

def PauseMenu() -> None:
    """
    Prints a menu of options when the game is paused. Options include continuing, saving, or quitting.
    """

    ClearConsole()
    DisplayDragon()
    MenuLine()
    print(" ^ Game Paused")
    MenuLine()
    
    options = [
        "Save and Continue Playing", 
        "Save and Quit to Main Menu", 
        "Quit to Main Menu without Saving", 
        "Delete a Save"
    ]

    for index, option in enumerate(options, 1):
        print(f" {index}. {option}")

    MenuLine()
    print(" * Press enter to return to the game...")
    MenuLine()

def MainMenu() -> None:
    """
    Displays the main menu at the start of the gameplay loop.
    """

    DisplayDragon()
    MenuLine()
    MenuTitle()
    MenuLine()
    MenuSelection()
    MenuLine()