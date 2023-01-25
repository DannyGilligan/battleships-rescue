# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

HEADER = "\n___________________________________BATTLESHIP___________________________________\n_____________________________________RESCUE_____________________________________\n"

WELCOME_MESSAGE = "Beyond Top Secret: For Danny's eyes only.\n\nYour mission is to intercept and destroy a fleet of 5 enemy Destroyers \nthat are currently in pursuit of 2 friendly Merchant ships sailing for our \nNorthern Port. These Merchant ships are on a clandestine mission to deliver \nclassified cargo that will turn the tide of this war once and for all!\n\nUnfortunately, during a recent skirmish, the Merchant ships lost all \ncommunication capabilities and the Enemy's radar jamming technology is \npreventing us from locating them. But we know they're out there somewhere.\n\nHunt down the enemy with extreme prejudice. Avoid friendly fire at all costs. \n\nRescue the Merchant Ships. Losing their cargo, means losing the war!\n"

DEFAULT_SYMBOL = "~"           # Defualt symbol
ENEMY_HIT_SYMBOL = "X"         # Hit on an enemy ship
MISS_SYMBOL = "O"              # Denotes a miss
MERCHANT_HIT_SYMBOL = "M"      # Denotes hit on friendly merchant ship

ROWS = 8            # Y axis (the rows will be counted vertically)
COLS = 8            # X axis (the columns will be counted horizontally)

GAME_BOARD = []     # Empty list to hold the list of lists for board

for row in range(ROWS):                         # To generate board rows
    GAME_BOARD.append([DEFAULT_SYMBOL] * COLS)  # Code to create the 'column' elements within each row array by appending a '~' symbol as a placeholder multiplied by the COLS value

def print_game_board():
    """
    This function will generate a dynamically sized game board based on the number of rows and columns determined by the user's input
    """
    print("---------------------- Battleship Command Operations Deck ----------------------\n\nAmmunition Remaining = \n\n[O] Misses =\n[X] Enemy Ships Hit = X     (*5* Remaining)\n[M] Merchant Ships Hit = M  (*2* Remaining)\n")
    col_headers = []                             # Empty array to hold the column header values based on the userinput
    for i in range(COLS):                        # Iterates based on the range dictated by the user input  
        col_headers.append(i)                    # Appends the column header numbers to the array 
    col_headers.insert(0, " ")                    # NOTE FOR BUG, HAD TO INDENT THIS OUTSIDE OF THE LOOP, and insert a blank space so it would align
    print("                             ", *col_headers, sep = ' ')                 # Breaks out the column headers from the array and prints horizontally

    row_counter = 0
    for row_array in GAME_BOARD: 
        print("                             ", row_counter, end = " ")
        row_counter += 1
        for col_elem in row_array:
            print(col_elem, end = " ")
        print()

GAME_BOARD[4][3] = ENEMY_HIT_SYMBOL

print_game_board()
