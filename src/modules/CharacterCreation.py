'''
Module for character creation in the game.

This module handles the selection process for a player's character, including race, birthsign, and class.
It provides a series of menus that guide the player through the character creation process,
allowing them to choose attributes that will affect gameplay. 

Functions:
- CharacterMenuSelection: Displays a menu for the player to select a character attribute (race, birthsign, or class).
- SelectClass: Manages the selection of the player's class, presenting options and modifying attributes based on the chosen class.
- SelectBirthsign: Manages the selection of the player's birthsign, presenting options and modifying attributes based on the chosen birthsign.
- SelectRace: Manages the selection of the player's race, presenting options and providing associated attributes.
'''

from src.modules.CoreGameFunctions import ConsoleInput, ClearConsole
from src.modules.ArtAssets import DisplayWarrior, DisplayMage, DisplayRogue

from collections.abc import Callable

m_attributes = " Strength\t- {}" + " " * 16 + "(Affects Max Stamina, Physical Damage)\n" \
               " Endurance\t- {}" + " " * 16 + "(Affects Max Health, Physical Defense)\n" \
               " Intelligence\t- {}" + " " * 20 + "(Affects Max Mana, Magical Damage)\n" \
               " Willpower\t- {}" + " " * 16 + "(Spell Effectiveness, Magical Defense)\n" \
               " Agility\t- {}" + " " * 26 + "(Dodge Chance, Critical Hit)\n" \
               " Speed\t\t- {}" + " " * 28 + "(Run Away, Faster Resting)"

def CharacterMenuSelection(name: str, art: Callable, menu_line: Callable, options: list, type: str = "") -> str:
    """
    Displays a menu for the player to select a character attribute (race, birthsign, or class).
    
    Parameters:
        name (str): The name of the character.
        art (function -> str): Function that returns ASCII art.
        menu_line (function -> str): Function that returns a pretty menu line.
        options (list): List of all options
        type (str): Type of choice being made (race, birthsign, or class)
    
    Returns:
        option (str): The option the player selected for their selection choices.
    """
    
    ClearConsole()
    art()
    menu_line()
    print(" * " + name + "... what is your " + type + "?")
    menu_line()

    for number, option in enumerate(options, start = 1):
        print(f" {number}. {option}")

    menu_line()
    option = ConsoleInput()

    ClearConsole()

    return option

def SelectClass(name: str, attributes: list, art_class: Callable, menu_line: Callable) -> tuple[str, list]:
    """
    Manages the selection of the player's class, presenting options and modifying attributes based on the chosen class.

    Parameters:
        name (str): The name of the character.
        attributes (list): The attributes of the character.
        art_birthsign (function -> str): Function that returns an ASCII drawing of stars.
        menu_line (function -> str): Function that returns a pretty menu line.

    Returns:
        player_class (str): The selected class of the character.
        attributes (list): The character's attributes.
    """

    class_options = ['Warrior', 'Mage', 'Rogue']

    class_messages = {
        class_options[0]: " The Warrior class specializes in swords, maces, axes, and heavy armor.\n\n Their armor is a bit too heavy though, and slows them down in battle.\n Despite that, they are very defensive and have quite the health pool.\n",
        class_options[1]: " The Mage class specializes in staves, spellmagic, and enchantments.\n\n Their focus on magic tends to make them a bit aloof and cold.\n Despite that, they are excellent magic users and have a lot of knowledge.\n",
        class_options[2]: " The Rogue class specializes in stealth, critical hits, and light armor.\n\n If they are caught, they can lose health very quickly.\n Despite that, they can deal extreme amounts of damage if well hidden.\n"
    }
    
    while True:
        option = CharacterMenuSelection(name, art_class, menu_line, class_options, "class")

        player_class = ""
        class_attributes = {}

        if option in ['1', '2', '3']:
            if option == '1':
                class_name = class_options[0]
                class_attributes = {'Strength': 5, 'Endurance': 5, 'Speed': -5}
                art = DisplayWarrior
            elif option == '2':
                class_name = class_options[1]
                class_attributes = {'Intelligence': 5, 'Willpower': 5, 'Agility': -5}
                art = DisplayMage
            elif option == '3':
                class_name = class_options[2]
                class_attributes = {'Agility': 5, 'Speed': 5, 'Endurance': -5}
                art = DisplayRogue

            art()
            menu_line()
            print(f" ^ {name}, the {class_name}:")
            menu_line()
            changes = " - ".join([f"[{key} {'+' if class_attributes.get(key, 0) > 0 else '-'}{abs(class_attributes.get(key, 0))}]" for key in attributes if class_attributes.get(key, 0) != 0])
            print(f" - {changes}")
            menu_line()
            message = class_messages[class_name]
            
            print(message)
            print(m_attributes.format(*[attributes[key] + class_attributes.get(key, 0) for key in attributes]))

            print("\n * Is this your class? (Y/N)")
            menu_line()
            response = ConsoleInput()

            if response.lower() == "y":
                player_class = class_name
                for key in class_attributes:
                    attributes[key] += class_attributes[key]
                break
            
    return player_class, attributes

def SelectBirthsign(name: str, attributes: list, art_birthsign: Callable, menu_line: Callable) -> tuple[str, list]:
    """
    Manages the selection of the player's birthsign, presenting options and modifying attributes based on the chosen birthsign.

    Parameters:
        name (str): The name of the character.
        attributes (list): The attributes of the character.
        art_birthsign (function -> str): Function that returns an ASCII drawing of stars.
        menu_line (function -> str): Function that returns a pretty menu line.

    Returns:
        birthsign (str): The selected birthsign of the character.
        attributes (list): The character's attributes.
    """
    
    birthsign_options = ['The Knight', 'The Magistar', 'The Shadow']
    
    birthsign_messages = {
        birthsign_options[0]: " Those born under The Knight can expect to be stronger and hardier.\n\n However, they tend to be slower, weaker to magical damage overall,\n and less capable at casting spells as they progress through the world.\n",
        birthsign_options[1]: " Those born under The Magistar can expect to be smart and diligent.\n\n However, they tend to be clumsy, weaker to physical damage overall,\n and have less health overall as they progress through the world.\n",
        birthsign_options[2]: " Those born under The Shadow can expect to be quick on their feet.\n\n However, they tend to be dumb, less effective with magic overall,\n and less capable at spellcasting as they progress through the world.\n"
    }

    while True:
        option = CharacterMenuSelection(name, art_birthsign, menu_line, birthsign_options, "birthsign")

        birthsign = ""
        birthsign_attributes = {}

        if option in ['1', '2', '3']:
            if option == '1':
                birthsign_name = birthsign_options[0]
                birthsign_attributes = {'Strength': 5, 'Endurance': 5, 'Willpower': -5, 'Speed': -5}
            elif option == '2':
                birthsign_name = birthsign_options[1]
                birthsign_attributes = {'Intelligence': 5, 'Willpower': 5, 'Endurance': -5, 'Agility': -5}
            elif option == '3':
                birthsign_name = birthsign_options[2]
                birthsign_attributes = {'Agility': 5, 'Speed': 5, 'Intelligence': -5, 'Willpower': -5}

            art_birthsign()
            menu_line()
            print(f" ^ {name}, born under {birthsign_name} sign:")
            menu_line()
            changes = " - ".join([f"[{key} {'+' if birthsign_attributes.get(key, 0) > 0 else '-'}{abs(birthsign_attributes.get(key, 0))}]" for key in attributes if birthsign_attributes.get(key, 0) != 0])
            print(f" - {changes}")
            menu_line()
            message = birthsign_messages[birthsign_name]
            
            print(message)
            print(m_attributes.format(*[attributes[key] + birthsign_attributes.get(key, 0) for key in attributes]))

            print("\n * Is this your birthsign? (Y/N)")
            menu_line()
            response = ConsoleInput()

            if response.lower() == "y":
                birthsign = birthsign_name
                for key in birthsign_attributes:
                    attributes[key] += birthsign_attributes[key]
                break
            
    return birthsign, attributes

def SelectRace(name: str, art_race: Callable, menu_line: Callable) -> tuple[str, dict]:
    """
    Manages the selection of the player's race, presenting options and providing associated attributes.

    Parameters:
        name (str): The name of the character.
        default_art_race (function -> str): Function that returns an ASCII planet with stars.
        menu_line (function -> str): Function that returns a pretty menu line.

    Returns:
        race (str): The race of the character.
        attributes (dict): The attributes of the selected race.
    """

    race_options = ['Human', 'Elf', 'Orc', 'Lynxarite', 'Scalekin']

    race_messages = {
        race_options[0]: " Humans are the most common race, found in cities across the planet. \n Many adventurers and conquerors of old have been of Human descent.\n\n Well-rounded, truly the jack of all trades with an even spread. \n You can go in any direction you want as a Human.\n",
        race_options[1]: " Elves are most often found along the mountains in the southeast. \n Wizards and scholars alike tend to be Elves. \n\n Superior in Intelligence and Willpower with excellent mana. \n The Elf tends to enjoy the highest comfort in all schools of magic.\n",
        race_options[2]: " Orcs live in clusters, typically in strongholds across the western coast. \n Incredibly strong and hardy - all Orcs share this in common. \n\n They boast high Strength and Endurance, but aren't very smart. \n Orcs tend to favor the warrior life, avoiding books.\n",
        race_options[3]: " Lynxarites prefer the tropical heat and warm sands of the equator. \n Nimble on their feet, they get out of trouble but cause even more. \n\n These cat-like beasts have higher Agility than most. \n As a Lynxarite, you'll always be one step ahead.\n",
        race_options[4]: " Hailing from the marshes in the south, the Scalekin reign supreme. \n As the most athletic race, they tend to get away from anything. \n\n These reptile-like beasts have Speed like none other. \n If you are going to race a Scalekin, best of luck to you!\n"
    }

    attributes = {
        'Human': {'Strength': 40, 'Endurance': 40, 'Intelligence': 40, 'Willpower': 40, 'Agility': 40, 'Speed': 40},
        'Elf': {'Strength': 30, 'Endurance': 35, 'Intelligence': 50, 'Willpower': 45, 'Agility': 40, 'Speed': 40},
        'Orc': {'Strength': 50, 'Endurance': 45, 'Intelligence': 30, 'Willpower': 35, 'Agility': 40, 'Speed': 40},
        'Lynxarite': {'Strength': 35, 'Endurance': 30, 'Intelligence': 45, 'Willpower': 40, 'Agility': 50, 'Speed': 40},
        'Scalekin': {'Strength': 45, 'Endurance': 40, 'Intelligence': 35, 'Willpower': 30, 'Agility': 40, 'Speed': 50}
    }
                   
    while True:
        option = CharacterMenuSelection(name, art_race, menu_line, race_options, "race")

        race = ""
        race_attributes = {}

        if option in ['1', '2', '3', '4', '5']:
            race_name = race_options[int(option) - 1]
            race_attributes = attributes[race_name]

            art_race()
            menu_line()
            print(f" ^ {name}, the {race_name}:")
            menu_line()
            message = race_messages[race_name]
            
            print(message)
            print(m_attributes.format(*[race_attributes[key] for key in race_attributes]))

            print("\n * Is this your race? (Y/N)")
            menu_line()
            response = ConsoleInput()

            if response.lower() == "y":
                race = race_name
                break
    
    return race, race_attributes