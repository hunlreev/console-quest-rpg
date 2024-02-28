'''
Class Name: Enemy.py
Description: Default Enemy class of which all enemies will use.
Author: Hunter Reeves
Date: 2024-02-27
'''

# Imports
import random

class Enemy:
    def __init__(self, player_level, threshold, player_location):
        # Information about an enemy
        self.name = self.generate_enemy_name(player_location)
        self.level = self.generate_enemy_level(player_level, threshold)
        self.modifier = random.uniform(1.30, 1.50) + (self.level / 25)
        self.dropped_exp = round((random.uniform(30, 50) * self.modifier), 0)
        self.dropped_gold = round((random.uniform(3, 5) * self.modifier), 0)
        # Use a dictionary to store random values for attributes
        self.attributes = {
            'Strength': min(round(random.uniform(20, 40) * self.modifier, 0), 100),
            'Endurance': min(round(random.uniform(20, 40) * self.modifier, 0), 100),
            'Intelligence': min(round(random.uniform(20, 40) * self.modifier, 0), 100),
            'Willpower': min(round(random.uniform(20, 40) * self.modifier, 0), 100),
            'Agility': min(round(random.uniform(20, 40) * self.modifier, 0), 100),
            'Speed': min(round(random.uniform(20, 40) * self.modifier, 0), 100)
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
        # Fighting statistics
        self.defense_modifier = 100
        self.physical_attack = round(1.0 + 10.5 * (self.attributes['Strength'] / 100) * (1 + 0.07 * self.level), 0)
        self.magical_attack = round(1.0 + 10.5 * (self.attributes['Intelligence'] / 100) * (1 + 0.07 * self.level), 0)
        self.physical_defense = round(((self.attributes['Endurance'] * 2) / self.defense_modifier) + (0.2 * self.level), 0)
        self.magical_defense = round(((self.attributes['Willpower'] * 2) / self.defense_modifier) + (0.2 * self.level), 0)
        self.dodge_chance = round(self.attributes['Agility'] / 200 + 0.002 * self.level, 2)

    def generate_enemy_name(self, current_location):
        """
        Generates a unique enemy name based on the player's location.
    
        Parameters:
            self (object): The enemy.

        Returns:
            (str): The generated enemy name.
        """
        
        enemy_names = {
            'Small Town': 'Mercenary',
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

    def calculate_stat(self, attribute, level, multiplier = 1):
        """
            Handles the math for calculating starting health, mana, and stamina.
    
            Parameters:
                self (object): Enemy object
                attribute (str): Attribute being used for the current stat.
                multiplier (int): Multiplier for the math in the stat equation.
            
            Returns:
                (int): The stat being calculated.
        """
        
        return round(self.attributes[attribute] * (multiplier + level * 0.01) - 1, 0)

    def generate_stat_bar(self, current, maximum, length = 46):
        """
            Display stats in a bar.
    
            Parameters:
                self (object): Enemy object
                current (int): Value of the current stat
                maximum (int): Value of the max stat
                length (int): Length of the stat bar
            
            Returns:
                stat_bar (str): The stat bar
                display (str): Stat in parathesis for actual value viewing
        """

        bar_length = int(length * (current / maximum))
        stat_bar = f"[{'=' * bar_length}{' ' * (length - bar_length)}]"
        display = f"({current}/{maximum})".rjust(10)

        return stat_bar, display