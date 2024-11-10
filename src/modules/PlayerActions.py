'''
Management of player actions during core gameplay.

This module handles various player actions while navigating the main gameplay loop, including:
- Recovering player stats during resting periods, influenced by player speed.
- Displaying the player's current stats, providing a comprehensive overview of their progress and abilities.
- Allowing players to explore randomly selected locations, potentially triggering combat encounters based on a specified encounter rate.

This module is crucial for enhancing player interaction and engagement, as it facilitates essential actions that influence the player's journey and character development.

Functions:
- RecoverStats: Manages the resting process for the player, updating health and stamina based on speed and providing descriptive feedback.
- PrintAllStats: Displays the player's current statistics, including attributes, attack and defense values, and kill/death ratio.
- ExploreLocation: Enables the player to explore a random location, determining whether an encounter occurs based on the encounter rate.
'''

from src.modules.MainMenu import ClearConsole
from src.modules.ArtAssets import DisplayStars
from src.modules.TextFormatter import MenuLine
from src.modules.CombatEncounter import StartEncounter
from src.modules.CoreGameFunctions import ReturnToGame

from src.classes.Player import Player # Change either to Player or old_Player

import time
import random

def RecoverStats(player: Player) -> None:
    """
    Manages the resting process for the player, updating health and stamina based on speed and providing descriptive feedback.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
    """

    seconds_to_wait = player.Rest()

    MenuLine()

    speed = player.attributes['Speed']
    
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

    MenuLine()

    time.sleep(seconds_to_wait)

def PrintAllStats(player: Player) -> None:
    """
    Displays the player's current statistics, including attributes, attack and defense values, and kill/death ratio.

    Parameters:
        player (object): The player
    """

    no_deaths = 0

    ClearConsole()
    DisplayStars()
    MenuLine()
    print(f" ^ {player.name}'s Stats")
    MenuLine()
    print(f" - Available Attribute Points: {player.attribute_points}")
    MenuLine()
    print(f" - Strength: {player.attributes['Strength']}")
    print(f" - Endurance: {player.attributes['Endurance']}")
    print(f" - Intelligence: {player.attributes['Intelligence']}")
    print(f" - Willpower: {player.attributes['Willpower']}")
    print(f" - Agility: {player.attributes['Agility']}")
    print(f" - Speed: {player.attributes['Speed']}")
    MenuLine()
    print(f" - Physical attack: {player.physical_attack}")
    print(f" - Magical attack: {player.magical_attack}")
    MenuLine()
    print(f" - Physical defense: {player.physical_defense}")
    print(f" - Magical defense: {player.magical_defense}")
    MenuLine()
    print(f" - Enemies Killed: {player.total_kills}")
    print(f" - Number of Deaths: {player.total_deaths}")

    # Determine KD Ratio
    if player.total_deaths == no_deaths:
        kill_death_ratio = "N/A"
    else:
        kill_death_ratio = round(player.total_kills / player.total_deaths, 1)

    print(f" - Kill/Death Ratio: {kill_death_ratio}")
    MenuLine()

def ExploreLocation(player: Player, locations: list, encounter_rate: float) -> None:
    """
    Enables the player to explore a random location, determining whether an encounter occurs based on the encounter rate.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        locations (List): A list of locations for the player to explore.
        encounter_rate (Float): A value from 0 to 1 that describes the encounter rate.
    """
    
    player.location = random.choice(locations)
    exploration_time = random.choice([(1, "a quick adventure"), (2, "a short, nearby exploration"), (3, "a long journey"), (4, "huge campaign and get lost")])
    message = ""
    encounter_roll = random.random()

    MenuLine()
    print(f" - You set out for {exploration_time[1]}...")
    MenuLine()

    time.sleep(exploration_time[0])

    if encounter_roll < encounter_rate:
        StartEncounter(player, message)
    else:
        ReturnToGame("")