'''
Module Name: creation.py
Description: Handles the selection of race, birthsign, and class for the player's character.
Author: Hunter Reeves
Date: 2024-02-17
'''

# Modules
from modules.core import console_input, clear_console
from modules.console_art import art_warrior, art_mage, art_rogue

# For printing the attributes to the screen at various locations
m_attributes = " Strength\t- {}" + " " * 16 + "(Affects Max Stamina, Physical Damage)\n" \
               " Endurance\t- {}" + " " * 16 + "(Affects Max Health, Physical Defense)\n" \
               " Intelligence\t- {}" + " " * 20 + "(Affects Max Mana, Magical Damage)\n" \
               " Willpower\t- {}" + " " * 16 + "(Spell Effectiveness, Magical Defense)\n" \
               " Agility\t- {}" + " " * 26 + "(Dodge Chance, Critical Hit)\n" \
               " Speed\t\t- {}" + " " * 21 + "(Attack First, Effective Resting)"

def selection_menu(name, art, menu_line, options, type = ""):
    """
    Handles the default menu for selecting race, birthsign, or class.
    
    Parameters:
        name (str): The name of the character.
        art (function -> str): Function that returns ASCII art.
        menu_line (function -> str): Function that returns a pretty menu line.
        options (list): List of all options
        type (str): Type of choice being made (race, birthsign, or class)
    
    Returns:
        option (str): The option the player selected for their selection choices.
    """
    
    # Clear console of previous menus
    clear_console()

    art()
    menu_line()
    print(" * " + name + "... what is your " + type + "?")
    menu_line()

    # Print options in the console for selection
    for number, option in enumerate(options, start = 1):
        print(f" {number}. {option}")

    menu_line()
    option = console_input()

    clear_console()

    return option

def select_class(name, attributes, art_class, menu_line):
    """
    Handles the menu and selection of the player's class.

    Parameters:
        name (str): The name of the character.
        attributes (list): The attributes of the character.
        art_birthsign (function -> str): Function that returns an ASCII drawing of stars.
        menu_line (function -> str): Function that returns a pretty menu line.

    Returns:
        player_class (str): The selected class of the character.
        attributes (list): The character's attributes.
    """

    # Select class options
    class_options = ['Warrior', 'Mage', 'Rogue']

    # Custom message for each class
    class_messages = {
        class_options[0]: " The Warrior class specializes in swords, maces, axes, and heavy armor.\n\n Their armor is a bit too heavy though, and slows them down in battle.\n Despite that, they are very defensive and have quite the health pool.\n",
        class_options[1]: " The Mage class specializes in staves, spellmagic, and enchantments.\n\n Their focus on magic tends to make them a bit aloof and cold.\n Despite that, they are excellent magic users and have a lot of knowledge.\n",
        class_options[2]: " The Rogue class specializes in stealth, critical hits, and light armor.\n\n If they are caught, they can lose health very quickly.\n Despite that, they can deal extreme amounts of damage if well hidden.\n"
    }
    
    # Cycle through the class selection until a final decision is made
    while True:
        # Start with default birthsign menu
        option = selection_menu(name, art_class, menu_line, class_options, "class")

        # Initialize variables
        player_class = ""
        class_attributes = {}

        # Manage buffs and debuffs to attributes
        if option in ['1', '2', '3']:
            if option == '1':
                class_name = class_options[0]
                class_attributes = {'Strength': 5, 'Endurance': 5, 'Speed': -5}
                art = art_warrior
            elif option == '2':
                class_name = class_options[1]
                class_attributes = {'Intelligence': 5, 'Willpower': 5, 'Agility': -5}
                art = art_mage
            elif option == '3':
                class_name = class_options[2]
                class_attributes = {'Agility': 5, 'Speed': 5, 'Endurance': -5}
                art = art_rogue

            # Menu for describing the selected class
            art()
            menu_line()
            print(f" ^ {name}, the {class_name}:")
            menu_line()
            # Iterate through attributes to display only the changed attributes on a single line
            changes = " - ".join([f"[{key} {'+' if class_attributes.get(key, 0) > 0 else '-'}{abs(class_attributes.get(key, 0))}]" for key in attributes if class_attributes.get(key, 0) != 0])
            print(f" - {changes}")
            menu_line()
            message = class_messages[class_name]
            
            # Print information regarding the current class
            print(message)
            print(m_attributes.format(*[attributes[key] + class_attributes.get(key, 0) for key in attributes]))

            # Confirmation for class
            print("\n * Is this your class? (Y/N)")
            menu_line()
            response = console_input()

            if response.lower() == "y":
                # Adjust attributes based on the class chosen by the player
                player_class = class_name
                for key in class_attributes:
                    attributes[key] += class_attributes[key]
                break
            
    return player_class, attributes

def select_birthsign(name, attributes, art_birthsign, menu_line):
    """
    Handles the menu and selection of the player's birthsign.

    Parameters:
        name (str): The name of the character.
        attributes (list): The attributes of the character.
        art_birthsign (function -> str): Function that returns an ASCII drawing of stars.
        menu_line (function -> str): Function that returns a pretty menu line.

    Returns:
        birthsign (str): The selected birthsign of the character.
        attributes (list): The character's attributes.
    """
    
    # Select birthsign section
    birthsign_options = ['The Knight', 'The Magistar', 'The Shadow']
    
    # Custom message for each sign
    birthsign_messages = {
        birthsign_options[0]: " Those born under The Knight can expect to be stronger and hardier.\n\n However, they tend to be slower, weaker to magical damage overall,\n and less capable at casting spells as they progress through the world.\n",
        birthsign_options[1]: " Those born under The Magistar can expect to be smart and diligent.\n\n However, they tend to be clumsy, weaker to physical damage overall,\n and have less health overall as they progress through the world.\n",
        birthsign_options[2]: " Those born under The Shadow can expect to be quick on their feet.\n\n However, they tend to be dumb, less effective with magic overall,\n and less capable at spellcasting as they progress through the world.\n"
    }

    # Cycle through birthsign selection until a final decision is made
    while True:
        # Start with default birthsign menu
        option = selection_menu(name, art_birthsign, menu_line, birthsign_options, "birthsign")

        # Initialize variables
        birthsign = ""
        birthsign_attributes = {}

        # Manage buffs and debuffs to attributes
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

            # Menu for describing the selected birthsign
            art_birthsign()
            menu_line()
            print(f" ^ {name}, born under {birthsign_name} sign:")
            menu_line()
            # Iterate through attributes to display only the changed attributes on a single line
            changes = " - ".join([f"[{key} {'+' if birthsign_attributes.get(key, 0) > 0 else '-'}{abs(birthsign_attributes.get(key, 0))}]" for key in attributes if birthsign_attributes.get(key, 0) != 0])
            print(f" - {changes}")
            menu_line()
            message = birthsign_messages[birthsign_name]
            
            # Print information regarding the current birthsign
            print(message)
            print(m_attributes.format(*[attributes[key] + birthsign_attributes.get(key, 0) for key in attributes]))

            # Confirmation for birthsign
            print("\n * Is this your birthsign? (Y/N)")
            menu_line()
            response = console_input()

            if response.lower() == "y":
                # Adjust attributes based on the birthsign chosen by the player
                birthsign = birthsign_name
                for key in birthsign_attributes:
                    attributes[key] += birthsign_attributes[key]
                break
            
    return birthsign, attributes

def select_race(name, art_race, menu_line):
    """
    Handles the menu and selection of the player's race.

    Parameters:
        name (str): The name of the character.
        default_art_race (function -> str): Function that returns an ASCII planet with stars.
        menu_line (function -> str): Function that returns a pretty menu line.

    Returns:
        race (str): The race of the character.
        attributes (dict): The attributes of the selected race.
    """

    # Select race section
    race_options = ['Human', 'Elf', 'Orc', 'Lynxarite', 'Scalekin']

    # Custom message for each race
    race_messages = {
        race_options[0]: " Humans are the most common race, found in cities across the planet. \n Many adventurers and conquerors of old have been of Human descent.\n\n Well-rounded, truly the jack of all trades with an even spread. \n You can go in any direction you want as a Human.\n",
        race_options[1]: " Elves are most often found along the mountains in the southeast. \n Wizards and scholars alike tend to be Elves. \n\n Superior in Intelligence and Willpower with excellent mana. \n The Elf tends to enjoy the highest comfort in all schools of magic.\n",
        race_options[2]: " Orcs live in clusters, typically in strongholds across the western coast. \n Incredibly strong and hardy - all Orcs share this in common. \n\n They boast high Strength and Endurance, but aren't very smart. \n Orcs tend to favor the warrior life, avoiding books.\n",
        race_options[3]: " Lynxarites prefer the tropical heat and warm sands of the equator. \n Nimble on their feet, they get out of trouble but cause even more. \n\n These cat-like beasts have higher Agility than most. \n As a Lynxarite, you'll always be one step ahead.\n",
        race_options[4]: " Hailing from the marshes in the south, the Scalekin reign supreme. \n As the most athletic race, they tend to get away from anything. \n\n These reptile-like beasts have Speed like none other. \n If you are going to race a Scalekin, best of luck to you!\n"
    }

    # Attributes for each race
    attributes = {
        'Human': {'Strength': 40, 'Endurance': 40, 'Intelligence': 40, 'Willpower': 40, 'Agility': 40, 'Speed': 40},
        'Elf': {'Strength': 30, 'Endurance': 35, 'Intelligence': 50, 'Willpower': 45, 'Agility': 40, 'Speed': 40},
        'Orc': {'Strength': 50, 'Endurance': 45, 'Intelligence': 30, 'Willpower': 35, 'Agility': 40, 'Speed': 40},
        'Lynxarite': {'Strength': 35, 'Endurance': 30, 'Intelligence': 45, 'Willpower': 40, 'Agility': 50, 'Speed': 40},
        'Scalekin': {'Strength': 45, 'Endurance': 40, 'Intelligence': 35, 'Willpower': 30, 'Agility': 40, 'Speed': 50}
    }
                   
    # Cycle through race selection until a final decision is made
    while True:
        # Start with default race menu
        option = selection_menu(name, art_race, menu_line, race_options, "race")

        # Initialize variables
        race = ""
        race_attributes = {}

        if option in ['1', '2', '3', '4', '5']:
            race_name = race_options[int(option) - 1]
            race_attributes = attributes[race_name]

            # Menu for describing the selected race
            art_race()
            menu_line()
            print(f" ^ {name}, the {race_name}:")
            menu_line()
            message = race_messages[race_name]
            
            # Print information regarding the current race
            print(message)
            print(m_attributes.format(*[race_attributes[key] for key in race_attributes]))

            # Confirmation for race
            print("\n * Is this your race? (Y/N)")
            menu_line()
            response = console_input()

            if response.lower() == "y":
                race = race_name
                break
    
    return race, race_attributes