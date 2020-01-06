# Import modules
import random

# Define function to gather input from user
def user_guess():
    user_guess = input("Guess a number from 1 to 10: ")
    is_int_result = is_int(user_guess)
    return is_int_result

# Define function to check if the user entry is a digit and within the range allowed
def is_int(user_guess):
    if user_guess.isdigit() and int(user_guess) in range(1,11):
        user_check = int(user_guess)
        return user_check
    else:
        return False

# Define computer random answer
def computer_guess():
    computer_guess = random.randint(1,10)
    return computer_guess

# Define compare computer random answer to user entered value
def guess_check():
    if user_guess() == 3:
        print("You guessed correctly.")
    elif user_guess() == False:
        print("hey, that's not a number")
    else:
        print("You guessed incorrectly.")

guess_check()
