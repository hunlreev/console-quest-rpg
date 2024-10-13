'''
Entry point for the Console Quest RPG.

This module initializes and starts the game by invoking the InitializeGame function from the Launcher module. It is responsible for setting up the gameplay loop and handling the transition from the main menu to the core game mechanics.

Execution starts when the module is run directly from the console or terminal.
'''

from src.modules.Launcher import InitializeGame

if __name__ == "__main__":
    InitializeGame()