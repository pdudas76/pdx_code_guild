'''
Lab 7: Password Generator

Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.

Advanced Version 1

Allow the user to choose how many characters the password will be.

Advanced Version 2

Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().
'''

import random
import string

password = ""
choices = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
length = input("How long would you like your password to be? 1-10\n")

if length.isdigit():
    length = int(length)
else:
    print("Please enter a valid number.\n")
    length = input("How long would you like your password to be? 1-10\n")

#print(choices)
for x in range(length):
    password += random.choice(choices)

print(password)
