'''
Module Name: creation.py
Description: Handles the selection of race, birthsign, and class for the player's character.
Author: Hunter Reeves
Date: 2024-02-15
'''

# Modules
from modules.core import console_input, clear_console

def birthsign_menu(name, art_birthsign, menu_line, birthsign_options):
    """
    Handles the default menu for selecting a birthsign.
    
    Parameters:
        name (str): The name of the character.
        art_birthsign (function -> str): Function that returns an ASCII planet with stars.
        menu_line (function -> str): Function that returns a pretty menu line.
        birthsign_options (list): List of all birthsigns.
    
    Returns:
        option (str): The option the player selected for their birthsign.
    """
    
    # Clear console of previous menus
    clear_console()

    art_birthsign()
    menu_line()
    print(" > " + name + "... what is your birthsign?")
    menu_line()

    # Print options in the console for selection
    for number, option in enumerate(birthsign_options, start = 1):
        print(f" {number}. {option}")

    menu_line()
    option = console_input()

    clear_console()

    return option

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
    birthsign_options = ['The Lord', 'The Magistar', 'The Rogue']
    
    # Custom message for each sign
    birthsign_messages = {
        birthsign_options[0]: "Those born under The Lord can expect to be stronger and hardier.\n\nHowever, they tend to be slower, weaker to magical damage overall,\nand less capable at casting spells as they progress through the world.\n",
        birthsign_options[1]: "Those born under The Magistar can expect to be smart and diligent.\n\nHowever, they tend to be clumsy, weaker to physical damage overall,\nand have less health overall as they progress through the world.\n",
        birthsign_options[2]: "Those born under The Rogue can expect to be quick on their feet.\n\nHowever, they tend to be dumb, less effective with magic overall,\nand less capable at spellcasting as they progress through the world.\n"
    }
            
    # For printing the updated attributes to the screen
    m_attributes = "Strength\t- {}" + " " * 17 + "(Affects Max Stamina, Physical Damage)\n" \
                   "Endurance\t- {}" + " " * 20 + "(Health Increase, Physical Defense)\n" \
                   "Intelligence\t- {}" + " " * 21 + "(Affects Max Mana, Magical Damage)\n" \
                   "Willpower\t- {}" + " " * 23 + "(Mana Increase, Magical Defense)\n" \
                   "Agility\t\t- {}" + " " * 27 + "(Dodge Chance, Critical Hit)\n" \
                   "Speed\t\t- {}" + " " * 22 + "(Attack First, Effective Resting)"

    # Cycle through birthsign selection until a final decision is made
    while True:
        # Start with default birthsign menu
        option = birthsign_menu(name, art_birthsign, menu_line, birthsign_options)

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
            print(f" > {name}, born under {birthsign_name} sign:")
            menu_line()
            # Iterate through attributes to display only the changed attributes on a single line
            changes = " - ".join([f"[{key} {'+' if birthsign_attributes.get(key, 0) > 0 else '-'}{abs(birthsign_attributes.get(key, 0))}]" for key in attributes if birthsign_attributes.get(key, 0) != 0])
            print(f" > {changes}")
            menu_line()
            message = birthsign_messages[birthsign_name]
            
            # Print information regarding the current birthsign
            print(message)
            print(m_attributes.format(*[attributes[key] + birthsign_attributes.get(key, 0) for key in attributes]))

            # Confirmation for birthsign
            print("\nIs this your birthsign? (Y/N)")
            menu_line()
            response = console_input()

            if response.lower() == "y":
                # Adjust attributes based on the birthsign chosen by the player
                birthsign = birthsign_name
                for key in birthsign_attributes:
                    attributes[key] += birthsign_attributes[key]
                break
            
    return birthsign, attributes

def race_menu(name, art_race, menu_line, race_options):
    """
    Handles the default menu for selecting a race.
    
    Parameters:
        name (str): The name of the character.
        default_art_race (function -> str): Function that returns an ASCII planet with stars.
        menu_line (function -> str): Function that returns a pretty menu line.
        race_options (list): List of all races.
    
    Returns:
        option (str): The option the player selected for their race.
    """
    
    # Clear console of previous menus
    clear_console()

    art_race()
    menu_line()
    print(" > " + name + "... what is your race?")
    menu_line()

    # Print options in the console for selection
    for number, option in enumerate(race_options, start = 1):
        print(f" {number}. {option}")

    menu_line()
    option = console_input()

    clear_console()

    return option

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
        race_options[0]: "Humans are the most common race, found living in cities across the planet. \nMany adventurers and conquerors of old have been of Human descent.\n\nWell-rounded, truly the jack of all trades. \nYou can go in any direction you want as there are no debuffs for Humans.\n",
        race_options[1]: "Elves are most often found along the mountains in the southeast. \nWizards and scholars alike tend to be Elves. \n\nSuperior in Intelligence and Willpower with excellent mana. \nThe Elf tends to enjoy the highest comfort in all schools of magic.\n",
        race_options[2]: "Orcs live in clusters, typically in strongholds across the western coast. \nIncredibly strong and hardy - all Orcs share this in common. \n\nThey boast high Strength and Endurance, but aren't very smart. \nOrcs tend to favor the warrior life while trying to avoid books.\n",
        race_options[3]: "Lynxarites prefer the tropical heat and warm sands of the equator. \nNimble on their feet, they get out of trouble but cause even more. \n\nThese cat-like beasts have higher Agility than most. \nAs a Lynxarite, you'll always be one step ahead.\n",
        race_options[4]: "Hailing from the marshes in the south, the Scalekin reign supreme. \nAs the most athletic race, they tend to get away from anything. \n\nThese reptile-like beasts have Speed like none other. \nIf you are going to race a Scalekin, best of luck to you!\n"
    }

    # Attributes for each race
    attributes = {
        'Human': {'Strength': 40, 'Endurance': 40, 'Intelligence': 40, 'Willpower': 40, 'Agility': 40, 'Speed': 40},
        'Elf': {'Strength': 35, 'Endurance': 35, 'Intelligence': 45, 'Willpower': 50, 'Agility': 35, 'Speed': 40},
        'Orc': {'Strength': 45, 'Endurance': 50, 'Intelligence': 35, 'Willpower': 35, 'Agility': 40, 'Speed': 35},
        'Lynxarite': {'Strength': 35, 'Endurance': 40, 'Intelligence': 35, 'Willpower': 40, 'Agility': 50, 'Speed': 40},
        'Scalekin': {'Strength': 40, 'Endurance': 35, 'Intelligence': 40, 'Willpower': 35, 'Agility': 40, 'Speed': 50}
    }

    # For printing the updated attributes to the screen
    m_attributes = "Strength\t- {}" + " " * 17 + "(Affects Max Stamina, Physical Damage)\n" \
                   "Endurance\t- {}" + " " * 20 + "(Health Increase, Physical Defense)\n" \
                   "Intelligence\t- {}" + " " * 21 + "(Affects Max Mana, Magical Damage)\n" \
                   "Willpower\t- {}" + " " * 23 + "(Mana Increase, Magical Defense)\n" \
                   "Agility\t\t- {}" + " " * 27 + "(Dodge Chance, Critical Hit)\n" \
                   "Speed\t\t- {}" + " " * 22 + "(Attack First, Effective Resting)"
                   
    # Cycle through race selection until a final decision is made
    while True:
        # Start with default race menu
        option = race_menu(name, art_race, menu_line, race_options)

        # Initialize variables
        race = ""
        race_attributes = {}

        if option in ['1', '2', '3', '4', '5']:
            race_name = race_options[int(option) - 1]
            race_attributes = attributes[race_name]

            # Menu for describing the selected race
            art_race()
            menu_line()
            print(f" > {name}, the {race_name}:")
            menu_line()
            message = race_messages[race_name]
            
            # Print information regarding the current race
            print(message)
            print(m_attributes.format(*[race_attributes[key] for key in race_attributes]))

            # Confirmation for race
            print("\nIs this your race? (Y/N)")
            menu_line()
            response = console_input()

            if response.lower() == "y":
                race = race_name
                break
    
    return race, race_attributes