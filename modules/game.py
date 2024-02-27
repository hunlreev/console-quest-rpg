'''
Module Name: game.py
Description: Core functionality for the main menu and starting the game
Author: Hunter Reeves
Date: 2024-02-27
'''

# Modules
from modules.core import clear_console
from modules.console_art import art_dragon, art_planet, art_stars, art_battleaxe
from modules.creation import select_race, select_birthsign, select_class
from modules.menu import menu_line, return_to_menu

# Imports
import os
import pickle

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
    art_dragon()
    menu_line()
    print(" ^ About Console Quest RPG")
    menu_line()
    print(" Console Quest RPG is an ASCII-based, text RPG inspired by several")
    print(" games such as the Elder Scrolls series, and classic ASCII games.")
    print("\n To play, simply follow along as you go and enter commands as needed.")
    print(" The game will guide you as you progress, so please... adventure on!")
    print("\n If you find any bugs, please let me know by shooting me a message")
    print(" over Discord. My username is SaxyButters! I welcome all messages!")
    print("\n Console Quest RPG was developed by Hunter Reeves. All rights reserved.")
    menu_line()

    return_to_menu()

def delete_game():
    """
    Deletes an existing save file.

    Parameters:
        None.

    Returns:
        None.
    """

    clear_console()

    saves_directory = "saves"  # Change this to your actual saves directory

    # Check if saves directory exists
    if not os.path.exists(saves_directory) or not os.path.isdir(saves_directory):
        print("No saved games found.")
        return

    # List available saved games
    saved_games = [file for file in os.listdir(saves_directory) if os.path.isfile(os.path.join(saves_directory, file))]
    
    if not saved_games:
        return ""
    
    menu_line()
    print(" * Select a save to delete (Enter 0 to cancel):")
    menu_line()
    for idx, game in enumerate(saved_games, start = 1):
        save_name = os.path.splitext(game)[0]
        print(f" {idx}. {save_name}")
    menu_line()

    try:
        choice = int(input(" > "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 < choice <= len(saved_games):
        selected_game = saved_games[choice - 1]
        menu_line()
        print(f" * Are you sure you want to delete this save? (Y/N)")
        menu_line()
        confirm = str(input(" > "))
        
        menu_line()

        if confirm.lower() == 'y':
            file_path = os.path.join(saves_directory, selected_game)
            os.remove(file_path)
        elif confirm.lower() == 'n':
            return ""
        else:
            return ""
    else:
        return

def load_game():
    """
    Loads an existing character from a previously saved file.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # Directory for all save files
    saves_directory = 'saves\\'

    # Start the load menu screen
    clear_console()
    art_dragon()

    # List all save files in the directory
    save_files = [f for f in os.listdir(saves_directory) if f.endswith('.pkl')]

    if not save_files:
        menu_line()
        print(" ^ Load Game")
        menu_line()
        print(" No saved games found. You will need to start a new game.\n\n Please go back to the main menu to start a new game.")
        menu_line()
        return_to_menu()
        return None

    # Display the list of save files with index
    menu_line()
    print(" ^ Load Game")
    menu_line()
    print(" * Choose a saved character to load:")
    menu_line()
    for i, save_file in enumerate(save_files, start = 1):
        # Remove ".pkl" extension when displaying the save file name
        save_name = os.path.splitext(save_file)[0]
        print(f" {i}. {save_name}")

    # Get user input for the selected save file
    while True:
        try:
            menu_line()
            choice = int(input(" > "))
            if 0 <= choice <= len(save_files):
                break
            else:
                menu_line()
                print(" * Invalid choice. Please enter a valid number.")
        except ValueError:
            menu_line()
            print(" * Invalid input. Please enter a number.")

    selected_save_file = save_files[choice - 1]

    with open(os.path.join(saves_directory, selected_save_file), 'rb') as file:
        player = pickle.load(file)

    return player

def save_game(player):
    """
    Saves the current player to a file for loading later on.
    
    Parameters:
        player (Player): The character that will be saved.
    
    Returns:
        None.
    """

    with open('saves\\' + player.name + '.pkl', 'wb') as file:
        pickle.dump(player, file)

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
    art_dragon()
    menu_line()
    print(" ^ New Game")
    menu_line()

    # Enter character name
    print(" * Enter thy name:")
    menu_line()
    name = input(" > ")
    # Default name if none is selected
    if name == "":
        name = 'Player'
    # Clears existing console
    clear_console()

    # Select the character's race (starts the character's attributes off)
    race, attributes = select_race(name, art_planet, menu_line)

    # Select the character's birthsign (affects the attributes)
    birth_sign, attributes = select_birthsign(name, attributes, art_stars, menu_line)

    # Select the character's class (affects the attributes)
    player_class, attributes = select_class(name, attributes, art_battleaxe, menu_line)

    # Return all character information to create the Player
    return name, race, birth_sign, player_class, attributes