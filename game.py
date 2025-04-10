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
        self.health = 100 #TODO change this back to 100 
        self.has_map = False
        self.has_lantern = False

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
   
def add_to_inventory(player, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")




# TODO: Create a function stay_still(player)
#       - Subtract 10 health when the player stays still

def stay_still(player):
    print("You stay still, but the cold saps your energy...")
    player.health -= 10
    


# TODO: Create a function check_win(player)
#       - If "treasure" and "rare herbs" are both in inventory, print win message and exit

def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print(f"Congratulations, {player.name}! You have found the treasure and rare herbs!")
        print("You win!")
        exit() 



# TODO: Create a function check_lose(player)
#       - If health is 0 or lower, print lose message and exit

def check_lose(player):
    if  player.health <= 0:
        print(f"Sorry, {player.name} you have lost of all of your health.")
        print("You lose")
        exit()

# TODO: Show the player's current health after every action
# TODO: Continue using good Git habits: save, commit, push!
# TODO: Final commit message example: "COMPLETE Final Adventure Game"

#---------------------------------------------------------------
#main program starts here
#---------------------------------------------------------------

def explore_dark_woods(player):
    if decision == "1":
        print(f"{player.name}, you step into the dark woods...")
        if "lantern" not in player.inventory: 
            add_to_inventory(player, "lantern")
            player.has_lantern = True
        else: 
            print("You already have a lantern.")
    

# TODO: Create a function called explore_mountain_pass(player)
#       - Print area description
#       - Add "map" to inventory if not already collected
def explore_mountain_pass(player):
    if decision == "2":
        print(f"{player.name}, you make your way "
              "towards the mountain pass, and there you find a map")
        if "map" not in player.inventory:
            add_to_inventory(player, "map")
            player.has_map = True 
        else: 
            print("You already have a map.")
        
# TODO: Create a function called explore_cave(player)
#       - If player.has_lantern: allow entry and add "treasure"
#       - Else: warn that it's too dark
def explore_cave(player):
    if decision == "3":
        print(f"{player.name}, you bravely head towards the dark cave")
        if player.has_lantern == False:
            player.health -= 10
            print("It's too dark to continue without a lantern.")
            print("Your fear alone saps health from you.")
        else:
            print (f"{player.name}, you head into the cave and see treasure inside.")
            if "treasure" not in player.inventory:
                add_to_inventory(player, "treasure")
                player.has_treasure = True
            else:
                print("You already have treasure, you greedy swine.")



def explore_hidden_valley(player):
    if decision == "4":
        if player.has_map == False:
            player.health -= 10
            print("You cannot find the hidden valley without a map.")
            print("Your own stupidity makes you question your qualifications and gives you a headache. This saps your health.")
        else:
            print (f"{player.name}, you follow the map to find the hidden valley and you stumble upon some rare herbs!")
            if "rare herbs" not in player.inventory:    
                add_to_inventory(player, "rare herbs")
                # player.has_herbs = True 
            else:
                print("""You have already gathered all the herbs in this area. 
                      You have caused an extinction of an endangered species.
                      May this adventure be worth the trail you leave behind.""")


player = welcome_player()
describe_area()

# Start the game Loop
while True:
    print("\nYou see several paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Head straight into the cave.")
    print("\t4. Look for a hidden valley.")
    print("\t5. Stay where you are.")
    print("\t6. Type 'i' to check your inventory.")
    print(f"Your health is now", player.health)

    decision = input("What will you do (1,2,3, 4 or i): ").lower()
# open the inventory


    if decision == "i":
        print("Inventory",player.inventory) 
        continue # Skip to the next iteration of the loop

#take the left path  - Dark woords
    if decision == "1":
        explore_dark_woods(player)
        
#take the right path - Mountain 
    if decision == "2":
        explore_mountain_pass(player)

#take the path straight ahead - cave
    if decision == "3":
        explore_cave(player)
       
#take the path to the hidden valley
    if decision == "4":
        explore_hidden_valley(player)


#stay where you are 
    elif decision == "5":
        print("You stay still, listening to the "
              "distant sounds of the forest")
        stay_still(player)
    else:
        print("Invalid choice. Please choose "
              "1, 2, 4, or 5.")
        
    
# win condition 
    check_win(player)

#lose condition 
    check_lose(player)
   
    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break # Exit the loop and end the game