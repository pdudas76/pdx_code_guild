# filename: madlibs.py

# this is a comment
# the computer will ignore these lines
# comments are for humans/team mates

# how to make a multiline comment: use three single quotes
'''
Mary had a little lamb
His fleece was white as snow, yeah
And everywhere the child went
That little lamb was sure to go now
'''

# user greeting
print("Hello, welcome to mad libs!\n")

# to create a variable, use:
# variable_name = data
# input is a function that prompts a user for an input. it will save the input to the variable
animal = input("Name an animal: ")
something_white = input("Name an item that is white: ")
user_name = input("What's your name?")

# "\n" to create a new line
print("\n")

print("Thanks, here is your mad lib!\n")

# fstring: prints variables inside strings
print(f"{user_name} had a little {animal}\nHis fleece was white as {something_white}, yeah\nAnd everywhere the child went\nThat little {animal} was sure to go now")

# a string is anything, ANYTHING inside "quotation marks". a string is a type of data
