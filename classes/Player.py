'''
Class Name: Player.py
Description: Default Player class of which all other character classes inherit from.
Author: Hunter Reeves
Date: 2024-02-15
'''

class Player:
    def __init__(self, name, race, birth_sign, attributes):
        # Information from creation
        self.name = name
        self.race = race
        self.birth_sign = birth_sign
        self.attributes = attributes
        # Information after creation
        self.stats = {'Health': 100, 'Mana': 100, 'Stamina': 100}
        self.max_stats = {'Health': 100, 'Mana': 100, 'Stamina': 100}
        self.level = 1
        self.experience = 0
        self.next_experience = 100