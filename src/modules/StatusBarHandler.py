'''
Management of player and enemy stat bars for combat and experience tracking.

This module is responsible for updating and displaying the health and experience bars for both players and enemies during gameplay. It manages:
- Updating the enemy health bar to reflect current health during combat encounters.
- Displaying the player's experience bar, indicating progress toward the next level.
- Building and displaying the player's health, mana, and stamina bars, providing an at-a-glance view of their current stats.

This module is essential for enhancing gameplay feedback by visually representing character and enemy states, helping players make strategic decisions during encounters.

Functions:
- UpdateEnemyHealthBar: Generates and displays the current health status of an enemy during combat.
- UpdateExperienceBar: Displays the player's experience status, showing how close they are to leveling up.
- UpdateStatusBar: Updates and displays the player's health, mana, and stamina, giving a complete overview of their current stats.
'''

from src.classes.Player import Player
from src.classes.Enemy import Enemy

def UpdateEnemyHealthBar(enemy: Enemy) -> None:
    """
    Generates and displays the current health status of an enemy during combat.

    Parameters:
        enemy (object): The enemy.
    """

    health_bar, health_display = enemy.generate_stat_bar(enemy.stats['Health'], enemy.max_stats['Health'], 50, 'red')
    
    print(f" -  HP: {health_bar} " + health_display)

def UpdateExperienceBar(player: Player) -> None:
    """
    Displays the player's experience status, showing how close they are to leveling up.

    Parameters:
        player (object): The player character.
    """

    bar_length = 46
    
    exp_bar, exp_display = player.generate_exp_bar(round(player.experience, 2), round(player.next_experience, 2), bar_length, 'yellow')

    print(f" - EXP: {exp_bar} " + exp_display)

def UpdateStatusBar(player: Player) -> None:
    """
    Updates and displays the player's health, mana, and stamina, giving a complete overview of their current stats.

    Parameters:
        player (object): The player character.
    """

    bar_length = 50
    
    health_bar, health_display = player.generate_stat_bar(round(player.stats['Health'], 2), round(player.max_stats['Health'], 2), bar_length, 'red')
    mana_bar, mana_display = player.generate_stat_bar(round(player.stats['Mana'], 2), round(player.max_stats['Mana'], 2), bar_length, 'blue')
    stamina_bar, stamina_display = player.generate_stat_bar(round(player.stats['Stamina'], 2), round(player.max_stats['Stamina'], 2),bar_length, 'green')

    print(f" -  HP: {health_bar} " + health_display)
    print(f" -  MP: {mana_bar} " + mana_display)
    print(f" -  SP: {stamina_bar} " + stamina_display)