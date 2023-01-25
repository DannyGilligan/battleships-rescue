
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

HEADER = "\n___________________________________BATTLESHIP___________________________________\n_____________________________________RESCUE_____________________________________\n"

WELCOME_MESSAGE = "Beyond Top Secret: For Danny's eyes only.\n\nYour mission is to intercept and destroy a fleet of 5 enemy Destroyers \nthat are currently in pursuit of 2 friendly Merchant ships sailing for our \nNorthern Port. These Merchant ships are on a clandestine mission to deliver \nclassified cargo that will turn the tide of this war once and for all!\n\nUnfortunately, during a recent skirmish, the Merchant ships lost all \ncommunication capabilities and the Enemy's radar jamming technology is \npreventing us from locating them. But we know they're out there somewhere.\n\nHunt down the enemy with extreme prejudice. Avoid friendly fire at all costs. \n\nRescue the Merchant Ships. Losing their cargo, means losing the war!\n"

DEFAULT_SYMBOL = "~"                            #Defualt symbol (as close to a wave as I could find!)
ENEMY_HIT_SYMBOL = "X"                          #Symbol to denote a hit on an enemy ship
MISS_SYMBOL = "O"                               #Symbol to denote a miss
MERCHANT_HIT_SYMBOL = "M"                       #Symbol to denote a hit on a friendly merchant ship

ROWS = 7                                        #Y axis (the rows will be counted vertically)
COLS = 7                                        #X axis (the columns will be counted horizontally)

GAME_BOARD = []                                 #Empty list to hold the list of lists that will form the game board

for row in range(ROWS):                         #For loop to generate rows on the game board based on the ROWS value
    GAME_BOARD.append([DEFAULT_SYMBOL] * COLS)  #Code to create the 'column' elements within each row array by appending a '~' symbol as a placeholder multiplied by the COLS value




