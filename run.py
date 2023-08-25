# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
import time
import os


HEADER = "________________________________________________________________________________\n___________________________________BATTLESHIP___________________________________\n_____________________________________RESCUE_____________________________________\n________________________________________________________________________________\n"



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
    print(f"---------------------- Battleship Command Operations Deck ----------------------\n\nAmmunition Remaining   = {ammunition}\n\n[O] Misses             = {misses}\n[X] Enemy Ships Hit    = {enemy_ships_sunk_counter}  ({enemy_ships_afloat_counter} Remaining)\n[M] Merchant Ships Hit = {merchant_ships_sunk_counter}  ({merchant_ships_afloat_counter} Remaining)\n")
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

ammunition = 14

misses = 0

enemy_ships_afloat = [ship_locations[0], ship_locations[1], ship_locations[2], ship_locations[3], ship_locations[4]]  # The enemy ship locations are retrived from the first 5 elements of the ship_location variable
enemy_ships_sunk = []    # Array to hold coordinates of sunken enemy ships
enemy_ships_afloat_counter = len(enemy_ships_afloat) # Variable to count remaining ships
enemy_ships_sunk_counter = len(enemy_ships_sunk)  # Variable to count sunk ships

merchant_ships_afloat = [ship_locations[5], ship_locations[6]]        # The Merchant ships are retrieved from the last two elements in the ship_locations array
merchant_ships_sunk = []    # Array to hold coordinates of sunken merchant ships
merchant_ships_afloat_counter = len(merchant_ships_afloat)  # Variable to count remaining ships
merchant_ships_sunk_counter = len(merchant_ships_sunk)  # Variable to count sunk ships





# Code below here has been added to outline the pages leading up to displaying the game board to the user
# Project will be deployed in an unfinished state due to time constraints
# This game is not currently playable. These lines of code are temporary. The project will continue to be developed in order to resubmit.

time.sleep(1)
print(HEADER)


name = input("\n\n\n\n                                Enter Username:\n")

while len(name) > 10 or len(name) < 2:         # A while loop is used here to perform a validation check on the username input and ensures it is between 2 and 10 characters before being accepted
    os.system('cls' if os.name == 'nt' else 'clear')
    print(HEADER)
    time.sleep(.25)
    name = input("\n\n\n\n           Please enter a valid username between 2 and 10 characters:\n")

print('                               Username accepted')    # A confirmation is displayed to the user once the username has been accepted

    

MISSION_MESSAGE = f"                  Above Top Secret: For {name}'s eyes only.\n\nYour mission is to intercept and destroy a fleet of 5 enemy Destroyers \nthat are currently in pursuit of 2 friendly Merchant ships sailing for our \nNorthern Port. These Merchant ships are on a clandestine mission to deliver \nclassified cargo that will turn the tide of this war once and for all!\n\nUnfortunately, during a recent skirmish, the Merchant ships lost all \ncommunication capabilities and the Enemy's radar jamming technology is \npreventing us from locating them. But we know they're out there, somewhere.\n\nHunt down the enemy with extreme prejudice. Avoid friendly fire at all costs. \n\nRescue the Merchant Ships. Losing that cargo, means losing the war!\n"
time.sleep(.4)


time.sleep(.4)

print('\n\n                           Retreiving Mission Details\n\n')

time.sleep(1.2)

os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(.5)

print(HEADER)

print(MISSION_MESSAGE)


mission_accept_valid_response = False

while not mission_accept_valid_response:    # A while loop is used again here to perform a validation check on the user input for the 'Accept Mission' screen and ensures the input is either 'Yes' or 'No'
    response = input("\n                         Accept Mission? (Yes or No)\n")
    if response.lower() == 'yes' or response.lower() == 'no':
        mission_accept_valid_response = True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(HEADER)
        print(MISSION_MESSAGE)

if response.lower() == "no":    # An if statement is used here to exit the program if the user inputs 'No' as the answer on the 'Accept Mission' screen
    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(HEADER)
    print("\n\n\n\n\n\n\n\n\n                 This war will be won only by those with the \n                   courage to take the fight to the enemy.")
    time.sleep(6)
    exit()
 

time.sleep(.5)

os.system('cls' if os.name == 'nt' else 'clear')

print_game_board()

row_fire_upon = input('\nSELECT ROW/LONGITUDE TO FIRE UPON:\n')

column_fire_upon = input('\nSELECT COLUMN/LATITUDE TO FIRE UPON:\n')



column_fire_coordinate = column_fire_upon
row_fire_coordinate = row_fire_upon

time.sleep(.5)

fire_upon_status = ('                    **** YOU SUNK AN ENEMY DESTROYER ****')

print(fire_upon_status)
print(enemy_ships_afloat_counter)