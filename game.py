''' 
This is a dosctring, a type of comment that isnt actually run in the code, Can be used with double quots "" or single quotes if its three in a row '
Adventure Game 
Author: Josue Salazar
Version 1.0 
Description: This is a text-based adventure game 
 This is a text based adventure game where the player makes choices to navigate through a mysterious forest.
 '''
 # the hashtag is used mainly for comments, same use as the quotation marks

'''Adventure Game 
Author: Josue Salazar 
Version : 1.0
Description: This is a text-based adventure game where the player makes choices to navigate through a mysterious forest
'''
print("Welcome to the Adventure Game!")
print("Your journey begins here...") 

# ask for the players name 
player_name = input ("what is your name, adventurer? ")

#Concatenate(combining) strings to create a personalized message 
print ("Welcome, " + player_name + "! Your journey begins now.") 

#use an f-string to display the same message in a more readable way 

print (f"Welcome, {player_name}! Your journey begins now.")

#describe the starting area 
starting_area = """" You Find yourself in a dark forest. The sound of rustling leaves fills the air. A faint path lies ahead, leading deeper into the unknown..."""
print (starting_area)

#start the game loop
while True: 
    print ("\nYou see two paths ahead:")
    print ("\t1. Take the left path into the dark woods.")
    print ("\t2. Take the right path towards the mountain pass.") 
    print ("\t3. Stay where you are.") 

    decision = input("What will you do (1,2,3): ") 

    if decision == "1": 
        print (f"{player_name}, you step into the dark woods. The trees whisper as you walk deeper. ") 
    elif decision == "2": 
        print (f"{player_name}, you make your way towards the mountain pass feeling the cold wind against your face.")
    elif decision == "3":
        print ("You stay still, listening to the distant sounds of the forest.")
    else:
        print("invalid choice, please choose 1, 2, or 3. ")

# ask if thye want to continue 
    play_again = input("Do you want to continue exploring? (Yes or no):").lower()
    if play_again != "yes": 
        print(f"Thanks for playing, {player_name}"
              "see you next time.")
        break #exit the loop and end the game 