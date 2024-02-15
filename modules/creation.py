'''
Module Name: creation.py
Description: Handles the selection of race, birthsign, and class for the player's character.
Author: Hunter Reeves
Date: 2024-02-15
'''

# Modules
from modules.core import console_input, clear_console

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
    birthsign_options = ['The Warrior', 'The Mage', 'The Rogue']
    
    # Test

def select_race(name, art_race, menu_line):
    """
    Handles the menu and selection of the player's race.

    Parameters:
        name (str): The name of the character.
        default_art_race (function -> str): Function that returns an ASCII planet with stars.
        menu_line (function -> str): Function that returns a pretty menu line.

    Returns:
        race (str): The race of the character.
        attributes (list): The attributes of the selected race.
    """

    # Select race section
    race_options = ['Human', 'Elf', 'Orc', 'Lynxarite', 'Scalekin']

    # Custom message for each race
    race_messages = {
        'Human': "Humans are the most common race, found living in cities across the planet. \nMany adventurers and conquerors of old have been of Human descent.\n\nWell-rounded, truly the jack of all trades. \nYou can go in any direction you want as there are no debuffs for Humans.\n",
        'Elf': "Elves are most often found along the mountains in the southeast. \nWizards and scholars alike tend to be Elves. \n\nSuperior in Intelligence and Willpower with excellent mana. \nThe Elf tends to enjoy the highest comfort in all schools of magic.\n",
        'Orc': "Orcs live in clusters, typically in strongholds across the western coast. \nIncredibly strong and hardy - all Orcs share this in common. \n\nThey boast high Strength and Endurance, but aren't very smart. \nOrcs tend to favor the warrior life while trying to avoid books.\n",
        'Lynxarite': "Lynxarites prefer the tropical heat and warm sands of the equator. \nNimble on their feet, they get out of trouble but cause even more. \n\nThese cat-like beasts have higher Agility than most. \nAs a Lynxarite, you'll always be one step ahead.\n",
        'Scalekin': "Hailing from the marshes in the south, the Scalekin reign supreme. \nAs the most athletic race, they tend to get away from anything. \n\nThese reptile-like beasts have Speed like none other. \nIf you are going to race a Scalekin, best of luck to you!\n"
    }

    attributes = {'Human': [40, 40, 40, 40, 40, 40], 'Elf': [35, 35, 45, 50, 35, 40], 'Orc': [45, 50, 35, 35, 40, 35], 'Lynxarite': [35, 40, 35, 40, 50, 40], 'Scalekin': [40, 35, 40, 35, 40, 50]}
    m_attributes = "Strength\t- {}" + " " * 17 + "(Affects Max Stamina, Physical Damage)\nEndurance\t- {}" + " " * 20 + "(Health Increase, Physical Defense)\nIntelligence\t- {}" + " " * 21 + "(Affects Max Mana, Magical Damage)\nWillpower\t- {}" + " " * 23 + "(Mana Increase, Magical Defense)\nAgility\t\t- {}" + " " * 27 + "(Dodge Chance, Critical Hit)\nSpeed\t\t- {}" + " " * 22+ "(Attack First, Effective Resting)"

    while True:
        # Start with default race menu
        option = race_menu(name, art_race, menu_line, race_options)

        # Initialize variables
        race = ""
        race_attributes = []

        if option in ['1', '2', '3', '4', '5']:
            race_name = race_options[int(option) - 1]
            race_attributes = attributes[race_name]

            art_race()
            menu_line()
            print(f" > {name}, the {race_name}:")
            menu_line()
            message = race_messages[race_name]
            print(message)
            print(m_attributes.format(*race_attributes))

            print("\nIs this your race? (Y/N)")
            menu_line()
            response = console_input()

            if response.lower() == "y":
                race = race_name
                break

    return race, attributes[race]

def race_menu(name, default_art_race, menu_line, race_options):
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

    default_art_race()
    menu_line()
    print(" > " + name + "... what is your race?")
    menu_line()

    # Print options in the console for selection
    for number, option in enumerate(race_options, start=1):
        print(f" {number}. {option}")

    menu_line()
    option = console_input()

    clear_console()

    return option