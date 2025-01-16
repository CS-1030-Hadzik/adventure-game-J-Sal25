# welcome messange and introduction
# THis is a text based adventure game  
'''Adventure Game 
Author: Josue Salazar 
Version : 1.0
Description: This is a text-based adventure game where the player makes choices to navigate through a mysterious forest
'''
print("Welcome to the Adventure Game!")
print("Your journey begins here...") 

# ask for the players name 
player_name = input ("what is your name, adventurer?")

#Concatenate strings to create a personalized message 
print ("Welcome, " + player_name + "! Your journey begins now.") 

#use an f-string to display the same message in a more readable way 

print (f"Welcome, {player_name}! Your journey begins now.")

#describe the starting area 
starting_area = """"
You Find yourself in a dark forest. The sound of rustling leaves fills the air. A faint path lies ahead, leading deeper into the unknown...
"""
print (starting_area)

#ask the player for their first decison
decision = input ("Do you wish to take the path? (yes or no): ").lower ()

#respond based on the players decison 

if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print (player_name + ", you decide to wait. Perhaps courage will find you later.") #concatenation exapmple
else: print ("Confused, you stand still, unsure of what to do")
