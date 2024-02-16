'''
Class Name: Player.py
Description: Default Player class of which all other character classes inherit from.
Author: Hunter Reeves
Date: 2024-02-15
'''

class Player:
    def __init__(self, name, race, birth_sign, player_class, attributes):
        # Information from creation
        self.name = name
        self.race = race
        self.birth_sign = birth_sign
        self.player_class = player_class
        self.attributes = attributes
        # Information after creation
        self.stats = {'Health': self.attributes['Endurance'] * 2, 'Mana': self.attributes['Intelligence'] * 2, 'Stamina': self.attributes['Strength'] * 2}
        self.max_stats = {'Health': self.stats['Health'], 'Mana': self.stats['Mana'], 'Stamina': self.stats['Stamina']}
        self.level = 1
        self.experience = 0
        self.next_experience = 100
        
    def set_starting_health(endurance):
        """
        Sets the starting health for the Player
        
        Parameters:
            endurance (int): Value of Player's endurance

        Returns
            (int): The starting health for the Player
        """
        
        return endurance * 2
    
    def set_starting_mana(intelligence):
        """
        Sets the starting mana for the Player
        
        Parameters:
            intelligence (int): Value of Player's intelligence

        Returns
            (int): The starting mana for the Player
        """
        
        return intelligence * 2
    
    def set_starting_stamina(strength):
        """
        Sets the starting stamina for the Player
        
        Parameters:
            strength (int): Value of Player's strength

        Returns
            (int): The starting stamina for the Player
        """
        
        return strength * 2