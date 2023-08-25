# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
import time
import os


HEADER = "\n___________________________________BATTLESHIP___________________________________\n_____________________________________RESCUE_____________________________________\n________________________________________________________________________________\n"



DEFAULT_SYMBOL = "~"           # Default symbol
ENEMY_HIT_SYMBOL = "X"         # Hit on an enemy ship
MISS_SYMBOL = "O"              # Denotes a miss
MERCHANT_HIT_SYMBOL = "M"      # Denotes hit on friendly merchant ship

ROWS = 7            # Y axis (the rows will be counted vertically)
COLS = 7            # X axis (the columns will be counted horizontally)

GAME_BOARD = []     # Empty list to hold the list of lists for board

for row in range(ROWS):                         # To generate board rows
    GAME_BOARD.append([DEFAULT_SYMBOL] * COLS)  # Code to create the 'column' elements within each row array by appending a '~' symbol as a placeholder multiplied by the COLS value

def print_game_board():
    """
    This function will generate a dynamically sized game board based on the number of rows and columns determined by the user's input
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Code from stack overflow forum on how to clear screen
    print("---------------------- Battleship Command Operations Deck ----------------------\n\nAmmunition Remaining   = \n\n[O] Misses             = O\n[X] Enemy Ships Hit    = X  (*5* Remaining)\n[M] Merchant Ships Hit = M  (*2* Remaining)\n")
    col_headers = []                             # Empty array to hold the column header values based on the userinput
    for i in range(COLS):                        # Iterates based on the range dictated by the user input  
        col_headers.append(i)                    # Appends the column header numbers to the array 
    col_headers.insert(0, " ")                   # NOTE FOR BUG, HAD TO INDENT THIS OUTSIDE OF THE LOOP, and insert a blank space so it would align
    print("                             ", *col_headers, sep = ' ')       # Breaks out the column headers from the array and prints horizontally

    row_counter = 0
    for row_array in GAME_BOARD: 
        print("                             ", row_counter, end = " ")
        row_counter += 1
        for col_elem in row_array:
            print(col_elem, end = " ")
        print()

GAME_BOARD[4][3] = ENEMY_HIT_SYMBOL

def ship_generator():
    """
    Generates random locations for ships
    """
    ships = []                      # Creates an empty array to store locations
    while len(ships) < 7:           # While loop that will terminate after 7 ships created
        xy = str(randint(0, ROWS)) + ',' + str(randint(0, COLS))  # Creates random x,y coordinates on each loop
        if xy not in ships:         # Checks if location is not already in the array
            ships.append(xy)        # Appends location to ship array
    return ships                    # Returns the values

ship_locations = ship_generator()   # Assigns generated locations to variable

enemy_ship_locations = [ship_locations[0], ship_locations[1], ship_locations[2], ship_locations[3], ship_locations[4]]  # The enemy ship locations are retrived from the first 5 elements of the ship_location variable
merchant_ship_locations = [ship_locations[5], ship_locations[6]]        # The Merchant ships are retrieved from the last two elements in the ship_locations array


# Code below here has been added to outline the pages leading up to displaying the game board to the user
# Project will be deployed in an unfinished state due to time constraints
# This game is not currently playable. These lines of code are temporary. The project will continue to be developed in order to resubmit.

time.sleep(1)
print(HEADER)

def name_validation(name):
    return len(name) > 3 and < 10

name = input("\n\n\n\n                                Enter Username:\n")

if name_validation(name):
    print('                               Username accepted')
else:
    print('               Please enter a valid username between 3 and 10 characters')

MISSION_MESSAGE = f"                  Above Top Secret: For {name}'s eyes only.\n\nYour mission is to intercept and destroy a fleet of 5 enemy Destroyers \nthat are currently in pursuit of 2 friendly Merchant ships sailing for our \nNorthern Port. These Merchant ships are on a clandestine mission to deliver \nclassified cargo that will turn the tide of this war once and for all!\n\nUnfortunately, during a recent skirmish, the Merchant ships lost all \ncommunication capabilities and the Enemy's radar jamming technology is \npreventing us from locating them. But we know they're out there, somewhere.\n\nHunt down the enemy with extreme prejudice. Avoid friendly fire at all costs. \n\nRescue the Merchant Ships. Losing that cargo, means losing the war!\n"
time.sleep(.5)

# print('                               Username accepted')

time.sleep(.5)

print('\n\n                           Retreiving Mission Details\n\n')

time.sleep(1.5)

os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(.5)

print(HEADER)

print(MISSION_MESSAGE)

mission_accept = input("\n                              Accept Mission? Y/N\n")

time.sleep(.5)

os.system('cls' if os.name == 'nt' else 'clear')

print_game_board()

column_fire_upon = input('\nSELECT COLUMN TO FIRE UPON:\n')

row_fire_upon = input('SELECT ROW TO FIRE UPON:\n')

column_fire_coordinate = column_fire_upon
row_fire_coordinate = row_fire_upon

time.sleep(.5)

fire_upon_status = ('                    **** YOU SUNK AN ENEMY DESTROYER ****')

print(fire_upon_status)