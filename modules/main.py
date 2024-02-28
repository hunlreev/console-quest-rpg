'''
Module Name: main.py
Description: Contains the actual gameplay loop and all the pieces that are implemented for it.
Author: Hunter Reeves
Date: 2024-02-28
'''

# Modules
from modules.menu import console_input, clear_console, main_menu, pause_menu
from modules.game import about_game, new_game, save_game, load_game, delete_game
from modules.console_art import art_planet, art_stars, art_battleaxe, art_skull
from modules.format import menu_line

# Classes
from classes.Player import Player
from classes.Enemy import Enemy

# Imports
import time
import random
import sys

def update_enemy_health_bar(enemy):
    """
    Takes enemy health and builds an updated health bar while in combat

    Parameters:
        enemy (object): The enemy.

    Returns:
        None.
    """
    
    health_bar, h_display = enemy.generate_stat_bar(enemy.stats['Health'], enemy.max_stats['Health'])
    
    print(f" -  Health: {health_bar} " + h_display)

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

def recover_stats(player):
    """
    Handles the resting portion of the game.

    Parameters:
        player (Player): The character save file that the user goes through the game with.

    Returns:
        None.
    """

    # Do some calculations...
    seconds_to_wait = player.rest()
    menu_line()
    
    # Players current speed stat
    speed = player.attributes['Speed']
    
    # Print a dynamic message based on how fast the player is when resting
    if speed < 10:
        print(" - Resting proves to be a challenge as you struggle to find comfort...")
    elif 10 <= speed < 20:
        print(" - You try to rest, but it's a bit of a struggle...")
    elif 20 <= speed < 30:
        print(" - It's not very effective, but you manage to rest anyway...")
    elif 30 <= speed < 40:
        print(" - You relax for a bit, and take your time to recover...")
    elif 40 <= speed < 50:
        print(" - A brief rest leaves you feeling much better than before...")
    elif 50 <= speed < 60:
        print(" - You rest for a short while and feel rejuvenated...")
    elif 60 <= speed < 70:
        print(" - You recover in no time and enjoy your rest...")
    elif 70 <= speed < 80:
        print(" - You rest and recover quickly, thinking about your progress...")
    elif 80 <= speed < 90:
        print(" - Your efficient rest results in near-instant recovery...")
    elif 90 <= speed < 100:
        print(" - You rejoice at the opportunity to restore yourself!")
    elif speed == 100:
        print(" - You recover your health instantly!")
    else:
        print(" - You take some time to rest and recuperate...")

    # Wait based on how fast the player is
    menu_line()
    time.sleep(seconds_to_wait)

def print_all_stats(player):
    """
    Prints all stats so the player can see their progress

    Parameters:
        player (object): The player

    Returns:
        None.
    """

    clear_console()
    art_stars()
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
    # Debug - not for final viewing
    print(f" - Physical attack: {player.physical_attack}")
    print(f" - Magical attack: {player.magical_attack}")
    print(f" - Critcal attack: {player.critical_hit}")
    menu_line()
    # Debug - not for final viewing
    print(f" - Physical defense: {player.physical_defense}")
    print(f" - Magical defense: {player.magical_defense}")
    menu_line()
    # Debug - not for final viewing
    print(f" - Critcal chance: {player.critical_chance}")
    print(f" - Dodge chance: {player.dodge_chance}")
    menu_line()

def check_dodge(player, enemy, dodge_threshold):
    """
    Handles the dodge logic during an encounter.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        enemy (Enemy): The enemy in the current encounter.
        dodge_threshold (float): Value to check against for dodging

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    # Check if player will dodge the enemy's attack
    if dodge_threshold < player.dodge_chance:
        return f" - You dodged the {enemy.type}'s attack!"
    # Failed to dodge the enemy's attack!
    else:
        player.stats['Health'] -= enemy.physical_attack - player.physical_defense
        return f" - The {enemy.type} attacks you!"

def run_away(player, enemy):
    """
    Handles the running away portion of the encounter.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        enemy (Enemy): The enemy in the current encounter.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    # Check if player is fast enough to run away
    if player.attributes['Speed'] > enemy.attributes['Speed']:
        return "Run away!"
    else:
        return f" - Oh no, you are too slow! You cannot run from this {enemy.type}."

def cast_spell(player, enemy):
    """
    Handles the spell casting portion of the encounter.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        enemy (Enemy): The enemy in the current encounter.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    crit_threshold = round(random.random(), 2)

    # Check if the player has enough mana first
    if player.stats['Mana'] >= player.mana_cost:
        # Check if spell will be a critical hit
        if crit_threshold < player.critical_chance:
            enemy.stats['Health'] -= player.critical_hit
            player.stats['Mana'] -= player.mana_cost
            return " - You landed a critical hit, dealing massive damage!"
        # Regular spell
        else:
            enemy.stats['Health'] -= player.magical_attack - enemy.magical_defense
            player.stats['Mana'] -= player.mana_cost
            return f" - You successfully casted a spell at the {enemy.type}!"
    # Not enough mana - cannot cast a spell!
    else:
        return " - You don't have enough mana to cast a spell right now!"

def attack(player, enemy):
    """
    Handles the attacking portion of the encounter.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        enemy (Enemy): The current enemy in the encounter.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    # Values for determining crits and dodging
    crit_threshold = round(random.random(), 2)

    # Check if player has enough stamina first
    if player.stats['Stamina'] >= player.stamina_cost:
        # Check if attack will be a critical hit (crits ignore defense stats)
        if crit_threshold < player.critical_chance:
            enemy.stats['Health'] -= player.critical_hit
            player.stats['Stamina'] -= player.stamina_cost
            return " - You landed a critical hit, dealing massive damage!"
        # Regular attack
        else:
            enemy.stats['Health'] -= player.physical_attack - enemy.physical_defense
            player.stats['Stamina'] -= player.stamina_cost
            return f" - You successfully attacked the {enemy.type}!"
    # Not enough stamina, cut amount of damage dealt in half
    else:
        enemy.stats['Health'] -= player.physical_attack / 2
        return " - You don't have enough stamina! Dealing half as much damage."

def player_input(player, enemy, user_input):
    """
    Handles the player input for the selection they make.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        enemy (Enemy): The current enemy in the encounter.
        user_input (string): Option the player selected in the previous menu.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    message = ""

    if user_input == '1':
        message = attack(player, enemy)
    elif user_input == '2':
        message = cast_spell(player, enemy)
    elif user_input == '3':
        message = run_away(player, enemy)
    
    return message

def enemy_encounter(player, message):
    """
    Handles the enemy encounters when they happen.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        message (str): A message that displays when updated.

    Returns:
        None.
    """

    # Function to handle death cooldown timer
    def return_to_main_menu_countdown(seconds):
        # Iterate through the number of seconds for the timer
        for i in range(seconds, 0, -1):
            sys.stdout.write(f"\r ^ Returning to main menu in: {i}")
            sys.stdout.flush()
            time.sleep(1)
        # Final message
        sys.stdout.write("\r ^ Returning to main menu in: 0\n")
        sys.stdout.flush()

    enemy = Enemy(player.level, 2, player.location)

    # Continue the encounter while the player is alive
    while player.stats['Health'] > 0:
        clear_console()
        art_battleaxe()
        menu_line()
        print(f" ^ You encountered a Level {enemy.level} {enemy.type} at {player.location}!")
        menu_line()
        # Debug - not for final viewing
        # print(f" - Physical defense: {enemy.physical_defense}")
        # print(f" - Magical defense: {enemy.magical_defense}")
        # menu_line()
        update_enemy_health_bar(enemy)
        menu_line()
        update_stat_bars(player)
        menu_line()
        
        # Only print a message in this section if there is something to display
        if message != "":
            print(message)
            menu_line()

        print(" * What would you like to do?")
        menu_line()
        print(" 1. Attack\n 2. Cast Spell\n 3. Run Away")
        menu_line()
        user_input = console_input()

        # Check speed stat to determine who attacks first? YES.
        # Player attack handled here
        message = player_input(player, enemy, user_input)
        # Code for enemy attacks go here (randomize attack, physical or magical - account for enemy dodge/crit)
        # message = enemy_output(enemy, player) ? or something like that...
        # Handle dodging of player through enemy_output instead of when player attacks...
        # specific message output for player first and then wait, then display messages for enemy? hmm...
        
        # Determine if user runs away from the encounter
        if message == "Run away!":
            clear_console()
            art_planet()
            menu_line()
            print(f" ^ You managed to run away from the {enemy.type}!")
            menu_line()
            time.sleep(3)
            break
        
        # Check if the player died
        if player.stats['Health'] <= 0:
            clear_console()
            art_skull()
            menu_line()
            print(f" ^ The {enemy.type} killed you! Please reload your last saved game.")
            menu_line()
            return_to_main_menu_countdown(5)
            break

        # Check if player should get experience
        if enemy.stats['Health'] <= 0:
            clear_console()
            art_stars()
            menu_line()
            print(f" ^ You defeated the {enemy.type}!")
            menu_line()
            print(f" - You have earned {enemy.dropped_exp} experience.")
            print(f" - You looted {enemy.dropped_gold} gold.")
            menu_line()
            player.experience += enemy.dropped_exp
            player.gold += enemy.dropped_gold
            time.sleep(3)
            # Check if player should level up
            if player.experience >= player.next_experience:
                clear_console()
                player.level_up()
            break

    return_to_game(user_input)

def explore_location(player, locations, encounter_rate):
    """
    Allows the player to explore a randomly selected location.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        locations (List): A list of locations for the player to explore.
        encounter_rate (Float): A value from 0 to 1 that describes the encounter rate.

    Returns:
        None.
    """
    
    # Randomly selected location
    player.location = random.choice(locations)

    # Determine how long the exploration will last
    exploration_time = random.choice([(1, "a quick adventure"), (2, "a short, nearby exploration"), (3, "a long journey"), (4, "huge campaign and get lost")])

    menu_line()
    print(f" - You set out for {exploration_time[1]}...")
    menu_line()
    time.sleep(exploration_time[0])

    message = ""

    # Determine if an enemy encounter will happen or not
    if random.random() < encounter_rate:
        enemy_encounter(player, message)
    else:
        return_to_game("")

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
    print(f" - Gold: {int(player.gold)}")
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

    # Function to handle selection in the pause menu when it is active
    def pause_menu_selection():
        if user_input == '1':
            return_to_game(user_input)
        elif user_input == '2':
            save_game(player)
        elif user_input == '3':
            save_game(player)
            return "Exit"
        elif user_input == '4':
            return "Exit"
        elif user_input == '5':
            delete_game()
        else:
            return_to_game(user_input)

    # List of locations to go to during the game
    locations = ["Small Town", "Foggy Forest", "Desolate Cave", "Knoll Mountain", "Sandy Beach", "Abandoned Fort", "Sacked Camp"]

    # Set enemy encounter rate while exploring from 0 to 1
    encounter_rate = 0.67

    # Only continue if a player currently exists by this point
    if player is None:
        return

    # Main gameplay loop while the player is still alive
    while player.stats['Health'] > 0:
        user_input = display_menu(player)

        if user_input == '1':
            pause_menu()
            user_input = console_input()
            exit = pause_menu_selection()
            # Break out of the loop
            if exit == "Exit":
                break
        elif user_input == '2':
            clear_console()
            art_planet()
            explore_location(player, locations, encounter_rate)
        elif user_input == '3':
            print_all_stats(player)
            print(" * Press enter to return to the game...")
            menu_line()
            console_input()
        elif user_input == '4':
            clear_console()
            art_stars()
            recover_stats(player)
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
            player = Player(**player_info)
            start_game(player)
        elif user_input == '2':
            player = load_game()
            start_game(player)
        elif user_input == '3':
            about_game()
        elif user_input == '4':
            # Exit the game
            break