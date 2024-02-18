'''
Class Name: Player.py
Description: Default Player class of which all other character classes inherit from.
Author: Hunter Reeves
Date: 2024-02-17
'''

class Player:
    def __init__(self, name, race, birth_sign, player_class, attributes):
        # Information from creation
        self.name = name
        self.race = race
        self.birth_sign = birth_sign
        self.player_class = player_class
        self.attributes = {attr: max(0, min(100, value)) for attr, value in attributes.items()}
        # Information after creation
        self.level = 1
        self.experience = 0
        self.next_experience = 100
        self.attribute_points = 0
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
        # For testing purposes
        self.physical_attack = round(1.0 + 10.5 * (self.attributes['Strength'] / 100) * (1 + 0.07 * self.level), 0)
        self.stamina_cost = max(8, round(40 * (1.4 - 0.012 * attributes['Endurance'] - 0.0005 * self.level), 0))
        self.magical_attack = round(1.0 + 10.5 * (self.attributes['Intelligence'] / 100) * (1 + 0.07 * self.level), 0)
        self.mana_cost = max(8, round(40 * (1.4 - 0.012 * attributes['Willpower'] - 0.0005 * self.level), 0))
        self.critical_hit = round(1.5 * (1 + self.attributes['Agility'] / 100) + self.physical_attack + 0.09 * self.level, 0)
        self.dodge_chance = round(self.attributes['Agility'] / 200 + 0.002 * self.level, 2)
        self.critical_chance = round(self.attributes['Agility'] / 400 + 0.002 * self.level, 2)

    def calculate_stat(self, attribute, level, multiplier = 2):
        """
            Handles the math for calculating starting health, mana, and stamina.
    
            Parameters:
                self (object): Player object
                attribute (str): Attribute being used for the current stat.
                multiplier (int): Multiplier for the math in the stat equation.
            
            Returns:
                (int): The stat being calculated.
        """

        return round(self.attributes[attribute] * (multiplier + level * 0.025) - 1, 0)