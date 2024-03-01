'''
Module Name: core.py
Description: Contains core functions for all modules to use freely.
Author: Hunter Reeves
Date: 2024-03-01
'''

import os

def console_input():
    """
    Helper Function: Obtains user input in a pretty format.
    
    Parameters:
        None.
    
    Returns:
        user_input(str): The string entered by the user.
    """

    user_input = str(input(" > "))

    return user_input

def clear_console():
    """
    Helper Function: Clears the console/terminal of all text, a reset.
    
    Parameters:
        None.
        
    Returns:
        None.
    """

    os.system('cls' if os.name == 'nt' else 'clear')