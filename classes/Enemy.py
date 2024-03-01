'''
Class Name: Enemy.py
Description: Default Enemy class of which all enemies will use.
Author: Hunter Reeves
Date: 2024-03-01
'''

import random

class Enemy:
    def __init__(self, player_level, threshold, player_location):
        self.types = ["Mercenary", "Imp", "Ogre", "Goblin", "Giant Crab", "Skeleton", "Bandit"]
        self.type = self.generate_enemy_type(player_location)
        self.level = self.generate_enemy_level(player_level, threshold)
        self.attribute_modifier = random.uniform(1.05, 1.10) + (self.level / 30)
        self.exp_modifier = random.uniform(1.30, 1.50) + (self.level / 4)
        self.gold_modifier = random.uniform(1.25, 1.75) + (self.level / 5)
        self.dropped_exp = round((random.uniform(30, 50) * self.exp_modifier), 0)
        self.dropped_gold = round((random.uniform(3, 5) * self.gold_modifier), 0)
        self.attributes = self.generate_enemy_attribute(self.type)
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
        self.defense_modifier = 100
        self.physical_attack = round(1.0 + 10.5 * (self.attributes['Strength'] / 100) * (1 + 0.07 * self.level), 0)
        self.magical_attack = round(1.0 + 10.5 * (self.attributes['Intelligence'] / 100) * (1 + 0.07 * self.level), 0)
        self.physical_defense = round(((self.attributes['Endurance'] * 2) / self.defense_modifier) + (0.2 * self.level), 0)
        self.magical_defense = round(((self.attributes['Willpower'] * 2) / self.defense_modifier) + (0.2 * self.level), 0)
        self.dodge_chance = round(self.attributes['Agility'] / 200 + 0.002 * self.level, 2)

    def generate_enemy_type(self, current_location):
        """
        Generates a unique enemy type based on the player's location.
    
        Parameters:
            self (object): The enemy.

        Returns:
            (str): The generated enemy name.
        """
        
        enemy_type_locations = {
            'Small Town': self.types[0],
            'Foggy Forest': self.types[1],
            'Desolate Cave': self.types[2],
            'Knoll Mountain': self.types[3],
            'Sandy Beach': self.types[4],
            'Abandoned Fort': self.types[5],
            'Sacked Camp': self.types[6]
        }

        return f"{enemy_type_locations.get(current_location, 'Enemy')}"

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
        
    def generate_enemy_attribute(self, enemy_type):
        """
            Determines the attributes of the enemy based on the type of enemy
    
            Parameters:
                self (object): Enemy object
            
            Returns:
                None.
        """

        enemy_type_attributes = {
            self.types[0]: {"Strength": 45, "Endurance": 35, "Intelligence": 45, "Willpower": 35, "Agility": 45, "Speed": 35},
            self.types[1]: {"Strength": 35, "Endurance": 35, "Intelligence": 45, "Willpower": 45, "Agility": 35, "Speed": 45},
            self.types[2]: {"Strength": 55, "Endurance": 55, "Intelligence": 30, "Willpower": 30, "Agility": 40, "Speed": 30},
            self.types[3]: {"Strength": 30, "Endurance": 30, "Intelligence": 55, "Willpower": 55, "Agility": 30, "Speed": 40},
            self.types[4]: {"Strength": 50, "Endurance": 50, "Intelligence": 30, "Willpower": 30, "Agility": 20, "Speed": 60},
            self.types[5]: {"Strength": 30, "Endurance": 30, "Intelligence": 50, "Willpower": 50, "Agility": 60, "Speed": 20},
            self.types[6]: {"Strength": 35, "Endurance": 45, "Intelligence": 35, "Willpower": 45, "Agility": 35, "Speed": 45}
        }

        attributes = enemy_type_attributes.get(enemy_type)
        modified_attributes = attributes

        for attribute, value in attributes.items():
            modified_attribute = round(value * self.attribute_modifier, 0)
            modified_attributes[attribute] = min(modified_attribute, 100)

        return modified_attributes

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