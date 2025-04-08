'''
DOCSTRING
Adventure Game
Author: Scott Hadzik
Version: 2.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''
#---------------------------------------------------------------
#player class to store player info and game state
#---------------------------------------------------------------

class Player: 
    # initializer  -constructor
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False


# TODO: Commit and push your code with a message like:
#       REF player class added and game state flags implemented



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
    name = input("What is your name, adventurer? ")

    player = Player(name)
    
    print(f"Welcome, {player.name}! Your journey begins now.")
    return player

def describe_area():

    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown...""")
   
def add_to_inventory(item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")


player = welcome_player()
describe_area()

# Start the game Loop
while True:
    print("\nYou see several paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Head straight into the cave.")
    print("\t4. Stay where you are.")
    print("\t5. Type 'i' to check your inventory.")

    decision = input("What will you do (1,2,3, 4 or i): ").lower()
# open the inventory


    if decision == "i":
        print("Inventory",player.inventory) 
        continue # Skip to the next iteration of the loop

#take the left path  - Dark woords
    if decision == "1":
        print(f"{player.name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
        add_to_inventory("lantern")
        player.has_lantern = True
        
#take the right path - Mountain 
    elif decision == "2":
        print(f"{player.name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("map")
        player.has_map = True

    elif decision == "3":
        if player.has_lantern == False:
            print("It's too dark to continue without a lantern.")
        else:
            print(f"{player.name}, bravely enter the dark cave")
            print(f"Inside the cave, you find hidden treasure.")


#stay where you are 
    elif decision == "4":
        print("You stay still, listening to the "
              "distant sounds of the forest")
    else:
        print("Invalid choice. Please choose "
              "1, 2, or 3.")
   
    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break # Exit the loop and end the game