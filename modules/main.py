'''
Module Name: main.py
Description: Contains the actual gameplay loop and all the pieces that are implemented for it.
Author: Hunter Reeves
Date: 2024-02-17
'''

# Modules
from modules.menu import console_input, clear_console, main_menu, pause_menu
from modules.game import about_game, new_game, save_game, load_game
from modules.format import menu_line

# Classes
from classes.Player import Player

def display_menu(player):
    """
    Display the game menu.

    Parameters:
        player (Player): The character save file that the user goes through the game with.

    Returns:
        str: The user's input.
    """

    clear_console()
    menu_line()
    print(f" ^ Welcome {player.name} the {player.race}!")
    menu_line()
    print(f" - You are a Level {player.level} {player.player_class}, born under {player.birth_sign} sign.")
    menu_line()
    print(f" - Health: {player.stats['Health']}/{player.max_stats['Health']} | Mana: {player.stats['Mana']}/{player.max_stats['Mana']} | Stamina: {player.stats['Stamina']}/{player.max_stats['Stamina']}")
    # print(f" - Mana: {player.stats['Mana']}/{player.max_stats['Mana']}")
    # print(f" - Stamina: {player.stats['Stamina']}/{player.max_stats['Stamina']}")
    menu_line()
    print(" * What would you like to do?")
    menu_line()

    options = {"Pause Game": 1, "Explore World": 2, "View All Stats": 3, "Rest": 4}

    # Display options in the menu
    for option, number in options.items():
        print(f" {number}. {option}")

    menu_line()

    return console_input()

def start_game(player):
    """
    The main gameplay loop for Console Quest RPG.

    Parameters:
        player (Player): The character save file that the user goes through the game with.

    Returns:
        None.
    """
    
    if player is None:
        return

    while True:
        user_input = display_menu(player)

        if user_input == '1':
            pause_menu()
            user_input = console_input()

            if user_input == '1':
                user_input = ''
            elif user_input == '2':
                save_game(player)
                return
            elif user_input == '3':
                return
        else:
            return
    
def initialize_game():
    """
    Initializes the main menu for Console Quest RPG.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    while True:
        # Get input from the user to select options from the main menu
        clear_console()
        main_menu()
        print(" * Select an option from the menu above:")
        menu_line()
        user_input = console_input()

        # Determine the user menu selection
        if user_input == '1':
            # Start a new character for a new game
            name, race, birth_sign, player_class, attributes = new_game()
            # Consolidate information
            player_info = {
                'name': name,
                'race': race,
                'birth_sign': birth_sign,
                'player_class': player_class,
                'attributes': attributes
            }
            # Create a new player and start the game with that player
            player = Player(**player_info)
            start_game(player)
        elif user_input == '2':
            # Load an existing character from a previously saved game
            player = load_game()
            start_game(player)
        elif user_input == '3':
            # View information/controls on how to play the game
            about_game()
        elif user_input == '4':
            # Exit the game
            break