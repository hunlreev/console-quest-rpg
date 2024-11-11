'''
Base Player class that represents the player character throughout the game.

The Player class models all aspects of the player's character, providing foundational functionality
and data management needed to represent the player’s identity, attributes, and progress throughout
the game. This class includes methods for calculating derived statistics, such as attack and defense
values, experience points, and level progression, while providing convenient tools for resource
management, inventory handling, and ability usage.

Key Features:
- Player Initialization: Automatically applies base values for the player's stats, experience, and location, as well as customized attributes, such as race, class, and birth sign.
- Attribute Scaling and Limits: Supports attribute-based scaling for health, mana, stamina, attack, and defense, with caps set at 100 to maintain game balance.
- Dynamic Stat Calculation: Provides calculations for key stats such as physical/magical attacks, defenses, critical hits, and resource costs, all scaled to the player’s level and attributes.
- Leveling System: Tracks experience, handles level-up events, and allows allocation of new attribute points.
- Combat and Interaction: Includes attack and defense mechanics, dodge, and critical hit chances, all influenced by the player's stats.
- Inventory and Resource Management: Manages gold, items, and other resources, offering methods to add or remove items and display character data.
'''

from src.modules.MainMenu import MenuLine
from src.modules.CoreGameFunctions import ConsoleInput, ClearConsole
from src.modules.ArtAssets import DisplayStars

import random
import time

class Player:
    """
    Base class for all Player characters in the game. This class provides common functionality 
    for generating player attributes, stats, and behaviors based on the player's level. 
    """

    def __init__(self, name, sex, race, birth_sign, player_class, attributes):
        self.name = name
        self.sex = sex
        self.race = race
        self.birth_sign = birth_sign
        self.player_class = player_class
        self.attributes = {attr: max(0, min(100, value)) for attr, value in attributes.items()}
        self.level = 1
        self.experience = 0
        self.next_experience = 100
        self.attribute_points = 0
        self.gold = 0
        self.location = "Small Town"
        self.description = self.player_class
        self.total_kills = 0
        self.total_deaths = 0
        self.inventory = {}
        self.stats = self.CalculateBaseStats()
        self.max_stats = self.stats.copy()
        self.defense_modifier = 100
        self.physical_attack = self.CalculateAttack("Strength", 10.5)
        self.magical_attack = self.CalculateAttack("Intelligence", 10.5)
        self.critical_hit = self.CalculateCriticalHit()
        self.physical_defense = self.CalculateDefense("Endurance")
        self.magical_defense = self.CalculateDefense("Willpower")
        self.stamina_cost = self.CalculateCost("Endurance", base = 15, scale = 1.2, per_level_scale = 0.012)
        self.mana_cost = self.CalculateCost("Willpower", base = 35, scale = 1.6, per_level_scale = 0.008)
        self.dodge_chance = self.CalculateDodgeChance()
        self.critical_chance = self.CalculateCriticalChance()

    def CalculateStat(self, attribute: str, level: int, multiplier: int = 2) -> float:
        """
        Calculates a specific stat for the player based on the provided attribute, level, and optional multiplier.

        This method computes the value of an player's stat (e.g., Health, Mana, Stamina) 
        by scaling the attribute's base value with a formula that incorporates the player's 
        level and a configurable multiplier. The formula ensures that stats grow progressively 
        as the player's level increases, providing balanced stat scaling.

        Args:
            attribute (str): The name of the attribute to be used for calculating the stat (e.g., 'Strength', 'Endurance').
            level (int): The level of the player, used to scale the stat.
            multiplier (int, optional): A multiplier to further adjust the stat calculation. Defaults to 1.

        Returns:
            float: The calculated value of the stat, rounded to the nearest whole number.
        """

        return round(self.attributes[attribute] * (multiplier + level * 0.025) - 1, 0)

    def CalculateBaseStats(self) -> dict:
        """
        Calculates the base stats of the player based on their attributes and level.

        This method utilizes the `CalculateStat` method to determine the player's 
        base stats for Health, Mana, and Stamina. Each stat is calculated by 
        referencing the corresponding attribute ('Endurance', 'Intelligence', 
        and 'Strength') and the player's current level. The results are stored 
        in a dictionary for easy access.

        Returns:
            dict: A dictionary containing the base stats of the player, with keys 'Health', 'Mana', and 'Stamina', each mapped to their respective calculated values.
        """

        return {
            'Health': self.CalculateStat('Endurance', self.level),
            'Mana': self.CalculateStat('Intelligence', self.level),
            'Stamina': self.CalculateStat('Strength', self.level)
        }
    
    def CalculateAttack(self, attribute: str, base_damage: float) -> int:
        """
        Calculates the attack damage of the player based on a specified attribute.

        This method computes the total attack damage by taking a base damage value 
        and adjusting it according to the specified attribute's effectiveness and 
        the player's level. The calculation involves multiplying the base damage by 
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
        Calculates the critical hit damage for the player.

        This method computes the critical hit damage by taking the base physical attack 
        value and adding a calculated bonus based on the player's agility and level. 
        The agility factor contributes to the likelihood of scoring a critical hit, 
        enhancing the overall damage output.

        Returns:
            int: The calculated critical hit damage, rounded to the nearest whole number.
        """

        agilityFactor = (self.attributes['Agility'] * 14) / 100

        return round(self.physical_attack + 2.75 * agilityFactor + 0.09 * self.level, 0)

    def CalculateDefense(self, attribute: str) -> int:
        """
        Calculates the defense value for the player based on a specified attribute.

        This method computes the player's defense by using a specified attribute (e.g., 
        Endurance or Willpower) and a defense modifier. It adjusts the defense value 
        based on the player's level, ensuring that the resulting value is reasonable for combat.

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
        base cost, scaling factors, and the player's attribute values. It ensures that 
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

    def CalculateDodgeChance(self) -> float:
        """
        Finds the chance the player will successfully dodge the Player's attack.

        This method computes the probability that the player will evade the Player's attack 
        based on the player's agility attribute and level, adjusted by the Player's level. 
        The dodge chance is influenced by the ratio of the player's agility and a base factor, 
        with a small level-based modifier to account for differences in combat experience. 
        Higher agility and level increase the dodge chance, while higher player level reduces it.

        Args:
            player_level (int): The current level of the Player.

        Returns:
            float: The player's dodge chance when in combat with the Player.
        """

        return round(self.attributes['Agility'] / 200 + 0.003 * self.level, 2)
    
    def CalculateCriticalChance(self) -> float:
        """
        Finds the chance the player will successfully land a critical hit on the Player.

        Full description goes here.

        Returns:
            float: The player's critical hit chance when in combat with the Player.
        """

        return round(self.attributes['Agility'] / 400 + 0.002 * self.level, 2)

    def GenerateStatBar(self, current, maximum, length = 50, bar_color = 'white', bracket_color = 'white'):
        """
        Display stats in a bar.

        Parameters:
            self (object): Player object
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

    def GenerateExpBar(self, current, maximum, length = 50, bar_color = 'white', bracket_color = 'white'):
        """
        Display experience in a bar.

        Parameters:
            self (object): Player object
            current (int): Value of the current stat
            maximum (int): Value of the max stat
            length (int): Length of the stat bar
        
        Returns:
            exp_bar (str): The experience bar
            display (str): Stat in parathesis for actual value viewing
        """

        bar_length = int(length * (current / maximum))
        color_code = f"\033[1;{30 + list(('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')).index(bar_color)}m"
        bracket_color_code = f"\033[1;{30 + list(('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')).index(bracket_color)}m"
        exp_bar = f"{bracket_color_code}[{color_code}{'=' * bar_length}{' ' * (length - bar_length)}{bracket_color_code}]\033[0m"
        display = f"({current}/{maximum})".rjust(5)

        return exp_bar, display

    def Rest(self):
        """
        Recovers a random amount for each stat based on the Speed and Agility attributes

        Parameters:
            self (object): Player object
        
        Returns:
            seconds_to_wait (float): How long the player must wait between rests (in seconds)
        """

        seconds_to_wait = 100 / self.attributes['Speed']

        max_recovery = int(((self.attributes['Agility'] + self.attributes['Speed']) / 2) * 0.90)
        min_recovery = int(((self.attributes['Agility'] + self.attributes['Speed']) / 2) * 0.50)

        recovery_health = random.randint(min_recovery, max_recovery)
        recovery_mana = random.randint(min_recovery, max_recovery)
        recovery_stamina = random.randint(min_recovery, max_recovery)

        self.stats['Health'] = min(self.max_stats['Health'], self.stats['Health'] + recovery_health)
        self.stats['Mana'] = min(self.max_stats['Mana'], self.stats['Mana'] + recovery_mana)
        self.stats['Stamina'] = min(self.max_stats['Stamina'], self.stats['Stamina'] + recovery_stamina)

        return seconds_to_wait

    def LevelUp(self):
        """
        Level up the player, gain attribute points, and reset experience.
        """

        def get_attribute_name(choice):
            """
            Get the attribute name based on the numeric choice.

            Parameters:
                choice (int): Numeric choice representing an attribute.

            Returns:
                attribute_name (str): Name of the corresponding attribute.
            """

            attribute_mapping = {
                1: 'Strength',
                2: 'Endurance',
                3: 'Intelligence',
                4: 'Willpower',
                5: 'Agility',
                6: 'Speed'
            }

            return attribute_mapping.get(choice)

        ClearConsole()

        self.attribute_points += 5

        while self.attribute_points > 0:
            DisplayStars()
            MenuLine()
            print(f" ^ Congratulations, {self.name}! You are now Level {self.level + 1}.")
            MenuLine()
            print(f" - Attribute Points Remaining: {self.attribute_points}")
            MenuLine()
            print(f" 1. Strength     - {self.attributes['Strength']} (Max Stamina, Physical Damage)")
            print(f" 2. Endurance    - {self.attributes['Endurance']} (Max Health, Physical Defense)")
            print(f" 3. Intelligence - {self.attributes['Intelligence']} (Max Mana, Magical Damage)")
            print(f" 4. Willpower    - {self.attributes['Willpower']} (Spell Casting, Magical Defense)")
            print(f" 5. Agility      - {self.attributes['Agility']} (Dodge Chance, Critical Hit)")
            print(f" 6. Speed        - {self.attributes['Speed']} (Run Away, Faster Resting)")
            MenuLine()
            print(" * Enter the number of the attribute to increase (0 to save points): ")
            MenuLine()

            choice = ConsoleInput()

            if choice == '0':
                break
            elif choice in ['1', '2', '3', '4', '5', '6']:
                attribute_name = get_attribute_name(int(choice))

                if self.attributes[attribute_name] < 100:
                    self.attributes[attribute_name] += 1
                    self.attribute_points -= 1
                    MenuLine()
                    print(f" - {attribute_name} increased to {self.attributes[attribute_name]}.")
                    ClearConsole()
                else:
                    MenuLine()
                    print(f" - {attribute_name} is already been maxed out. Please try again.")
                    MenuLine()
                    time.sleep(2)
                    ClearConsole()
            else:
                return

        self.experience = round(self.experience % self.next_experience, 0)
        self.level += 1
        self.next_experience = round(self.next_experience * 1.125, 0)
        self.stats = self.CalculateBaseStats()
        self.max_stats = self.stats.copy()
        self.physical_attack = self.CalculateAttack("Strength", 10.5)
        self.magical_attack = self.CalculateAttack("Intelligence", 10.5)
        self.critical_hit = self.CalculateCriticalHit()
        self.physical_defense = self.CalculateDefense("Endurance")
        self.magical_defense = self.CalculateDefense("Willpower")
        self.stamina_cost = self.CalculateCost("Endurance", base = 15, scale = 1.4, per_level_scale = 0.012)
        self.mana_cost = self.CalculateCost("Willpower", base = 30, scale = 1.4, per_level_scale = 0.012)
        self.dodge_chance = self.CalculateDodgeChance()
        self.critical_chance = self.CalculateCriticalChance()