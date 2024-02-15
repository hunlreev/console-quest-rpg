import random
import time
import pickle
import os

from classes.Player import Player  # Importing Player class from Player.py

locations = {
    'Forest': {'enemy': 'Goblin', 'quest': 'Collect 5 mushrooms'},
    'Cave': {'enemy': 'Troll', 'quest': 'Find the lost treasure'},
    'Town': {'enemy': None, 'quest': 'Help the lady with a rat problem'},
    'Mountain': {'enemy': 'Bandit', 'quest': 'Retrieve the religious artifact'}
}

def explore():
    return random.choice(list(locations.keys()))

def encounter_enemy(enemy):
    print(f"\nOh no! You encounter a {enemy}!")
    return {'name': enemy, 'Strength': random.randint(50, 70), 'Endurance': random.randint(20, 40), 'Willpower': random.randint(20, 40), 'health': random.randint(60, 100)}

def combat(player, enemy):
    print(f"Battle begins! {player.name} vs {enemy['name']}")

    while player.stats['Health'] > 0 and enemy['health'] > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("(1) Attack\n(2) Cast a spell\n(3) Dodge\n(4) Run away")
        print("\nChose your action")
        action_choice = input("> ")
        time.sleep(1) 

        if action_choice == '1':
            if player.use_stamina(10):
                player_damage = max(0, player.attributes['Strength'] - enemy['Endurance'])
                enemy['health'] -= player_damage
                time.sleep(1) 
                print(f"\n{player.name} attacks {enemy['name']} for {player_damage} damage. {enemy['name']}'s health: {enemy['health']}\n")
        elif action_choice == '2':
            if player.use_mana(15):
                print("\nYou cast a spell!")
                spell_damage =  max(0, player.attributes['Intelligence'] - enemy['Willpower'])
                enemy['health'] -= spell_damage
                time.sleep(1) 
                print(f"\nThe spell hits {enemy['name']} for {spell_damage} damage. {enemy['name']}'s health: {enemy['health']}\n")
        elif action_choice == '3':
            print("\nYou attempt to dodge the enemy's attack!")
            time.sleep(2)
            print("Dodge failed!")
        elif action_choice == '4':
            print("\nYou decide to run away.")
            time.sleep(1) 
            break
        else:
            print("\nInvalid choice. Try again.")

        if enemy['health'] <= 0:
            print(f"\nYou defeated the {enemy['name']}!")
            player.gain_experience(random.randint(30, 50))
            player.inventory['Gold'] += random.randint(10, 20)
            break

        # Enemy's turn
        enemy_damage = max(0, enemy['Strength'] + (round(1.15 * player.level + 5, 0)) - player.attributes['Endurance']) # Scale damage to player level
        player.stats['Health'] -= enemy_damage
        time.sleep(2) 
        print(f"{enemy['name']} attacks {player.name} for {enemy_damage} damage. {player.name}'s health: {player.stats['Health']}")
        time.sleep(2) 

        if player.stats['Health'] <= 0:
            print(f"\nUnfortunately, you have been defeated by the {enemy['name']}. Game over.")
            break

def save_game(player):
    with open('saves\\' + player.name + '.pkl', 'wb') as file:
        pickle.dump(player, file)
    print("\nThanks for playing! Your progress has been saved.")

def load_game(name):
    try:
        with open('saves\\' + name + '.pkl', 'rb') as file:
            player = pickle.load(file)
        print("\nGame loaded.")
        return player
    except FileNotFoundError:
        print("No saved game found.")
        return None

def main():
    # Clear terminal at start of game loop
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Title Screen
    print("Welcome to the Enhanced Text Adventure RPG!\n")

    print("Do you want to load a saved game? (yes/no)")
    load_option = input("> ").lower()
    if load_option == 'yes':
        print("\nPlease enter your chacter's name.")
        name = input("> ")
        player = load_game(name)
        if player is None:
            print("\nEnter your character's name")
            name = input("> ")
            print("Enter your character's race")
            race = input("> ")
            player = Player(name, race)
    else:
        print("\nEnter your character's name")
        name = input("> ")
        print("Enter your character's race")
        race = input("> ")
        player = Player(name, race)

    while player.stats['Health'] > 0:
        # End the game loop if player died
        if player.stats["Health"] <= 0:
            break

        # Player exploration choice
        print("\nWhat will you do? (1) Explore (2) View status (3) Rest (4) Save and quit (5) Quit without saving")
        user_choice = input("> ")

        if user_choice == '1':
            print("\nYou decide to explore...")
            time.sleep(1)
            player.location = explore()
            print(f"\nCurrent Location: {player.location}.")
            # Random chance of encountering an enemy
            if random.random() < 0.5 and player.location != 'Town':
                enemy_info = encounter_enemy(locations[player.location]['enemy'])
                combat(player, enemy_info)
        elif user_choice == '2':
            time.sleep(0) 
            player.display_status()
        elif user_choice == '3':
            print("\nYou take a moment to rest and recover.")
            time.sleep(3) 
            player.rest()
        elif user_choice == '4':
            save_game(player)
            time.sleep(0) 
            break
        elif user_choice == '5':
            print("\nYou decide to quit the game without saving. Thanks for playing!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")

        # End the game loop if player died
        if player.stats["Health"] <= 0:
            print("\nGame over.")
            break

if __name__ == "__main__":
    main()