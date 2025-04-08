'''
DOCSTRING
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

#---------------------------------------------------------------
#global inventory list
# this will hold items the player collects
#---------------------------------------------------------------
inventory = []



# TODO: Define a function called welcome_player() that:
#       - Prints a welcome message
#       - Asks the user for their name using input()
#       - Welcomes the user using an f-string
#       - Returns the player's name

#---------------------------------------------------------------
# Function: welcome_player
#greets the palyer, asks for thei name, 
#and rethruns the name as a string
#---------------------------------------------------------------
def welcome_player():
    print("Welcome to the Adventure Game!")
    print('Your journey begins here... ')
    player_name = input("What is your name, adventurer? ")
    print(f"Welcome, {player_name}! Your journey begins now.")
    return player_name

def describe_area():

    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown...""")
   
def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up a {item}!")


player_name = welcome_player()
describe_area()

# Start the game Loop
while True:
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\t4. Type 'i' to check your inventory.")

    decision = input("What will you do (1,2,3 or i): ").lower()

    if decision == "i":
        print("Inventory",inventory) 
        continue # Skip to the next iteration of the loop


    if decision == "1":
        print(f"{player_name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
        add_to_inventory("lantern")
    elif decision == "2":
        print(f"{player_name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("map")
    elif decision == "3":
        print("You stay still, listening to the "
              "distant sounds of the forest")
    else:
        print("Invalid choice. Please choose "
              "1, 2, or 3.")
   
    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player_name} "
              "See you next time.")
        break # Exit the loop and end the game