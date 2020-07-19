from room import Room
from player import Player
from item import Item

#items dictionary
roomItems = {
    "note": Item("A note", "You assume it was left by the previous adventurers. The note reads: 'We may have taken this treasure, but if you can defeat the beast across the Grand Overlook you will be rewarded greatly.'"),

    "ladder": Item("A ladder", "An old, but very sturdy 15 foot wooden ladder."),

    "amulet": Item("An amulet", "A blue and white Nazar amulet shaped like an eye. It's said to protect against the evil eye.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [roomItems["ladder"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [roomItems["amulet"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [roomItems["note"]]),
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

player1 = Player('Link', room['outside'], [Item("A journal page", "An old withered page from your great aunt's journal that reads:\n 'Seek gold in the northern caves'.")])

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

def adventureGame():
    #WELCOME MESSAGE
    print(f'\nWelcome, {player1.name}!')
    print(f'This is the beginning of your greatest feat yet! {player1.current_room.description}...how will you begin your adventure?\n')

    #GAME LOOP START
    while True:
        move = input('What would you like to do? \n[N] Go North  [S] Go South  [E] Go East  [W] Go West  [Take + item] Take Item  [Drop + item] Drop Item  [I] See Inventory  [Q] Quit \n :').lower()

        #Checks if use is entering one or two words in input
        def isSingleStr(str):
            return len(str.split()) < 2

        if move == "n" and isSingleStr(move) and hasattr and (player1.current_room, 'n_to'):
            player1.current_room = player1.current_room.n_to
            print(f'\n{player1.current_room} \n')

        elif move == "s" and isSingleStr(move) and hasattr:
            player1.current_room = player1.current_room.s_to
            print(f'\n{player1.current_room} \n')

        elif move == "e" and isSingleStr(move) and hasattr:
            player1.current_room = player1.current_room.e_to
            print(f'\n{player1.current_room} \n')

        elif move == "w" and isSingleStr(move) and hasattr:
            player1.current_room = player1.current_room.w_to
            print(f'\n{player1.current_room} \n')

        elif move == "i" and isSingleStr(move):
            print(f"\nInventory:\n{player1.get_inventory()}\n")        

        elif move == "q" and isSingleStr(move):
            print(f'\nAdventure over!')
            break

        elif move.startswith("take".lower()):
            try:
                player1.get_item(roomItems[move.split()[1]])
            except KeyError:
                print("that item is not in this area")  

        elif move.startswith("drop".lower()):
            try:
                player1.drop_item(roomItems[move.split()[1]])
            except KeyError:
                print("You don't have this item in your inventory.")              

        else:
            print(f"\nYou can't go this way. Try going a different direction.")

# GAME START
adventureGame()
