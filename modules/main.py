'''
Module Name: main.py
Description: Contains the actual gameplay loop and all the pieces that are implemented for it.
Author: Hunter Reeves
Date: 2024-02-15
'''

# Modules
from modules.menu import console_input, clear_console, main_menu, new_game, load_game, about_game, menu_line
from modules.console_art import art_main_menu
    
def initialize_game():
    """
    Initializes the gameplay loop for Console Quest RPG.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # Main gameplay loop
    while True:
        # Clear terminal at start of game play loop
        clear_console()

        # Display the main menu screen
        main_menu()
        
        # Get input from the user to select options from the main menu
        user_input = console_input()

        # Determine the selection
        if user_input == '1':
            # Start a new character
            name, race, birth_sign, attributes = new_game()
            # Clean up the console for the start of the game
            clear_console()
            art_main_menu()
            menu_line()
            # Print current location (placeholder for now)
            print("> Current Location: Unknown")
            menu_line()
            # Persistent stats for viewing at all times
            print(f"> Welcome {name}, the {race}! Born under {birth_sign}.")
            menu_line()
            # See attributes (debug)
            print("> Attributes:")
            for attr_name, attr_value in zip(["Strength", "Endurance", "Intelligence", "Willpower", "Agility", "Speed"], attributes):
                print(f"+ {attr_value} - {attr_name}")
            menu_line()
            # Continue the game here...
            console_input()
        elif user_input == '2':
            # Load an existing character (not yet implemented)
            load_game()
        elif user_input == '3':
            # View information/controls on how to play the game
            about_game()
        elif user_input == '4':
            # Exit the game
            break