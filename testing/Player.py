'''
Class Name: Player.py
Description: Default Player class of which all other character Classes inherit from.
Author: Hunter Reeves
Date: 2024-02-14
'''

# Imports
import random

class Player:
    def __init__(self, name, race):
        # Define default, classless Player
        self.name = name
        self.race = race
        self.level = 1
        self.experience = 0
        self.next_level_experience = 100
        self.stats = {'Health': 100, 'Mana': 100, 'Stamina': 100}
        self.max_stats = {'Health': 100, 'Mana': 100, 'Stamina': 100}
        self.attributes = {'Strength': 50, 'Endurance': 50, 'Intelligence': 50, 'Willpower': 50, 'Agility': 50, 'Speed': 50}
        self.attribute_points = 0
        self.inventory = {'Gold': 250, 'Health Potion': 3, 'Mana Potion': 0, 'Stamina Potion': 0}
        self.quest_log = []
        self.location = None

    def display_status(self):
        # Print all Player information
        print(f"\n{self.name} the {self.race}:")
        print(f"Level: {self.level} ({self.experience}/{self.next_level_experience})")
        print("Stats:", self.stats)
        print("Attributes:", self.attributes)
        print("Inventory:", self.inventory)
        print("Quests:")
        for quest in self.quest_log:
            print(quest)

    def gain_experience(self, amount):
        # Add experience until Player level up
        self.experience += amount
        print(f"You gained {amount} experience points!")

        if self.experience >= self.next_level_experience:
            self.level_up()

    def level_up(self):
        # Level up the player and add attribute/stat points
        print("Congratulations! You leveled up!")
        self.level += 1
        self.experience = 0
        self.next_level_experience = round(self.next_level_experience * 1.18, 0)
        self.attribute_points += 5
        for stat in self.stats:
            # Default increase for stats
            increase = random.randint(1, 5)
            # Modified increases for stats based on attributes
            e_increase = round(increase * (self.attributes['Endurance'] * 0.15), 0)
            w_increase = round(increase * (self.attributes['Willpower'] * 0.15), 0)
            s_increase = round(increase * (self.attributes['Speed'] * 0.15), 0)
            # Increase stats based on attribute gains
            self.stats['Health'] += e_increase
            self.stats['Mana'] += w_increase
            self.stats['Stamina'] += s_increase
            self.max_stats['Health'] += e_increase
            self.max_stats['Mana'] += w_increase
            self.max_stats['Stamina'] += s_increase
            # Recover to full max for each upon level up
            self.stats[stat] = self.max_stats[stat]

        while self.attribute_points != 0:
            print("Attributes:", self.attributes)
            print("You have", self.attribute_points, "points left.")
            print('Select an attribute by entering the first letter.')
            attribute = input('> ')
            if attribute == 'S' or 's':
                self.attributes['Strength'] += 1
                self.attribute_points -= 1
            elif attribute == 'E' or 'e':
                self.attributes['Endurance'] += 1
                self.attribute_points -= 1
            elif attribute == 'I' or 'i':
                self.attributes['Intelligence'] += 1
                self.attribute_points -= 1
            elif attribute == 'W' or 'w':
                self.attributes['Willpower'] += 1
                self.attribute_points -= 1
            elif attribute == 'A' or 'a':
                self.attributes['Agility'] += 1
                self.attribute_points -= 1
            elif attribute == 'S' or 's':
                self.attributes['Speed'] += 1
                self.attribute_points -= 1
            else:
                print('Invalid option. Please enter the attribute to add a point to.')
                attribute = input('> ')

    def use_mana(self, cost):
        modified_cost = round((cost - (self.attributes['Intelligence'] * 0.15)), 0)
        if self.stats['Mana'] >= modified_cost:
            self.stats['Mana'] -= modified_cost
            return True
        else:
            print("Not enough mana!")
            return False

    def use_stamina(self, cost):
        modified_cost = round((cost - (self.attributes['Strength'] * 0.15)), 0)
        if self.stats['Stamina'] >= modified_cost:
            self.stats['Stamina'] -= modified_cost
            return True
        else:
            print("Not enough stamina!")
            return False
        
    def rest(self):
        recovery = random.randint(10, 20) + round((self.attributes['Speed'] * 0.15), 0)
        self.stats['Health'] = min(self.max_stats['Health'], self.max_stats['Health'] + recovery)
        self.stats['Mana'] = min(self.max_stats['Mana'], self.max_stats['Mana'] + recovery)
        self.stats['Stamina'] = min(self.max_stats['Stamina'], self.max_stats['Stamina'] + recovery)
        print("Health, Mana, and Stamina has been restored.")