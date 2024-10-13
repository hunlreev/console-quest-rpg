'''
Core functionality for the main menu and starting the game.

This module handles the main menu operations, including displaying game 
information, deleting and loading saved games, and starting new games. 
It includes functions to manage player character creation and interactions 
with saved game files. The game supports basic ASCII art for a visual 
presentation and aims to provide a text-based RPG experience.

Functions:
- AboutGame: Displays some information and background about the game, how to play, etc.
- DeleteGame: Deletes an existing saved game.
- LoadGame: Loads a saved character from a file.
- SaveGame: Saves the current player character to a file.
- GetSex: Prompts the user to select the player's sex.
- GetName: Prompts the user to enter the player's name.
- NewGame: Initializes a new game with character attributes.
'''

from src.modules.CoreGameFunctions import ClearConsole
from src.modules.ArtAssets import DisplayDragon, DisplayPlanet, DisplayStars, DisplayBattleAxe
from src.modules.CharacterCreation import SelectRace, SelectBirthsign, SelectClass
from src.modules.MainMenu import MenuLine, ReturnToMainMenu

from src.classes.Player import Player

import os
import pickle

def AboutGame() -> None:
    """
    Displays some information and background about the game, how to play, etc.
    """

    ClearConsole()

    DisplayDragon()
    MenuLine()
    print(" ^ About Console Quest RPG")
    MenuLine()
    print(" Console Quest RPG is an ASCII-based, text RPG inspired by several")
    print(" games such as the Elder Scrolls series, and classic ASCII games.")
    print("\n To play, simply follow along as you go and enter commands as needed.")
    print(" The game will guide you as you progress, so please... adventure on!")
    print("\n If you find any bugs, please let me know by shooting me a message")
    print(" over Discord. My username is SaxyButters! I welcome all messages!")
    print("\n Console Quest RPG was developed by Hunter Reeves. All rights reserved.")
    MenuLine()

    ReturnToMainMenu()

def DeleteGame() -> None:
    """
    Deletes an existing saved game.
    """

    ClearConsole()

    DisplayDragon()

    saves_directory = "saves"

    if not os.path.exists(saves_directory) or not os.path.isdir(saves_directory):
        print("No saved games found.")
        return

    saved_games = [file for file in os.listdir(saves_directory) if os.path.isfile(os.path.join(saves_directory, file))]
    
    if not saved_games:
        return ""
    
    MenuLine()
    print(" * Select a save to delete (Enter 0 to cancel):")
    MenuLine()
    for idx, game in enumerate(saved_games, start = 1):
        save_name = os.path.splitext(game)[0]
        print(f" {idx}. {save_name}")
    MenuLine()

    try:
        choice = int(input(" > "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 < choice <= len(saved_games):
        selected_game = saved_games[choice - 1]
        MenuLine()
        print(f" * Are you sure you want to delete this save? (Y/N)")
        MenuLine()
        confirm = str(input(" > "))
        
        MenuLine()

        if confirm.lower() == 'y':
            file_path = os.path.join(saves_directory, selected_game)
            os.remove(file_path)
        elif confirm.lower() == 'n':
            return ""
        else:
            return ""
    else:
        return

def LoadGame() -> None:
    """
    Loads a saved character from a file.
    """

    saves_directory = 'saves\\'

    ClearConsole()
    DisplayDragon()

    save_files = [f for f in os.listdir(saves_directory) if f.endswith('.pkl')]

    if not save_files:
        MenuLine()
        print(" ^ Load Game")
        MenuLine()
        print(" No saved games found. You will need to start a new game.\n\n Please go back to the main menu to start a new game.")
        MenuLine()
        ReturnToMainMenu()
        return None

    MenuLine()
    print(" ^ Load Game")
    MenuLine()
    print(" * Choose a saved character to load:")
    MenuLine()
    for i, save_file in enumerate(save_files, start = 1):
        remove_pkl_from_name = os.path.splitext(save_file)[0]
        print(f" {i}. {remove_pkl_from_name}")

    while True:
        try:
            MenuLine()
            choice = int(input(" > "))
            if 0 <= choice <= len(save_files):
                break
            else:
                MenuLine()
                print(" * Invalid choice. Please enter a valid number.")
        except ValueError:
            MenuLine()
            print(" * Invalid input. Please enter a number.")

    selected_save_file = save_files[choice - 1]

    with open(os.path.join(saves_directory, selected_save_file), 'rb') as file:
        player = pickle.load(file)

    return player

def SaveGame(player: Player) -> None:
    """
    Saves the current player character to a file.
    
    Parameters:
        player (Player): The character that will be saved.
    """

    with open('saves\\' + player.name + '.pkl', 'wb') as file:
        pickle.dump(player, file)
        
def GetSex(name: str) -> str:
    """
    Prompts the user to select the player's sex.
    
    Parameters:
        name (string): Name of the player.
    
    Returns:
        sex (string): Sex of the player.
    """
    
    DisplayDragon()
    MenuLine()
    print(" ^ New Game")
    MenuLine()
    print(f" * {name}... what is your sex?")
    MenuLine()
    print(" 1. Male\n 2. Female")
    MenuLine()
    sex = input(" > ")
    if sex == '1':
        sex = 'Male'
    elif sex == '2':
        sex = 'Female'
    else:
        sex = 'Other'
    ClearConsole()
    
    return sex
        
def GetName() -> str:
    """
    Prompts the user to enter the player's name.
    
    Returns:
        name (string): Name of the player.
    """
    
    DisplayDragon()
    MenuLine()
    print(" ^ New Game")
    MenuLine()
    print(" * Enter thy name:")
    MenuLine()
    name = input(" > ")
    if name == "":
        name = 'Player'
    ClearConsole()
    
    return name

def NewGame() -> tuple[str, str, str, str, str, list]:
    """
    Initializes a new game with character attributes.
    
    Returns:
        tuple: A tuple containing the 
        character's name, sex, race, birth sign, class, and a list of attributes.
    """

    ClearConsole()
    
    name = GetName()
    sex = GetSex(name)
    
    race, attributes = SelectRace(name, DisplayPlanet, MenuLine)
    birth_sign, attributes = SelectBirthsign(name, attributes, DisplayStars, MenuLine)
    player_class, attributes = SelectClass(name, attributes, DisplayBattleAxe, MenuLine)

    return name, sex, race, birth_sign, player_class, attributes