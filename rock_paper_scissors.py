# Filename rock_paper_scissors.py

'''
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors
'''

# Import random module
import random

# Define computer outcomes
choices = ["rock","paper","scissors"]

play_again = "yes"

while play_again == "yes" or play_again == "y":

    computer_choice = random.choice(choices)

    user_choice = input("\nChoose your weapon\nEnter rock, paper, or scissors\n\n:")

    print("\nYou: " + user_choice + " vs " + "Computer: " + computer_choice + "\n")

    if computer_choice == user_choice:
        print("TIE!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win, " + user_choice + " beats " + computer_choice + ".\n")
        else:
            print("You lose," + computer_choice + " beats " + user_choice + ".\n")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win, " + user_choice + " beats " + computer_choice + ".\n")
        else:
            print("You lose, " + computer_choice + " beats " + user_choice + ".\n")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win, " + user_choice + " beats " + computer_choice + ".\n")
        else:
            print("You lose, " + computer_choice + " beats " + user_choice + ".\n")
    else:
        print("ERROR -- Please choose rock, paper or scissors in lower case only.")

    play_again = input("Would you like to play again? ")

print("Goodbye!")
