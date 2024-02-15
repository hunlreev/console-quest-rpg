'''
Module Name: console_art.py
Description: Contains the strings of ASCII art used in the game.
Author: Hunter Reeves
Date: 2024-02-15
'''

def art_birthsign():
    """
    Prints art of stars for the birthsign menu

    Parameters:
        None.

    Returns
        None.
    """

    stars = """
 o              .        .                .          .           o       .                     
       .           |   .       o      .         .         o
   *          o   -O-                   .               .      *       .    
                   |  .         .              .                          .
  .       .            *             o           |     *        .     * 
     *                                          -O-       . 
                   o      |     *                |            o        .
            *            -O-          .    *                              .
   .    o                 |                               .         .
                .              .             o    *    .
    |                   *                  .                       o
   -O-        .          .         .               .      .              |
    |    .          o             .              o               .      -O-
  .          *                o           .             .   *            |
                 .        ,            ,                o         .              
"""

    print(stars)

def art_race():
    """
    Prints art of a planet and stars for the race menu.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    planet = """
 o              .        ___---___                    .                     
       .              .--\        --.     .     .         .         o
                    ./.;_.\     __/~ \.    
                   /;  / `-'  __\*   . \                                  .
  .       .       / ,--'     / .   .;   \        |              .       
                 | .|       /*      __   |      -O-       . 
                |__/    __ |* . ;   \ | . |      |
                |      /  \\\\_  , . ;| \___|                              .
   .    o       |      \  .~\\\\___,--'     |           .         .
                 |     | . ; ~~~~\_    __|
    |             \    \   .  .^ ; \  /_/   .                       o
   -O-        .    \   /     ^ ^ ^. |  ~/                  .             |
    |    .          ~\ \   .   ^^ /  /~          o               .      -O-
  .                   ~--___ ; ___--~                   .                |
                 .          ---         .              
"""                 

    print(planet)

def art_main_menu():
    """
    Prints the dragon art at the top of the menu.
    
    Parameters:
        None.
    
    Returns:
        None.
    """

    # ASCII Art by Adrian Elhart
    dragon = """

              /|                                           |\                 
             /||             ^               ^             ||\                
            / \\\\__          //               \\\\          __// \               
           /  |_  \         | \   /     \   / |         /  _|  \              
          /  /  \  \         \  \/ \---/ \/  /         /  /     \             
         /  /    |  \         \  \/\   /\/  /         /  |       \            
        /  /     \   \__       \ ( 0\ /0 ) /       __/   /        \           
       /  /       \     \___    \ \_/|\_/ /    ___/     /\         \          
      /  /         \_)      \___ \/-\|/-\/ ___/      (_/\ \      `  \         
     /  /           /\__)       \/  oVo  \/       (__/   ` \      `  \        
    /  /           /,   \__)    (_/\ _ /\_)    (__/         `      \  \       
   /  '           //       \__)  (__V_V__)  (__/                    \  \      
  /  '  '        /'           \   |{___}|   /         .              \  \     
 /  '  /        /              \/ |{___}| \/\          `              \  \    
/     /        '       .        \/{_____}\/  \          \    `         \  \   
     /                ,         /{_______}\   \          \    \         \     
                     /         /{___/_\___}\   `          \    `     
    """

    print(dragon)