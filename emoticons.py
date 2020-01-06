# filename emoticons.py

'''

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)
'''
# Import random module
import random

# Define options for facial features
eyes = [':',";"]
noses = [">","~","-","^"]
mouths = ["|","/","o",")"]

# Generate 5 randomized emoticons
generate = "yes"
while generate == "yes" or generate == "y":
    for x in range(5):
        emoticon = x + 1
        eye = random.choice(eyes)
        nose = random.choice(noses)
        mouth = random.choice(mouths)
        print(f"Emoticon {emoticon}) {eye}{nose}{mouth}")
    generate = input("\nWould you like 5 more emoticons? ")
print("\nGoodbye!")
