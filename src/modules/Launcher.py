'''
Main gameplay initialization and loop for Console Quest RPG.

This module handles the initialization of the game and the core gameplay loop. It manages:
- Displaying the main menu and handling user selection (New Game, Load Game, About, Quit).
- Starting a new game by creating a player with customizable attributes (name, race, class, etc.).
- Loading an existing game from a saved file.
- Running the main game loop, where the player can pause, explore, manage their stats, inventory, visit a shop, rest, etc.

This module is essential for the game's flow, connecting the main menu, game actions, and player interaction with the world.

Functions:
- InitializeGame: Sets up the main menu and handles user inputs to start or load a game.
- StartGame: Executes the core game loop, allowing the player to explore, view stats, manage inventory, and more.
- DisplayMenu: Shows the in-game menu with options for the player to choose from.
'''

from src.modules.MainMenu import MainMenu, PauseMenu
from src.modules.CoreGameFunctions import ConsoleInput, ClearConsole, ReturnToGame
from src.modules.GameActions import AboutGame, NewGame, SaveGame, LoadGame, DeleteGame
from src.modules.ArtAssets import DisplayPlanet, DisplayStars, DisplayDragon
from src.modules.TextFormatter import MenuLine
from src.modules.ShopHandler import ShopMenu
from src.modules.StatusBarHandler import UpdateStatusBar, UpdateExperienceBar
from src.modules.PlayerActions import ExploreLocation, PrintAllStats, RecoverStats

from src.classes.Player import Player # Change either to Player or old_Player

def DisplayMenu(player: Player) -> str:
    """
    Display the in-game menu.

    Parameters:
        player (Player): The character save file that the user goes through the game with.

    Returns:
        str: The user's input.
    """

    ClearConsole()
    MenuLine()
    print(f" ^ Welcome {player.name} the {player.sex} {player.race}!")
    MenuLine()
    print(f" - You are a Level {player.level} {player.player_class}, born under the {player.birth_sign} sign.")
    MenuLine()
    print(f" - Gold: {int(player.gold)}")
    MenuLine()
    print(f" - Current Location: {player.location}")
    MenuLine()

    UpdateStatusBar(player)
    MenuLine()
    UpdateExperienceBar(player)
    MenuLine()

    print(" * What would you like to do?")
    MenuLine()

    options = ["Pause Game", "Explore World", "View Stats", "View Inventory", "Visit Shop", "Rest"]

    for index, option in enumerate(options, 1):
        print(f" {index}. {option}")

    MenuLine()

    return ConsoleInput()

def StartGame(player: Player) -> None:
    """
    The main gameplay loop for Console Quest RPG.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
    """

    locations = ["Small Town", "Foggy Forest", "Desolate Cave", "Knoll Mountain", "Sandy Beach", "Abandoned Fort", "Sacked Camp"]
    encounter_rate = 0.67

    if player is None:
        return

    while player.stats['Health'] > 0:
        user_input = DisplayMenu(player)

        if user_input == '1':
            PauseMenu()
            user_input = ConsoleInput()

            if user_input == '1' or user_input == '2':
                SaveGame(player)

                if user_input == '2':
                    break
            elif user_input == '3':
                break
            elif user_input == '4':
                DeleteGame()
            else:
                ReturnToGame(user_input)
        elif user_input == '2':
            ClearConsole()
            DisplayPlanet()
            ExploreLocation(player, locations, encounter_rate)
        elif user_input == '3':
            PrintAllStats(player)
            print(" * Press enter to return to the game...")
            MenuLine()
            ConsoleInput()
        elif user_input == '4':
            ClearConsole()
            DisplayDragon()
            MenuLine()
            
            if not player.inventory:
                print(" ^ Your inventory is currently empty.")
            else:
                print(f" ^ {player.name}'s Inventory:")
                MenuLine()

                for item, details in player.inventory.items():
                    print(f" - {item} (x{details['count']})")
            MenuLine()
            print(" * Press enter to return to the game...")
            MenuLine()
            ConsoleInput()
        elif user_input == '5':
            ClearConsole()
            ShopMenu(player)
        elif user_input == '6':
            ClearConsole()
            DisplayStars()
            RecoverStats(player)
        # Debug command for giving experience
        elif user_input == '7':
            if player.level >= 50:
                player.experience = player.next_experience
            else:
                player.experience += 2500
                
            if player.experience >= player.next_experience:
                ClearConsole()
                player.LevelUp()
        # Debug command for giving max health, mana, and stamina
        elif user_input == '8':
            player.stats['Health'] = player.max_stats['Health']
            player.stats['Mana'] = player.max_stats['Mana']
            player.stats['Stamina'] = player.max_stats['Stamina']
        # Debug command for giving 100 gold
        elif user_input == 'g':
            player.gold += 100
        # Debug command for giving 99 of every enemy drop
        elif user_input == 'd':
            enemy_drops = ['Leather Strip', 'Imp Gall', 'Ogre Teeth', 'Rusted Metal', 'Chitin Claw', 'Old Bone', 'Faded Cloth']
    
            for item in enemy_drops:
                if item in player.inventory:
                    player.inventory[item]['count'] += 99
                else:
                    player.inventory[item] = {'count': 99}

        else:
            ReturnToGame(user_input)
    
def InitializeGame() -> None:
    """
    Initializes and handles the main menu for Console Quest RPG.
    """

    game_running = True

    while game_running:
        ClearConsole()
        MainMenu()
        print(" * Select an option from the menu above:")
        MenuLine()

        user_input = ConsoleInput()

        if user_input == '1':
            name, sex, race, birth_sign, player_class, attributes = NewGame()

            player_info = {
                'name': name,
                'sex': sex,
                'race': race,
                'birth_sign': birth_sign,
                'player_class': player_class,
                'attributes': attributes
            }

            player = Player(**player_info)

            StartGame(player)
        elif user_input == '2':
            player = LoadGame()
            StartGame(player)
        elif user_input == '3':
            AboutGame()
        elif user_input == '4':
            game_running = False