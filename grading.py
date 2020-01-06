
'''
Lab instructions:

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''

# Importing the Random module
import random

# Tried out a few different ways to determine if letter score for scores 70-100
# I hope I will pass your grading because not all are using the same method

score = input("Please enter your score from 0 to 100. ")
if score.isdigit():
    score = int(score)
    onesdigit = score % 10
    # defining the plus or minus at the end of the letter grade
    if onesdigit > 4:
        plus_minus = "+"
    else:
        plus_minus = "-"
    print(f"\nThe numeric score entered is {score}.\n")

    if score >= 90:
        print(f"Your letter grade is A{plus_minus}.\n")
    elif score >= 80 and score <=89:
        print(f"Your letter grade is B{plus_minus}.\n")
    elif score in range(70,79):
        print(f"Your letter grade is C{plus_minus}.\n")
    elif score >= 60:
        print(f"Your letter grade is D{plus_minus}.\n")
    else:
        print(f"Sorry, your letter grade is F{plus_minus}.\n")
else:
    score = input("\nDoh! Please enter a valid digit between 0 to 100. ")
    if score.isdigit():
        score = int(score)
        # defining the plus or minus at the end of the letter grade
        onesdigit = score % 10
        if onesdigit > 4:
            plus_minus = "+"
        else:
            plus_minus = "-"
        print(f"\nThe numeric score entered is {score}.\n")
        if score >= 90:
            print(f"Your letter grade is A{plus_minus}.\n")
        elif score >= 80 and score <=89:
            print(f"Your letter grade is B{plus_minus}.\n")
        elif score in range(70,79):
            print(f"Your letter grade is C{plus_minus}.\n")
        elif score >= 60:
            print(f"Your letter grade is D{plus_minus}.\n")
        else:
            print(f"Sorry, your letter grade is F{plus_minus}.\n")
    else:
        print("\nToo many tries.")
        score = random.randint(1,100)
        # defining the plus or minus at the end of the letter grade
        onesdigit = score % 10
        if onesdigit > 4:
            plus_minus = "+"
        else:
            plus_minus = "-"
        if score >= 90:
            print(f"Your random letter grade is A{plus_minus}.\n")
        elif score >= 80 and score <=89:
            print(f"Your random letter grade is B{plus_minus}.\n")
        elif score in range(70,79):
            print(f"Your random letter grade is C{plus_minus}.\n")
        elif score >= 60:
            print(f"Your random letter grade is D{plus_minus}.\n")
        else:
            print(f"Sorry, random your letter grade is F{plus_minus}.\n")

# Display and compare rival score
rival_score = random.randint(1,100)
rival_onesdigit = rival_score % 10
if onesdigit > 4:
    plus_minus = "+"
else:
    plus_minus = "-"
if score >= 90:
    print(f"Your rivals letter grade is A{plus_minus}.\n")
elif score >= 80 and score <=89:
    print(f"Your rivals letter grade is B{plus_minus}.\n")
elif score in range(70,79):
    print(f"Your rivals letter grade is C{plus_minus}.\n")
elif score >= 60:
    print(f"Your rivals letter grade is D{plus_minus}.\n")
else:
    print(f"Sorry, rivals your letter grade is F{plus_minus}.\n")
