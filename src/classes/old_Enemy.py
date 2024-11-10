'''
Default Enemy class that represents all enemies in the game.

This class defines the characteristics and behaviors of enemies, generating their 
types, attributes, stats, and loot based on the player's level, location, and 
game configuration. Each enemy instance will have unique attributes and combat 
capabilities, allowing for varied interactions during gameplay.

Key Features:
- Generates enemy type and level dynamically based on the player's situation.
- Calculates enemy attributes and stats, including health, mana, and stamina.
- Supports loot generation from external configuration files.
- Provides methods for displaying stats visually and managing enemy actions.
- Enables customization of enemy behaviors and interactions in the game.
'''

import random

class Enemy:
    """
    The Enemy class defines enemies in the game, generating their type, attributes, 
    stats, and loot based on the player's level, location, and game configuration.
    
    Attributes:
        types (list): List of possible enemy types.
        type (str): The type of the enemy generated based on the player's location.
        level (int): The level of the enemy based on the player's level and a threshold.
        attribute_modifier (float): Modifier to scale enemy attributes.
        exp_modifier (float): Modifier to scale experience dropped by the enemy.
        gold_modifier (float): Modifier to scale gold dropped by the enemy.
        dropped_exp (int): Experience points dropped by the enemy when defeated.
        dropped_gold (int): Gold dropped by the enemy when defeated.
        dropped_item (dict): Items dropped by the enemy, read from an external file.
        attributes (dict): Attribute values for the enemy (e.g., Strength, Endurance).
        description (str): A description of the enemy type.
        stats (dict): Current stats like Health, Mana, and Stamina.
        max_stats (dict): Maximum stats like Health, Mana, and Stamina.
        physical_attack (float): Physical attack value of the enemy.
        magical_attack (float): Magical attack value of the enemy.
        critical_hit (float): Critical hit chance of the enemy.
        physical_defense (float): Physical defense value of the enemy.
        magical_defense (float): Magical defense value of the enemy.
        stamina_cost (int): Stamina cost for the enemy's actions.
        mana_cost (int): Mana cost for the enemy's actions.
        dodge_chance (float): Chance for the enemy to dodge an attack.
        critical_chance (float): Chance for the enemy to land a critical hit.
    """

    def __init__(self, player_level, threshold, player_location):
        self.types = ["Mercenary", "Imp", "Ogre", "Goblin", "Giant Crab", "Skeleton", "Bandit"]
        self.type = self.generate_enemy_type(player_location)
        self.level = self.generate_enemy_level(player_level, threshold)
        self.attribute_modifier = random.uniform(1.05, 1.10) + (self.level / 30)
        self.exp_modifier = random.uniform(1.30, 1.50) + (self.level / 4)
        self.gold_modifier = random.uniform(1.25, 1.75) + (self.level / 5)
        self.dropped_exp = round((random.uniform(15, 30) * self.exp_modifier), 0)
        self.dropped_gold = round((random.uniform(2, 4) * self.gold_modifier), 0)
        self.dropped_item = self.read_drops_from_file('.\\config\\enemyDrops.txt')
        self.attributes = self.generate_enemy_attribute(self.type)
        self.description = self.type
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
        self.critical_hit = self.physical_attack + round(2.5 * ((self.attributes['Agility'] * 12) / 100) + 0.08 * self.level, 0)
        self.physical_defense = round(((self.attributes['Endurance'] * 2) / self.defense_modifier) + (0.2 * self.level), 0)
        self.magical_defense = round(((self.attributes['Willpower'] * 2) / self.defense_modifier) + (0.2 * self.level), 0)
        self.stamina_cost = max(8, round(15 * (1.4 - 0.012 * self.attributes['Endurance'] - 0.0005 * self.level), 0))
        self.mana_cost = max(8, round(30 * (1.4 - 0.012 * self.attributes['Willpower'] - 0.0005 * self.level), 0))
        self.dodge_chance = round(self.attributes['Agility'] / 200 + 0.002 * self.level, 2) - (player_level / 200)
        self.critical_chance = round(self.attributes['Agility'] / 400 + 0.002 * self.level, 2)

    def generate_enemy_type(self, current_location: str):
        """
        Generates a unique enemy type based on the player's location.
    
        Parameters:
            self (object): The enemy.
            current_location (str): Player's current location.

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

    def generate_enemy_level(self, player_level: int, threshold: int):
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
        
    def generate_enemy_attribute(self, enemy_type: str):
        """
            Determines the attributes of the enemy based on the type of enemy
    
            Parameters:
                self (object): Enemy object
                enemy_type (str): Type of enemy.
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

    def calculate_stat(self, attribute: str, level: int, multiplier: int = 1):
        """
            Handles the math for calculating starting health, mana, and stamina.
    
            Parameters:
                self (object): Enemy object
                attribute (str): Attribute being used for the current stat.
                level (int): Level of the player.
                multiplier (int): Multiplier for the math in the stat equation.
            
            Returns:
                (int): The stat being calculated.
        """
        
        return round(self.attributes[attribute] * (multiplier + level * 0.02) - 1, 0)

    def generate_stat_bar(self, current: int, maximum: int, length: int = 50, bar_color: str = 'white', bracket_color: str = 'white'):
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
            color_code = f"\033[1;{30 + list(('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')).index(bar_color)}m"
            bracket_color_code = f"\033[1;{30 + list(('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')).index(bracket_color)}m"
            stat_bar = f"{bracket_color_code}[{color_code}{'=' * bar_length}{' ' * (length - bar_length)}{bracket_color_code}]\033[0m"
            display = f"({current}/{maximum})".rjust(10)

            return stat_bar, display
    
    def read_drops_from_file(self, filename: str):
        """
            Takes the enemy drops from the file and determines the drops for the Player.
    
            Parameters:
                filename (str): The filename of the enemy drop information.
            
            Returns:
                drops (dict): All of the drop information from the enemy.
        """
        drops = {}
    
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                
                if len(parts) == 4:
                    enemy_type = parts[0].strip()
                    name = parts[1].strip()
                    min_count = int(parts[2].strip())
                    max_count = int(parts[3].strip())
                    
                    count = random.randint(min_count, max_count)
                    
                    if enemy_type == self.type:
                        drops[name] = {'type': enemy_type, 'name': name, 'count': count}
                        return drops
                    
            return drops