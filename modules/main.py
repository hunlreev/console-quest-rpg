'''
Module Name: main.py
Description: Contains the actual gameplay loop and all the pieces that are implemented for it.
Author: Hunter Reeves
Date: 2024-02-22
'''

# Modules
from modules.menu import console_input, clear_console, main_menu, pause_menu
from modules.game import about_game, new_game, save_game, load_game, delete_game
from modules.format import menu_line

# Classes
from classes.Player import Player

# Imports
import time

def print_all_stats(player):
    """
    Prints all stats so the player can see their progress

    Parameters:
        player (object): The player

    Returns:
        None.
    """

    clear_console()
    menu_line()
    print(f" ^ {player.name}'s Stats")
    menu_line()
    print(f" - Available Attribute Points: {player.attribute_points}")
    menu_line()
    print(f" - Strength: {player.attributes['Strength']}")
    print(f" - Endurance: {player.attributes['Endurance']}")
    print(f" - Intelligence: {player.attributes['Intelligence']}")
    print(f" - Willpower: {player.attributes['Willpower']}")
    print(f" - Agility: {player.attributes['Agility']}")
    print(f" - Speed: {player.attributes['Speed']}")
    menu_line()
    print(f" - Physical attack: {player.physical_attack}")
    print(f" - Magical attack: {player.magical_attack}")
    print(f" - Critcal attack: {player.critical_hit}")
    menu_line()
    print(f" - Critcal chance: {player.critical_chance}")
    print(f" - Dodge chance: {player.dodge_chance}")
    menu_line()

def return_to_game(user_input):
    """
    Takes the user back to the main game menu to continue playing.

    Parameters:
        user_input (str): User input.

    Returns:
        user_input (str): Empty string to continue playing.
    """

    user_input = ''

    return user_input

def update_stat_bars(player):
    """
    Takes player stats and builds updated stat bars before printing them out.

    Parameters:
        player (object): The player character.

    Returns:
        None.
    """
    
    health_bar, h_display = player.generate_stat_bar(player.stats['Health'], player.max_stats['Health'])
    mana_bar, m_display = player.generate_stat_bar(player.stats['Mana'], player.max_stats['Mana'])
    stamina_bar, s_display = player.generate_stat_bar(player.stats['Stamina'], player.max_stats['Stamina'])

    print(f" -  Health: {health_bar} " + h_display)
    print(f" -    Mana: {mana_bar} " + m_display)
    print(f" - Stamina: {stamina_bar} " + s_display)
    
def update_exp_bar(player):
    """
    Takes player experience and displays an experience bar

    Parameters:
        player (object): The player character.

    Returns:
        None.
    """
    
    exp_bar, e_display = player.generate_exp_bar(player.experience, player.next_experience)

    print(f" - EXP: {exp_bar} " + e_display)

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
    update_stat_bars(player)
    menu_line()
    update_exp_bar(player)
    menu_line()
    print(" * What would you like to do?")
    menu_line()

    options = {"Pause Game": 1, "Explore World": 2, "View Stats": 3, "Rest": 4}

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

    # Debug - amount of stat points lost each time (for losing stats, updating the bars)
    health_loss = 12.5
    added_exp = 95
    
    # Exit to main menu if no player exits yet
    if player is None:
        return

    # Main game loop
    while True:
        # User input to determine what to do next
        user_input = display_menu(player)

        # Pause the game
        if user_input == '1':
            pause_menu()
            user_input = console_input()

            # Menu to continue, save the game, or exit
            if user_input == '1':
                return_to_game(user_input)
            elif user_input == '2':
                save_game(player)
                return
            elif user_input == '3':
                user_input = delete_game()
                return_to_game(user_input)
            elif user_input == '4':
                return
            else:
                return_to_game(user_input)
        # Explore the existing world - Not implemented
        elif user_input == '2':
            return_to_game(user_input)
        # View all player stats - Not implemented
        elif user_input == '3':
            print_all_stats(player)
            print(" * Press enter to return to the game...")
            menu_line()
            console_input()
        # Rest and restore stats - Not implemented
        elif user_input == '4':
            seconds_to_wait = player.rest()
            menu_line()
            print(" - You rest for a little bit...")
            menu_line()
            time.sleep(seconds_to_wait)
        elif user_input == '5':
            # Debugging
            player.lose_stat_points('Health', health_loss)
        elif user_input == '6':
            player.cast_spell()
        elif user_input == '7':
            player.use_physical()
        elif user_input == '8':
            player.add_experience(added_exp)
            if player.experience >= player.next_experience:
                menu_line()
                player.level_up()
        # If not a pre-determined option, return to game (do nothing, essentially)
        else:
            return_to_game(user_input)
    
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