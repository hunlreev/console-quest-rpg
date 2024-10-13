'''
Shop functionality for Console Quest RPG.

This module handles the shop system within the game, allowing players to buy and sell items. It manages:
- Displaying the shop menu for player interactions (buying items, selling items, leaving the shop).
- Loading the inventory of items available for purchase and the items the shop requires from external text files.
- Facilitating item purchases and sales, updating the player's gold and inventory accordingly.

This module is essential for enhancing player experience by providing a dynamic and interactive way to manage resources in the game.

Functions:
- ShopMenu: Displays the shop interface where players can select options to buy or sell items.
- LoadShopInventory: Loads items available for purchase from a specified inventory file, generating random buy prices.
- LoadShopNeeds: Loads items that the shop needs from a specified file, generating random sell prices.
- BuyItems: Enables the player to purchase items, updating their inventory and gold.
- SellItems: Allows the player to sell items from their inventory, updating their gold and inventory as necessary.
'''

from src.modules.MainMenu import ConsoleInput, ClearConsole
from src.modules.ArtAssets import DisplayPlanet
from src.modules.TextFormatter import MenuLine

from src.classes.Player import Player

import random

def ShopMenu(player: Player) -> None:
    """
    Displays the shop interface where players can select options to buy or sell items.

    Parameters:
        player (Player): The character save that the user plays the game with.
    """

    while True:
        ClearConsole()
        DisplayPlanet()
        MenuLine()
        print(" ^ The Medieval World Shoppe")
        MenuLine()
        print(" 1. Buy Items")
        print(" 2. Sell Items")
        print(" 3. Leave Shop")
        MenuLine()

        print(" * Please select an option from the menu above...")
        MenuLine()
        choice = ConsoleInput()

        if choice == "1":
            BuyItems(player)
        elif choice == "2":
            SellItems(player)
        elif choice == "3":
            return
        else:
            return
        
def LoadShopInventory(file_path: str = '.\\config\\shopInventory.txt') -> list:
    """
    Loads items available for purchase from a specified inventory file, generating random buy prices.

    Parameters:
        file_path (str): The path to the shop items file.

    Returns:
        items (list): A list of dictionaries representing items available in the shop.
    """
    
    selling_items = []

    with open(file_path, 'r') as file:
        for line in file:
            name, min_price, max_price = line.strip().split(', ')
            min_price, max_price = int(min_price), int(max_price)
            buy_price = random.randint(min_price, max_price)
            selling_items.append({
                'name': name,
                'sell_price': buy_price
            })

    return selling_items

def LoadShopNeeds(file_path: str = '.\\config\\shopNeeds.txt') -> list:
    """
    Loads items that the shop needs from a specified file, generating random sell prices.

    Parameters:
        file_path (str): The path to the shop items file.

    Returns:
        items (list): A list of dictionaries representing items available in the shop.
    """

    buying_items = []

    with open(file_path, 'r') as file:
        for line in file:
            name, min_price, max_price = line.strip().split(', ')
            min_price, max_price = int(min_price), int(max_price)
            sell_price = random.randint(min_price, max_price)
            buying_items.append({
                'name': name,
                'sell_price': sell_price
            })

    return buying_items

def BuyItems(player: Player) -> None:
    """
    Enables the player to purchase items, updating their inventory and gold.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
    """
    
    shop_inventory = LoadShopInventory()

    # Randomly select 5 items from the shop selling items
    items_to_display = random.sample(shop_inventory, min(5, len(shop_inventory)))

    ClearConsole()
    DisplayPlanet()
    MenuLine()
    print(" ^ Buy from the Medieval World Shoppe")
    MenuLine()
    print(f" - Gold: {int(player.gold)}")
    MenuLine()

    # Loop through the selected items 
    for index, item in enumerate(items_to_display, start=1):
        print(f" {index}. {item['name']} @ {item['sell_price']}g each")

    MenuLine()
    # Ask the player what item to buy
    print(f" * Choose an item to buy using the leading number.")
    MenuLine()

    item_choice = ConsoleInput()

    # Exit if user doesn't enter in a number
    if item_choice == '':
        return

    # Get the selected item
    selected_item = items_to_display[int(item_choice) - 1]
    item_name = selected_item['name']
    item_price = selected_item['sell_price']

    # Ask the player how many of the item they want to buy
    MenuLine()
    print(f" * How many {item_name}s do you want to buy?")
    MenuLine()
    quantity_choice = ConsoleInput()

    try:
        quantity_choice = int(quantity_choice)

        # Check for valid quantity (should be greater than 0)
        if quantity_choice <= 0:
            raise ValueError("Quantity must be greater than zero.")

        total_cost = item_price * quantity_choice

        # Check if the player has enough gold
        if player.gold < total_cost:
            raise ValueError("Not enough gold")

        # Subtract the total cost from the player's gold
        player.gold -= total_cost

        if item_name in player.inventory:
            player.inventory[item_name]['count'] += quantity_choice
        else:
            player.inventory[item_name] = {'count': quantity_choice}

        MenuLine()
        print(f" * You bought {quantity_choice} {item_name}(s) for {total_cost}g!")
        MenuLine()
        print(f" - You now have {int(player.gold)}g.")
        MenuLine()
        print(" * Press enter to return to the shop menu...")
        MenuLine()
        ConsoleInput()
    except ValueError as ve:
        MenuLine()
        print(f" * Invalid selection: {ve}")
        MenuLine()
        ConsoleInput()
    except KeyError:
        MenuLine()
        print(f" * The item '{item_name}' is not in your inventory.")
        MenuLine()
        ConsoleInput()
    except TypeError:
        MenuLine()
        print(" * An error occurred with the item price. Please check the item details.")
        MenuLine()
        ConsoleInput()

def SellItems(player: Player) -> None:
    """
    Allows the player to sell items from their inventory, updating their gold and inventory as necessary.

    Parameters:
        player (Player): The character save file that the user goes through the game with.
    """

    shop_needs = LoadShopNeeds()

    ClearConsole()
    DisplayPlanet()
    MenuLine()
    print(" ^ Sell to the Medieval World Shoppe")
    MenuLine()
    print(f" - Gold: {int(player.gold)}")
    MenuLine()
    
    if not player.inventory:
        print(" - Your inventory is currently empty.")
        MenuLine()
        print(" * Press enter to return to the shop menu...")
        MenuLine()
        ConsoleInput()
        return

    # Loop through the inventory items
    for index, (item_name, details) in enumerate(player.inventory.items(), start=1):
        item_count = details['count']

        # Find the corresponding shop item to get the sell price
        shop_item = next((shop_item for shop_item in shop_needs if shop_item['name'] == item_name), None)
        if shop_item:
            print(f" {index}. {item_name} (x{item_count}) @ {shop_item['sell_price']}g each")
        else:
            print("ERROR: shopNeeds ")

    MenuLine()
    # Ask the player what item to sell
    print(f" * Choose an item to sell using the leading number.")
    MenuLine()

    item_choice = ConsoleInput()

    try:
        item_choice = int(item_choice) - 1
        if item_choice < 0 or item_choice >= len(player.inventory):
            raise ValueError
    except ValueError:
        return
    
    # Get the selected item
    selected_item_name = list(player.inventory.keys())[item_choice]
    selected_item = player.inventory[selected_item_name]

    # Ask the player how many of the item they want to sell
    max_quantity = selected_item['count']
    MenuLine()
    print(f" * How many {selected_item_name} do you want to sell? (1-{max_quantity})")
    MenuLine()
    quantity_choice = ConsoleInput()

    try:
        quantity_choice = int(quantity_choice)
        if quantity_choice < 1 or quantity_choice > max_quantity:
            raise ValueError
    except ValueError:
        return
    
    # Calculate the gold earned from the sale
    shop_item = next((shop_item for shop_item in shop_needs if shop_item['name'] == selected_item_name), None)
    if shop_item:
        total_gold = shop_item['sell_price'] * quantity_choice
        player.gold += total_gold
        player.inventory[selected_item_name]['count'] -= quantity_choice

        # Remove the item from inventory if count reaches zero
        if player.inventory[selected_item_name]['count'] <= 0:
            del player.inventory[selected_item_name]

        MenuLine()
        print(f" - You sold {quantity_choice} {selected_item_name} for {total_gold}g.")
        MenuLine()
        print(f" - You now have {int(player.gold)}g.")
        MenuLine()
        print(" * Press enter to return to the shop menu...")
        MenuLine()
        ConsoleInput()