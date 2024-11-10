'''
Handles all functionality regarding an enemy encounter in the game.

This module manages the combat mechanics, including player and enemy actions,
such as melee attacks, spell casting, dodging, and running away during encounters. 
It also tracks health, mana, and stamina changes, and handles the outcome of 
the encounters.

Functions:
- CheckDodge: Determines if an attack was dodged based on the attacker's dodge chance.
- RunAway: Evaluates the possibility of escaping from an encounter based on speed.
- CastSpell: Executes spell casting logic, including mana checks, critical hits, and dodging.
- MeleeAttack: Manages melee attack logic, considering stamina, critical hits, and dodging.
- EnemyDecides: Simulates enemy actions during combat based on random selection.
- PlayerDecides: Processes player actions during combat based on user input.
- StartEncounter: Initiates the enemy encounter, managing turns, health updates, and the resolution of the encounter outcome.
'''

from src.modules.MainMenu import ConsoleInput, ClearConsole
from src.modules.GameActions import SaveGame
from src.modules.ArtAssets import DisplayPlanet, DisplayStars, DisplayBattleAxe, DisplaySkull
from src.modules.TextFormatter import MenuLine
from src.modules.StatusBarHandler import UpdateStatusBar, UpdateEnemyHealthBar
from src.modules.CoreGameFunctions import ReturnToGame

from src.classes.Player import Player # Change either to Player or old_Player
from src.classes.Enemy import Enemy

import time
import random

def CheckDodge(attacker, dodge_threshold: float) -> bool:
    """
    Determines if an attack was dodged based on the attacker's dodge chance.

    Parameters:
        attacker (Player or Enemy): The character or enemy attacking.
        dodge_threshold (float): To check if a dodge is executed or not.

    Returns:
        bool (bool): Check if dodge happened or not.
    """

    if dodge_threshold < attacker.dodge_chance:
        return True
    else:
        return False

def RunAway(attacker, defender) -> None:
    """
    Evaluates the possibility of escaping from an encounter based on speed.

    Parameters:
        attacker (Player or Enemy): The character or enemy attacking.
        defender (Player or Enemy): The character or enemy being attacked.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    if attacker.attributes['Speed'] > defender.attributes['Speed']:
        return "Run away!"
    else:
        return f" - Oh no, you are too slow! You cannot run from this {defender.description}."

def CastSpell(attacker, defender) -> str:
    """
    Executes spell casting logic, including mana checks, critical hits, and dodging.

    Parameters:
        attacker (Player or Enemy): The character or enemy attacking.
        defender (Player or Enemy): The character or enemy being attacked.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    crit_threshold = round(random.random(), 2)
    dodge_threshold = round(random.random(), 2)

    spell_damage = max(0, attacker.magical_attack - defender.magical_defense)
    critical_damage = attacker.critical_hit

    if attacker.stats['Mana'] < attacker.mana_cost:
        return f" - {attacker.description} doesn't have enough mana to cast a spell right now!"

    if crit_threshold < attacker.critical_chance:
        defender.stats['Health'] -= attacker.critical_hit
        attacker.stats['Mana'] -= attacker.mana_cost
        return f" - {attacker.description} landed a critical hit, dealing {critical_damage} damage!"

    if CheckDodge(attacker, dodge_threshold):
        return f" - {defender.description} dodged the {attacker.description}'s spell!"

    defender.stats['Health'] -= max(0, attacker.magical_attack - defender.magical_defense)
    attacker.stats['Mana'] -= attacker.mana_cost
    return f" - {attacker.description} casted a spell at the {defender.description}, dealing {spell_damage} damage!"

def MeleeAttack(attacker, defender) -> str:
    """
    Manages melee attack logic, considering stamina, critical hits, and dodging.

    Parameters:
        attacker (Player or Enemy): The character or enemy attacking.
        defender (Player or Enemy): The character or enemy being attacked.

    Returns:
        message (str): A dynamic message for displaying additional information.
    """

    crit_threshold = round(random.random(), 2)
    dodge_threshold = round(random.random(), 2)

    melee_damage = max(0, attacker.physical_attack - defender.physical_defense)
    critical_damage = attacker.critical_hit

    if attacker.stats['Stamina'] < attacker.stamina_cost:
        weakened_damage = max(0, attacker.physical_attack * 0.75 - defender.physical_defense)
        defender.stats['Health'] -= weakened_damage
        return f" - {attacker.description} doesn't have enough stamina, only dealing {weakened_damage} damage!"

    if crit_threshold < attacker.critical_chance:
        defender.stats['Health'] -= attacker.critical_hit
        attacker.stats['Stamina'] -= attacker.stamina_cost
        return f" - {attacker.description} landed a critical hit, dealing {critical_damage} damage!"

    if CheckDodge(attacker, dodge_threshold):
        return f" - {defender.description} dodged the {attacker.description}'s attack!"
    
    defender.stats['Health'] -= melee_damage
    attacker.stats['Stamina'] -= attacker.stamina_cost
    return f" - {attacker.description} attacked the {defender.description}, dealing {melee_damage} damage!"
    
def EnemyDecides(enemy: Enemy, player: Player) -> str:
    """
    Simulates enemy actions during combat based on random selection.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        enemy (Enemy): The current enemy in the encounter.
        user_input (string): Option the player selected in the previous menu.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    message = ""
    options = ['1', '2']
    random_selection = random.choice(options)

    if random_selection == options[0]:
        message = MeleeAttack(enemy, player)
    elif random_selection == options[1]:
        message = CastSpell(enemy, player)
    
    return message

def PlayerDecides(player: Player, enemy: Enemy, user_input: str) -> str:
    """
    Processes player actions during combat based on user input.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        enemy (Enemy): The current enemy in the encounter.
        user_input (string): Option the player selected in the previous menu.

    Returns:
        message (str): A dynamic message for displaying additional information
    """

    message = ""

    if user_input == '1':
        message = MeleeAttack(player, enemy)
    elif user_input == '2':
        message = CastSpell(player, enemy)
    elif user_input == '3':
        message = RunAway(player, enemy)
    # Debug - for instant killing enemies so I can test my code
    elif user_input == '4':
        message = "Debug"
        enemy.stats['Health'] -= 1000
    
    return message

def StartEncounter(player: Player, message: str) -> None:
    """
    Initiates the enemy encounter, managing turns, health updates, and the resolution of the encounter outcome.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
        message (str): A message that displays when updated.
    """

    def return_to_main_menu_countdown(seconds):
        import sys
        
        for i in range(seconds, 0, -1):
            sys.stdout.write(f"\r ^ Returning to main menu in: {i}")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r ^ Returning to main menu in: 0\n")
        sys.stdout.flush()

    def determine_enemy_drop():
        for item_name, item_info in enemy.dropped_item.items():
            item_name = item_info['name']
            item_count = item_info['count']
            
            if item_count <= 0:
                continue
            
            print(f" - You looted {item_count} {item_name}.")
            
            if item_name in player.inventory:
                player.inventory[item_name]['count'] += item_count
            else:
                player.inventory[item_name] = {'count': item_count}
        
    enemy = Enemy(player.level, 2)
    turn_counter = 1
    
    if player.attributes['Speed'] >= enemy.attributes['Speed']:
        isPlayerTurn = True
    else:
        isPlayerTurn = False

    while player.stats['Health'] > 0:
        ClearConsole()
        DisplayBattleAxe()
        MenuLine()
        print(f" ^ You encountered a Level {enemy.level} {enemy.type} at {player.location}!")
        MenuLine()
        UpdateEnemyHealthBar(enemy)
        MenuLine()
        UpdateStatusBar(player)
        MenuLine()
        
        if message != "":
            print(message)
            MenuLine()
            
        if turn_counter % 2 == 1 and isPlayerTurn:
            isPlayerTurn = False
            print(" * What would you like to do?")
            MenuLine()
            print(" 1. Attack\n 2. Cast Spell\n 3. Run Away")
            MenuLine()
            user_input = ConsoleInput()
            message = PlayerDecides(player, enemy, user_input)
        elif turn_counter % 2 == 0 and not isPlayerTurn:
            isPlayerTurn = True
            print(f" * {enemy.type} is making a decision...")
            MenuLine()
            time.sleep(3)
            message = EnemyDecides(enemy, player)

        turn_counter += 1 
        
        mana_recovery = round(player.attributes['Willpower'] * 0.03, 2)
        stamina_recovery = round(player.attributes['Endurance'] * 0.03, 2)
        
        player_mana = player.stats['Mana']
        player_stamina = player.stats['Stamina']
        
        mana_difference = player.max_stats['Mana'] - player.stats['Mana']
        stamina_difference = player.max_stats['Stamina'] - player.stats['Stamina']
                
        player.stats['Mana'] += mana_recovery if player_mana + mana_recovery <= player.max_stats['Mana'] else mana_difference
        player.stats['Stamina'] += stamina_recovery if player_stamina + stamina_recovery <= player.max_stats['Stamina'] else stamina_difference
        
        if message == "Run away!":
            ClearConsole()
            DisplayPlanet()
            MenuLine()
            print(f" ^ You managed to run away from the {enemy.type}!")
            MenuLine()
            time.sleep(3)
            break
        
        if player.stats['Health'] <= 0:
            player.total_deaths += 1
            player.max_stats['Health'] -= 1
            player.max_stats['Mana'] -= 1
            player.max_stats['Stamina'] -= 1
            health_penalty = round(player.max_stats['Health'] * 0.10, 2)
            player.stats['Health'] = max(health_penalty, 1)
            player.experience -= round(player.experience * 0.5, 2)
            SaveGame(player)
            ClearConsole()
            DisplaySkull()
            MenuLine()
            print(f" ^ The {enemy.type} killed you! You have lost some progress as a result.")
            MenuLine()
            return_to_main_menu_countdown(5)
            break

        if enemy.stats['Health'] <= 0:
            player.total_kills += 1
            ClearConsole()
            DisplayStars()
            MenuLine()
            print(f" ^ You defeated the {enemy.type}!")
            MenuLine()
            level_cap = 50

            if player.level < level_cap:
                print(f" - You have earned {int(enemy.dropped_exp)} experience.")
                player.experience += enemy.dropped_exp
                
            print(f" - You looted {int(enemy.dropped_gold)} gold.")
            determine_enemy_drop()
            MenuLine()
            player.gold += enemy.dropped_gold
            time.sleep(4)

            if player.experience >= player.next_experience and player.level < level_cap:
                ClearConsole()
                player.level_up()
            break

    ReturnToGame(user_input)