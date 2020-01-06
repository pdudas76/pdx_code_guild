# filename magic_8_ball.py
# this application will simulate the Magic 8 magic_8_ball

# importing the random module
import random

# defining the list of items
answers = ["Yes","No","Maybe","I don't think so.","Try again.","Wouldn't you like to know.","I'm scared to say."]

# welcoming the user to the Magic 8 Ball program
print("_-" * 30)
print("\nWelcome, Have fun.")

# prompt for user input
user_question = input("\nWhat would you like to ask Magic 8 Ball?\nQuestion: ")
print(f"\nYou asked Magic 8 Ball this question: {user_question}")

# randomly select item from answers
random_answer = random.choice(answers)
print(f"\nMagic 8 Ball's answer is: {random_answer}\n")
