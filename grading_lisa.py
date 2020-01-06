# filename: grading.py
'''
Goal: convert a number grade to a letter grade
    - using elif statements and comparisons (==, >= <=)

- Have the user enter a number representing the grade (0-100) .. use input()
- Convert the number grade to a letter grade

OUTCOME: print letter grade out to the user

Outcomes:
Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F

Stretch
- Use randint() from the random module to determine the user's rival's score
- Let the user know if they did better than their rival

- +/-
'''

# Modules
import random

stars = "*" * 5

# greet the user
print(f"{stars} Welcome to Your Grade Book {stars}")
# this method is called concatenating aka mushing strings together

# prompt user for a score
user_grade = input("What is your score? (0-100)")

# data/form validation
# - must be a number
# - number within range of 0-100

if user_grade.isdigit():
    # print("Hey, this is a number.")
    user_grade = float(user_grade)

    if 90 <= user_grade <= 100:
        print("A")
        # letter_grade = "A"
    elif user_grade in range(80,90):
        letter_grade = "B"
    elif user_grade in range(70,80):
        letter_grade = "C"
    elif user_grade in range(60,70):
        letter_grade = "D"
    elif user_grade in range(0,60):
        letter_grade = "F"
    else:
        print("Sorry, input not in range of 0-100")
else:
    print("Please enter a valid score between 0-100")

# calculate +/-

add_on_grade = user_grade%10

if add_on_grade > 6:
    sign = "+"
elif add_on_grade < 4:
    sign = "-"
else:
    sign = ""

# computer generated score for rival
rival_score = random.randint(0,100)

print(f"You got a score of {user_grade} which is a {letter_grade}{sign}. Your rival got {rival_score}")

# check if user score is higher or lower than rival

if user_grade > rival_score:
    print("You did better than your rival!")
elif user_grade < rival_score:
    print("Your rival did better than you!")
else:
    print("You tie!")
