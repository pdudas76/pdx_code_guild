'''
Lab 7: Password Generator

Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.

Advanced Version 1

Allow the user to choose how many characters the password will be.

Advanced Version 2

Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().
'''
# Importing modules
import random
import string

# Defining Variables
password = ""
do_over = "yes"
# Gather number of letters, numbers and punctuation
while do_over in ["yes","y"]:

    characters = []

    letters_length = input("\nHow many upper and lowercase letters would you like? ")
    letters_escape = 0
    while letters_escape == 0:
        if letters_length.isdigit():
            letters_length = int(letters_length)
            letters_escape =+ 1
        else:
            letters_length = input("\nPlease enter a valid number. ")

    numbers_length = input("\nHow many numbers would you like? ")
    numbers_escape = 0
    while numbers_escape == 0:
        if numbers_length.isdigit():
            numbers_length = int(numbers_length)
            numbers_escape =+ 1
        else:
            numbers_length = input("\nPlease enter a valid number. ")

    punctuation_length = input("\nHow many special characters would you like? ")
    punctuation_escape = 0
    while punctuation_escape == 0:
        if punctuation_length.isdigit():
            punctuation_length = int(punctuation_length)
            punctuation_escape =+ 1
        else:
            punctuation_length = input("\nPlease enter a valid number. ")

    # Determine the random characters from the number the user chose and add them to a list
    for x in range(letters_length):
        characters.append(random.choice(string.ascii_lowercase + string.ascii_uppercase))

    for x in range(numbers_length):
        characters.append(random.choice(string.digits))

    for x in range(punctuation_length):
        characters.append(random.choice(string.punctuation))

    # Shuffle the list of characters and join them together for output
    random.shuffle(characters)
    characters = "".join(characters)

    # Output password to user
    print(f"\nYour new password is: {characters}\n")
    do_over = input("Would you like to generate another password? ")
