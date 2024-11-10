# Console Quest RPG - Patches and Updates
All versions of Console Quest RPG will be documented here, along with the changelog and bug fixes.

## Version 0.2.2-pre (Date Finished - 11/10/2024)
- Refactored the Enemy class
- Refactored the Player class
- The type of enemy is no longer tied to the player's location and is entirely random now
- Changed wording of "sex" in character creation to "gender" and added more options for diversity purposes
- Added damage amount indicators during encounters so you can see what damage is being dealt.
- Tweaked wording of the combat encounter messages as well, cleaned up that code a bit.
- Updated the enemy scaling so the enemy attributes scale up with the player's level.
- Minor tweaks, changes, and bug fixes (as always)
- Removed Herobrine

## Version 0.2.1-pre (Date Finished - 10/13/2024)
- Refactored the entire codebase, naming conventions, etc.
- Added more docstring and cleaned up method declarations
- Reorganized code structure a bit more too
- Updated the file structure so it can handle growing as a project
- Minor tweaks, changes, and bug fixes (as always)
- Removed Herobrine

## Version 0.2.0-pre (Date Finished - 08/10/2024)
- Added a shop to sell and buy items from
- Shop inventory automatically refreshes with a list of 5 items
- Added a repository of items and prices for the shop to sell
- Prices dynamically change each time you enter it
- Added gold player data to sell/buy menus
- Reworked prices to be set by shop instead of on enemy drop
- Added current attribute points on level up for reference
- Minor tweaks, changes, and bug fixes (as always)

## Version 0.1.2-pre (Date Finished - 03/13/2024)
- Added a basic inventory management system
- Added potential drops from enemies
- Player can view their inventory
- Player can obtain drops from enemies
- Refactored a bit of code
- Changed an absolute path to a relative path
- Adjusted how the level cap works
- Minor tweaks, changes, and bug fixes (as always)

## Version 0.1.1-pre (Date Finished - 03/03/2024)
- Adjusted health, mana, stamina, and exp display bars
- Added colors to the display bars for each stat
- Minor tweaks, changes, and bug fixes (as always)

## Version 0.1.0-pre (Date Finished - 03/01/2024)
- Changed display to allow for stat bars for health, mana, and stamina
- Added functionality to be able to delete existing saves as well
- Added functionality to see stats at any time during the game
- Added rest functionality based on Speed and Agility attribute
- Added level up functionality and updates to all stats to reflect level up
- Added experience bar and adjusted the length of the bars
- Added locations to travel to
- Added enemies and fully implemented combat
- Minor tweaks, changes, and bug fixes (as always)

## Version 0.0.1-pre (Date Finished - 02/29/2024)
- Started the project, git-hub repo, basic file structure setup, etc
- Implemented a main menu with options such as new game, load game, about game, and quit game
- Added character creation with name, race, birthsign, and class
- Create a Player object with all information obtained through character creation
- Added a menu once the game starts after character creation to allow the player to continue, save progress, or quit
- Added functionality to to load an existing character in the "saves" folder
- Minor tweaks, changes, and bug fixes (as always)