'''
Class Name: Enemy.py
Description: Default Enemy class of which all enemies will use.
Author: Hunter Reeves
Date: 2024-02-22
'''

# Imports
import random

class Enemy:
    def __init__(self, player_level, threshold, player_location):
        # Information about an enemy
        self.name = self.generate_enemy_name(player_location)
        self.level = self.generate_enemy_level(player_level, threshold)
        # Use a dictionary to store random values for attributes
        self.attributes = {
            'Strength': round(random.uniform(25 * player_level, 45 * player_level), 0),
            'Endurance': round(random.uniform(25 * player_level, 45 * player_level), 0),
            'Intelligence': round(random.uniform(25 * player_level, 45 * player_level), 0),
            'Willpower': round(random.uniform(25 * player_level, 45 * player_level), 0),
            'Agility': round(random.uniform(25 * player_level, 45 * player_level), 0),
            'Speed': round(random.uniform(25 * player_level, 45 * player_level), 0)
        }
        # Use a dictionary to store random values for health, mana, and stamina
        self.stats = {
            'Health': self.calculate_stat('Endurance', self.level),
            'Mana': self.calculate_stat('Intelligence', self.level),
            'Stamina': self.calculate_stat('Strength', self.level)
        }
        self.max_stats = {
            'Health': self.stats['Health'],
            'Mana': self.stats['Mana'],
            'Stamina': self.stats['Stamina']
        }

    def generate_enemy_name(self, current_location):
        """
        Generates a unique enemy name based on the player's location.
    
        Parameters:
            self (object): The enemy.

        Returns:
            (str): The generated enemy name.
        """
        
        enemy_names = {
            'Small Town': 'Challenger',
            'Foggy Forest': 'Imp',
            'Desolate Cave': 'Ogre',
            'Knoll Mountain': 'Goblin',
            'Sandy Beach': 'Giant Crab',
            'Abandoned Fort': 'Skeleton',
            'Sacked Camp': 'Bandit',
        }

        return f"{enemy_names.get(current_location, 'Enemy')}"

    def generate_enemy_level(self, player_level, threshold):
        """
            Determines the level of the enemy.
    
            Parameters:
                self (object): The enemy.
                player_level (int): Level of the player.
                threshold (int): Plus or minus threhold to determine enemy level.
            
            Returns:
                (int): The level of the enemy.
        """
        
        if player_level < threshold:
            return 1
        else:
            return random.randint(max(1, player_level - threshold), player_level + threshold)

    def calculate_stat(self, attribute, level, multiplier = 2):
        """
            Handles the math for calculating starting health, mana, and stamina.
    
            Parameters:
                self (object): Enemy object
                attribute (str): Attribute being used for the current stat.
                multiplier (int): Multiplier for the math in the stat equation.
            
            Returns:
                (int): The stat being calculated.
        """

        return round(self.attributes[attribute] * (multiplier + level * 0.025) - 1, 0)