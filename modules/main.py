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
from classes.Enemy import Enemy

# Imports
import time
import random

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

def update_enemy_health_bar(enemy):
    """
    Takes enemy health and builds an updated health bar while in combat

    Parameters:
        enemy (object): The enemy.

    Returns:
        None.
    """
    
    health_bar, h_display = enemy.generate_stat_bar(enemy.stats['Health'], enemy.max_stats['Health'])
    
    print(f" -  Enemy Health: {health_bar} " + h_display)

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
    print(f" - Current Location: {player.location}")
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
    
    # List of locations the player can explore
    locations = ["Small Town", "Foggy Forest", "Desolate Cave", "Knoll Mountain", "Sandy Beach", "Abandoned Fort", "Sacked Camp"]
    
    # Define an encounter rate (e.g., 30% chance of encounter from 0.0 to 1.0)
    encounter_rate = 0.67
    
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
            # Randomly select a location
            player.location = random.choice(locations)
            
            # Randomly select how long to explore
            exploration_time = random.choice([(1, "for an hour"), (2, "for several hours"), (3, "for a day"), (4, "for a couple days")])
            menu_line()
            print(f" - You explore {exploration_time[1]}...")
            menu_line()
            time.sleep(exploration_time[0])
            
            # Extra message to display additional information when needed
            message = ""
            
            # Roll a random value to determine if an encounter happens
            if random.random() < encounter_rate:
                # Encounter an enemy
                enemy = Enemy(player.level, 3, player.location)
        
                while enemy.stats['Health'] > 0:
                    clear_console()
                    menu_line()
                    print(f" ^ You encountered a Level {enemy.level} {enemy.name} at {player.location}!")
                    menu_line()
                    update_enemy_health_bar(enemy)
                    menu_line()
                    update_stat_bars(player)
                    menu_line()
                    if message != "":
                        print(message)
                        menu_line()
                    print(" * What would you like to do?")
                    menu_line()
                    print(" 1. Attack\n 2. Cast Spell\n 3. Run Away")
                    menu_line()
                    user_input = console_input()
                    # Player attacks the enemy
                    if user_input == '1':
                        # Thresholds for critical hit and dodging
                        crit_threshold = round(random.random(), 2)
                        dodge_threshold = round(random.random(), 2)
                        # Player deals damage and loses stamina if enough stamina is available
                        if player.stats['Stamina'] >= player.stamina_cost:
                            message = ""
                            # Roll to see if Player will land a critical hit
                            if crit_threshold < player.critical_chance:
                                message = " - You landed a critical hit, dealing massive damage!"
                                enemy.stats['Health'] -= player.critical_hit
                                player.stats['Stamina'] -= player.stamina_cost
                            else:
                                message = ""
                                enemy.stats['Health'] -= player.physical_attack
                                player.stats['Stamina'] -= player.stamina_cost
                        else:
                            # Player only deals half as much damage
                            message = " - Not enough stamina! Dealing half as much damage."
                            enemy.stats['Health'] -= player.physical_attack / 2
                        if dodge_threshold < player.dodge_chance:
                            message = f" - You dodged the {enemy.name}'s attack!"
                        else:
                            message = f" - The {enemy.name} attacks you!"
                            player.stats['Health'] -= enemy.physical_attack
                    # Player cast a spell on the enemy
                    elif user_input == '2':
                        # Thresholds for critical hit and dodging
                        crit_threshold = round(random.random(), 2)
                        dodge_threshold = round(random.random(), 2)
                        # Player casts a spell and deals magic damage if enough mana is available
                        if player.stats['Mana'] >= player.mana_cost:
                            message = ""
                            enemy.stats['Health'] -= player.magical_attack
                            player.stats['Mana'] -= player.mana_cost
                        else:
                            # Not enough mana!
                            message = " - Not enough mana! You can't cast a spell right now!"
                        if dodge_threshold < player.dodge_chance:
                            message = f" - You dodged the {enemy.name}'s spell!"
                        else:
                            message = f" - The {enemy.name} casts a spell at you!"
                            player.stats['Health'] -= enemy.magical_attack
                    # Player attempts to run away from the enemy
                    elif user_input == '3':
                        if player.attributes['Speed'] > enemy.attributes['Speed']:
                            message = ""
                            break
                        else:
                            # Not fast enough!
                            message = " - Oh no, you are too slow! You cannot run from this enemy."
                    # Continue the encounter...
                    else:
                        user_input = ''
                # Add experience to the player after winning
                player.experience += enemy.dropped_exp
                # Level up if necessary
                if player.experience >= player.next_experience:
                    player.level_up()
            else:
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