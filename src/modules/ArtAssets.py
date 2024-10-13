'''
Contains functions to display ASCII art used throughout the game.

This module provides a collection of functions that render various ASCII art representations 
for different characters, items, and themes within the Console Quest RPG. Each function is dedicated 
to displaying a specific piece of art, enhancing the visual experience for players and adding 
flair to the game's presentation.

Functions:
- DisplaySkull: Displays ASCII art representing a skull.
- DisplayRogue: Displays ASCII art representing a rogue character.
- DisplayMage: Displays ASCII art representing a mage character.
- DisplayWarrior: Displays ASCII art representing a warrior character.
- DisplayBattleAxe: Displays ASCII art of a battle axe.
- DisplayStars: Displays ASCII art of stars for decorative purposes.
- DisplayPlanet: Displays ASCII art for a race menu.
- DisplayDragon: Displays ASCII art of a dragon.
'''

def DisplaySkull() -> None:
    """
    Displays ASCII art representing a skull.
    """

    skull = """
                 .... NO! ...                  ... MNO! ...
               ..... MNO!! ...................... MNNOO! ...
              ..... MMNO! ......................... MNNOO!! .
            .... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
             ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
              ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
             ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
              . ....... MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
                ....... MMMMM..    OPPMMP    .,OMI! ....
                 ...... MMMM::   o.,OPMP,.o   ::I!! ...
                     .... NNM:::.,,OOPM!P,.::::!! ....
                      .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
                     ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
                       .. MMMMMNNOOMMNNIIIPPPOO!! ......
                      ...... MMMONNMMNNNIIIOO!..........
                   ....... MN MOMMMNNNIIIIIO! OO ..........
                ......... MNO! IiiiiiiiiiiiI OOOO ...........
              ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
               .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
               ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
                  ...... OO! ................. ON! .......
                      ................................
"""

    print(skull)

def DisplayRogue() -> None:
    """
    Displays ASCII art representing a rogue character.
    """

    rogue = """
                         _,._
                       ,'   ,`-.
            |.        /     |\  `.
            \ \      (  ,-,-` ). `-._ __
             \ \      \|\,'     `\  /'  `\\
              \ \      ` |, ,  /  \ \     \\
               \ \         `,_/`, /\,`-.__/`.
                \ \            | ` /    /    `-._
                 \\\           `-/'    /         `-.
                  \\`/ _______,-/_   /'             \\
                 ---'`|       |`  ),' `---.  ,       |
                  \..-`--..___|_,/          /       /
                             |    |`,-,...,/      ,'
                             \    | |_|   /     ,' __  r-'',
                              |___|/  |, /  __ /-''  `'`)  |
                           _,-'   ||__\ /,-' /     _,.--|  (
                        .-'       )   `(_   / _,.-'  ,-' _,/
                         `-------'       `--''       `'''
"""

    print(rogue)

def DisplayMage() -> None:
    """
    Displays ASCII art representing a mage character.
    """

    mage = """
                                      _,-'|
                                   ,-'._  |
                         .||,      |####\ |
                        \.`',/     \####| |
                        = ,. =      |###| |
                        / || \    ,-'\#/,'`.
                          ||     ,'   `,,. `.
                          ,|____,' , ,;' \| |
                         (3|\    _/|/'   _| |
                          ||/,-''  | >-'' _,\\
                          ||'      ==\ ,-'  ,'
                          ||       |  V \ ,|
                          ||       |    |` |
                          ||       |    |   \\
                          ||       |    \    \\
                          ||       |     |    \\
                          ||       |      \_,-'
                          ||       |___,,--")_\\
                          ||         |_|   ccc/
                          ||        ccc/
                          ||                
"""

    print(mage)

def DisplayWarrior() -> None:
    """
    Displays ASCII art representing a warrior character.
    """

    warrior = """
                        /\\
                        ||
                        ||
                        ||
                        ||          \{\}
                        ||          .--.
                        ||         /.--.\\
                        ||         |====|
                        ||         |`::`|
                       _||_    .-;`\..../`;_.-^-._
                        /\   /  |...::..|`   :   `|
                       |:'\ |   /'''::''|   .:.   |
                        \ /\;-,/\   ::  |..:::::..|
                         \ <` >  >._::_.| ':::::' |
                          `""`  /   ^^  |   ':'   |
                                |       \    :    /
                                |        \   :   /
                                |___/\___|`-.:.-`
                                 \_ || _/    `
                                 <_ >< _>
                                 |  ||  |
                                 |  ||  |
                                _\.:||:./_
                               /____/\____\\
"""

    print(warrior)

def DisplayBattleAxe() -> None:
    """
    Displays ASCII art of a battle axe.
    """

    battleaxe = """
                                                _.gd8888888bp._
                                             .g88888888888888888p.
                                            .d8888P""       ""Y8888b.
                                           "Y8P"               "Y8P'
                                             `.               ,'
                                               \     .-.     /
                                                \   (___)   /
     .------------------._______________________:__________j
     /                   |                      |           |`-.,_
     \###################|######################|###########|,-'`
     `------------------'                       :    ___   l
                                                /   (   )   \\
                                               /     `-'     \\
                                             ,'               `.
                                          .d8b.               .d8b.
                                          "Y8888p..       ,.d8888P"
                                            "Y88888888888888888P"
                                               ""YY8888888PP""
"""

    print(battleaxe)

def DisplayStars() -> None:
    """
    Displays ASCII art of stars for decorative purposes.
    """

    stars = """
 o              .        .                .          .           o     .                     
       .           |   .       o      .         .         o
   *          o   -O-                   .               .      *      .    
                   |  .         .              .                        .
  .       .            *             o           |     *        .     * 
     *                                          -O-       . 
                   o      |     *                |            o       .
            *            -O-          .    *                            .
   .    o                 |                               .         .
                .              .             o    *    .
    |                   *                  .                       o
   -O-        .          .         .               .      .            |
    |    .          o             .              o               .    -O-
  .          *                o           .             .   *          |
                 .        ,            ,                o         .              
"""

    print(stars)

def DisplayPlanet() -> None:
    """
    Displays ASCII art for a race menu.
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

def DisplayDragon() -> None:
    """
    Displays ASCII art of a dragon.
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