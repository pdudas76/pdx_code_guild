import random
adjectives = input("Type three adjectives separated by commas: ")
adjectives_separate = adjectives.split(",")
random_adjective = random.choice(adjectives_separate)
print ("Random list of items: " + str(adjectives_separate))
