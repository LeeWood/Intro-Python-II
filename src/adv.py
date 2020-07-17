from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Link', room['outside'])

#print(player1.current_room)

#print(room['outside'].n_to)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def adventureGameStart():
    #welcome message
    print(f'Welcome, {player1.name}!')
    print(f'You find yourself at a mysterious cave entrance...how will you begin your adventure?')
    #* here if user goes in any direction other than north, print error message..."Are you sure?"

    while True:
        move = input('Which direction do you want to go? \n [N] North  [S] South  [E] East  [W] West  [Q] Quit \n :')
        #* need to chage this so that user input is NOT case sensitive

        if move == "N":
            player1.current_room = player1.current_room.n_to
            print(player1.current_room)

        elif move == "S":
            player1.current_room = player1.current_room.s_to
            print(player1.current_room)

        elif move == "E":
            player1.current_room = player1.current_room.e_to
            print(player1.current_room)

        elif move == "W":
            player1.current_room = player1.current_room.w_to
            print(player1.current_room)

        elif move == "Q":
            print("Game over!")
            break

        else:
            print("Please make a valid selection.")

        #* I need error handling for if there is no option to go a certain direction based on the player's current position.    

            

adventureGameStart()    

