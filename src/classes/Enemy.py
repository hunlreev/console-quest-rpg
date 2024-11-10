'''
Base Enemy class that represents all enemies in the game.

This class defines the foundational characteristics and behaviors of enemies, generating
their attributes, stats, and loot based on the player's level and game configuration. 
Each enemy instance is dynamically generated with unique stats, combat capabilities, 
and modifiers, allowing for varied and challenging interactions during gameplay.

Key Features:
- Dynamically generates enemy level based on the player's level and a difficulty threshold.
- Calculates enemy attributes (e.g., Strength, Endurance, Agility) and corresponding combat stats like health, mana, stamina, physical/magical attack, and defense.
- Supports loot generation, including experience points (EXP) and gold rewards.
- Provides methods to calculate critical hits, attack power, defense, and action costs.
- Enables customization of enemy actions and interactions during combat.
'''

import random

class Enemy:
    """
    Base class for all enemy types in the game. This class provides common functionality 
    for generating enemy attributes, stats, and behaviors based on the player's level. 
    """

    enemy_types = [
        "Mercenary",
        "Imp", 
        "Ogre", 
        "Goblin", 
        "Giant Crab", 
        "Skeleton", 
        "Bandit"
    ]

    def __init__(self, player_level, threshold):
        self.type = self.RandomlySelectEnemyType()
        self.level = self.GenerateEnemyLevel(player_level, threshold)
        self.attribute_modifier = random.uniform(1.05, 1.10) + (self.level / 30)
        self.exp_modifier = random.uniform(1.30, 1.50) + (self.level / 4)
        self.gold_modifier = random.uniform(1.25, 1.75) + (self.level / 5)
        self.dropped_exp = self.CalculateDroppedExp()
        self.dropped_gold = self.CalculateDroppedGold()
        self.dropped_item = self.ReadDropsFromFile('.\\config\\enemyDrops.txt')
        self.attributes = self.GetAttributes(player_level)
        self.description = self.type
        self.stats = self.CalculateBaseStats()
        self.max_stats = self.stats.copy()
        self.defense_modifier = 100
        self.physical_attack = self.CalculateAttack("Strength", 10.5)
        self.magical_attack = self.CalculateAttack("Intelligence", 10.5)
        self.critical_hit = self.CalculateCriticalHit()
        self.physical_defense = self.CalculateDefense("Endurance")
        self.magical_defense = self.CalculateDefense("Willpower")
        self.stamina_cost = self.CalculateCost("Endurance", base = 15, scale = 1.4, per_level_scale = 0.012)
        self.mana_cost = self.CalculateCost("Willpower", base = 30, scale = 1.4, per_level_scale = 0.012)
        self.dodge_chance = self.CalculateDodgeChance(player_level)
        self.critical_chance = self.CalculateCriticalChance()

    def RandomlySelectEnemyType(self) -> str:
        """
        Randomly selects an enemy type from the list.

        The available enemy types include:
        - **Mercenary**: Skilled fighters for hire, often tactical in battle.
        - **Imp**: Small and mischievous creatures known for their agility and trickery.
        - **Ogre**: Large, brutish beings with immense strength, but often slow.
        - **Goblin**: Cunning and stealthy, goblins excel at ambush tactics.
        - **Giant Crab**: Terrifying creatures of the sea, known for their hard shells.
        - **Skeleton**: Animated remains of fallen warriors, wielding rusty weapons.
        - **Bandit**: Outlaws that attack travelers for loot, relying on numbers.

        Returns:
            str: The randomly selected Enemy type from the list of enemies.
        """

        return random.choice(self.enemy_types)

    def GenerateEnemyLevel(self, player_level: int, threshold: int) -> int:
        """
        Determines the enemy's level based on the player's level and a difficulty threshold.

        This method generates a random enemy level within a range that is influenced by the 
        player's current level and the specified threshold. The enemy's level is always at least 1, 
        and its upper bound is determined by the player's level plus the threshold, ensuring 
        that enemies remain challenging and balanced.

        Args:
            player_level (int): The current level of the player.
            threshold (int): The difficulty range for generating the enemy's level, with the level falling between (player_level - threshold) and (player_level + threshold).

        Returns:
            int: The randomly generated enemy level, with a minimum value of 1.
        """

        return max(1, random.randint(player_level - threshold, player_level + threshold))

    def CalculateStat(self, attribute: str, level: int, multiplier: int = 1) -> float:
        """
        Calculates a specific stat for the enemy based on the provided attribute, level, and optional multiplier.

        This method computes the value of an enemy's stat (e.g., Health, Mana, Stamina) 
        by scaling the attribute's base value with a formula that incorporates the enemy's 
        level and a configurable multiplier. The formula ensures that stats grow progressively 
        as the enemy's level increases, providing balanced stat scaling.

        Args:
            attribute (str): The name of the attribute to be used for calculating the stat (e.g., 'Strength', 'Endurance').
            level (int): The level of the enemy, used to scale the stat.
            multiplier (int, optional): A multiplier to further adjust the stat calculation. Defaults to 1.

        Returns:
            float: The calculated value of the stat, rounded to the nearest whole number.
        """

        return round(self.attributes[attribute] * (multiplier + level * 0.02) - 1, 0)

    def CalculateDroppedExp(self) -> float:
        """
        Calculates the amount of experience (EXP) dropped by the enemy upon defeat.

        This method generates a random value within a predefined range (15 to 30),
        then scales it by the enemy's experience modifier (`exp_modifier`). The result 
        is rounded to the nearest whole number to determine how much experience the player 
        will receive after defeating the enemy.

        Returns:
            float: The amount of experience dropped by the enemy, rounded to the nearest whole number.
        """

        return round(random.uniform(15, 30) * self.exp_modifier, 0)

    def CalculateDroppedGold(self) -> float:
        """
        Calculates the amount of gold dropped by the enemy upon defeat.

        This method generates a random value within a predefined range (2 to 4),
        then scales it by the enemy's gold modifier (`goldModifier`). The result 
        is rounded to the nearest whole number to determine how much gold the player 
        will receive after defeating the enemy.

        Returns:
            float: The amount of gold dropped by the enemy, rounded to the nearest whole number.
        """

        return round(random.uniform(2, 4) * self.gold_modifier, 0)

    def ReadDropsFromFile(self, filename: str) -> dict:
        """
        Takes the enemy drops from the file and determines the drops for the Player.

        This method opens a specified file containing information about possible drops for various enemy types. 
        It processes each line in the file to check if the enemy's type matches the type in the file, and if so, 
        randomly determines the quantity of each item within the specified range for that drop. If a match is 
        found, it returns a dictionary containing the items and quantities dropped by the enemy; otherwise, 
        an empty dictionary is returned.

        Args:
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

    def CalculateBaseStats(self) -> dict:
        """
        Calculates the base stats of the enemy based on its attributes and level.

        This method utilizes the `CalculateStat` method to determine the enemy's 
        base stats for Health, Mana, and Stamina. Each stat is calculated by 
        referencing the corresponding attribute ('Endurance', 'Intelligence', 
        and 'Strength') and the enemy's current level. The results are stored 
        in a dictionary for easy access.

        Returns:
            dict: A dictionary containing the base stats of the enemy, with keys 'Health', 'Mana', and 'Stamina', each mapped to their respective calculated values.
        """

        return {
            'Health': self.CalculateStat('Endurance', self.level),
            'Mana': self.CalculateStat('Intelligence', self.level),
            'Stamina': self.CalculateStat('Strength', self.level)
        }

    def CalculateAttack(self, attribute: str, base_damage: float) -> int:
        """
        Calculates the attack damage of the enemy based on a specified attribute.

        This method computes the total attack damage by taking a base damage value 
        and adjusting it according to the specified attribute's effectiveness and 
        the enemy's level. The calculation involves multiplying the base damage by 
        the attribute's percentage contribution and applying a level-based scaling factor.

        Args:
            attribute (str): The name of the attribute to use for the attack calculation.
            base_damage (float): The base damage value to adjust based on the attribute.

        Returns:
            int: The calculated attack damage, rounded to the nearest whole number.
        """

        return round(1.0 + base_damage * (self.attributes[attribute] / 100) * (1 + 0.07 * self.level), 0)

    def CalculateCriticalHit(self) -> int:
        """
        Calculates the critical hit damage for the enemy.

        This method computes the critical hit damage by taking the base physical attack 
        value and adding a calculated bonus based on the enemy's agility and level. 
        The agility factor contributes to the likelihood of scoring a critical hit, 
        enhancing the overall damage output.

        Returns:
            int: The calculated critical hit damage, rounded to the nearest whole number.
        """

        agilityFactor = (self.attributes['Agility'] * 12) / 100

        return round(self.physical_attack + 2.5 * agilityFactor + 0.08 * self.level, 0)

    def CalculateDefense(self, attribute: str) -> int:
        """
        Calculates the defense value for the enemy based on a specified attribute.

        This method computes the enemy's defense by using a specified attribute (e.g., 
        Endurance or Willpower) and a defense modifier. It adjusts the defense value 
        based on the enemy's level, ensuring that the resulting value is reasonable for combat.

        Args:
            attribute (str): The attribute used to calculate defense (e.g., 'Endurance').

        Returns:
            int: The calculated defense value, rounded to the nearest whole number.
        """

        return round(((self.attributes[attribute] * 2) / self.defense_modifier) + (0.2 * self.level), 0)

    def CalculateCost(self, attribute: str, base: int, scale: float, per_level_scale: float) -> int:
        """
        Calculates the cost of an action or ability based on a specified attribute.

        This method determines the cost for using an ability or action based on a 
        base cost, scaling factors, and the enemy's attribute values. It ensures that 
        the cost does not drop below a minimum threshold, allowing for manageable 
        resource expenditure during gameplay.

        Args:
            attribute (str): The attribute affecting the cost calculation.
            base (int): The base cost of the action or ability.
            scale (float): The scaling factor for the cost.
            per_level_scale (float): The scaling factor that decreases cost per level.

        Returns:
            int: The calculated cost, rounded to the nearest whole number, with a minimum value of 8.
        """

        cost = base * (scale - per_level_scale * self.attributes[attribute] - 0.0005 * self.level)
        
        return max(8, round(cost, 0))
    
    def CalculateDodgeChance(self, player_level: int) -> float:
        """
        Finds the chance the Enemy will successfully dodge the Player's attack.

        This method computes the probability that the Enemy will evade the Player's attack 
        based on the Enemy's agility attribute and level, adjusted by the Player's level. 
        The dodge chance is influenced by the ratio of the Enemy's agility and a base factor, 
        with a small level-based modifier to account for differences in combat experience. 
        Higher agility and level increase the dodge chance, while higher player level reduces it.

        Args:
            player_level (int): The current level of the Player.

        Returns:
            float: The Enemy's dodge chance when in combat with the Player.
        """

        return round(self.attributes['Agility'] / 200 + 0.002 * self.level, 2) - (player_level / 200)
    
    def CalculateCriticalChance(self) -> float:
        """
        Finds the chance the Enemy will successfully land a critical hit on the Player.

        Full description goes here.

        Returns:
            float: The Enemy's critical hit chance when in combat with the Player.
        """

        return round(self.attributes['Agility'] / 400 + 0.002 * self.level, 2)
    
    def GenerateStatBar(self, current: int, maximum: int, length: int = 50, bar_color: str = 'white', bracket_color: str = 'white') -> str:
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
    
    def GetAttributes(self, player_level: int) -> dict:
        """
        Retrieves the unique attributes for the enemy based on its type.

        This method checks the randomly selected enemy type and retrieves the 
        corresponding attributes from the predefined dictionary. Each enemy type has 
        unique strengths and weaknesses that affect their combat capabilities. If 
        the enemy type is None, a default attribute set is returned.

        The attributes are scaled based on the player's level, ensuring they do not exceed 100.

        Args:
            player_level (int): The level of the player, which influences the enemy's attributes.

        Returns:
            dict: A dictionary containing the attributes of the enemy, based on the enemy type.
        """

        initial_enemy_attributes = {
            "Mercenary": {"Strength": 45, "Endurance": 35, "Intelligence": 45, "Willpower": 35, "Agility": 45, "Speed": 35},
            "Imp": {"Strength": 35, "Endurance": 35, "Intelligence": 45, "Willpower": 45, "Agility": 35, "Speed": 45},
            "Ogre": {"Strength": 55, "Endurance": 55, "Intelligence": 30, "Willpower": 30, "Agility": 40, "Speed": 30},
            "Goblin": {"Strength": 30, "Endurance": 30, "Intelligence": 55, "Willpower": 55, "Agility": 30, "Speed": 40},
            "Giant Crab": {"Strength": 50, "Endurance": 50, "Intelligence": 30, "Willpower": 30, "Agility": 20, "Speed": 60},
            "Skeleton": {"Strength": 30, "Endurance": 30, "Intelligence": 50, "Willpower": 50, "Agility": 60, "Speed": 20},
            "Bandit": {"Strength": 35, "Endurance": 45, "Intelligence": 35, "Willpower": 45, "Agility": 35, "Speed": 45}
        }

        base_attributes = initial_enemy_attributes.get(self.type, {
            'Strength': 25,
            'Endurance': 25,
            'Intelligence': 25,
            'Willpower': 25,
            'Agility': 25,
            'Speed': 25
        })

        scaling_factor = 0.6

        scaled_attributes = {
            attribute: min(int(value + (player_level * scaling_factor)), 100)
            for attribute, value in base_attributes.items()
        }

        return scaled_attributes