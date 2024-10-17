#Programmer:  Hazel Osborne
# Course:  CS151, Zelalem Yalew
# Due Date: 10/16/2024
# PA Assignment: 2
# Problem Statement: Game of Sticks, 2 players 1 computer
# Data In: number of sticks
# Data Out: losses

#Import random
import random
#Output Introduction to User
print("-"*100)
print("Welcome to the Game of Sticks!")
print("Played with 2 players and the computer! \n ")

print("The game starts with some number of sticks on the table (between 10 and 100, chosen by the user) \n"
      "Three players take turns choosing how many sticks to take. \n" 
      "On each player’s turn they must take either 1, 2, or 3 sticks. \n"
      "The player to take the last stick loses.")
print("-"*100)

#Set all losses to 0
player_1_loss = 0
player_2_loss = 0
computer_loss = 0
loser = ""
#Set total_sticks to 0

#Set play_choice as empty string
play_choice = ""
play_choice = str(play_choice)

#Prompt user to enter the number of sticks they want to play with
total_sticks = int(input("How many sticks would you like to play with? (10-100): "))

#Error check that total_sticks is valid
while not 10 <= total_sticks <= 100:
    total_sticks = int(input("Invalid input. Please enter a number from 10-100): "))

#Only continue if they still want to play
while play_choice != "no":

    turn = 1

#Runs game till sticks have run out
    while not total_sticks < 1:
#Player 1's turn
        if turn == 1 :
            sticks_removed = int(input("Player 1, Please Enter the number of sticks you would like to remove(1-3): "))
    #Error check that sticks_removed is valid
            while not 1 <= sticks_removed <= 3:
                sticks_removed = int(input("Invalid input. Please enter a number from 1-3: "))
    #Calculate Sticks that are left
            total_sticks -= sticks_removed
            loser = "Player 1"
            turn = 2

#Player 2's turn
        elif turn == 2:
            sticks_removed = int(input("Player 2, Please Enter the number of sticks you would like to remove(1-3): "))
    # Error check that sticks_removed is valid
            while not 1 <= sticks_removed <= 3:
                sticks_removed = int(input("Invalid input. Please enter a number from 1-3: "))
    # Calculate Sticks that are left
            total_sticks -= sticks_removed
            loser = "Player 2"
            turn = 3

#Computer's turn
        elif turn == 3:
    #Generate Computers sticks removed
            sticks_removed =  random.randint(1, 3)
            print("Computer removed", sticks_removed)
    #Calculate total_sticks
            total_sticks -= sticks_removed
            loser = "Computer"
            turn = 1

#Output Loser
    print("The loser of this round is", loser)
#Update Loss count
    if loser == "Player 1":
        player_1_loss += 1
    elif loser == "Player 2":
        player_2_loss += 1
    elif loser == "Computer":
        computer_loss += 1

#Check if user would like to play again
    print("Would you like to play another round?")
    play_choice = str(input("Yes or No: "))
    play_choice = play_choice.lower()
    while play_choice != "yes" and play_choice != "no":
        play_choice = str(input("Invalid Input. Yes or No: "))

    if play_choice == "yes":
        # Prompt user to enter the number of sticks they want to play with
        total_sticks = int(input("How many sticks would you like to play with? (10-100: "))
        while not 10 <= total_sticks <= 100:
            total_sticks = int(input("Invalid Input. How many sticks would you like to play with? (10-100): "))

    #Display Losses
    print(" \nPlayer 1 has lost", player_1_loss, "times.")
    print("Player 2 has lost", player_2_loss, "times.")
    print("The Computer has lost", computer_loss, "times.\n")

#Display Ending Message
print("*"*70)
print("Thanks for playing Sticks!")
print("-"*70)











