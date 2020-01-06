# Commenting the hash symbol in front will make python ignore the following text and treat it as a comment. The grey colour is due to the editor helping by changing it to look different for visibility

'''
Multi line Commenting
Text between the three apostropies on top and bottom will make all the lines
between commented. Thought the comments will show in green instead of grey.
Baa, baa, black sheep,
Have you any wool?
Yes, sir, yes, sir,
Three bags full;

One for my master,
One for the dame,
One for the little kid
who lives down the lane.
'''

# user greeting
print("\nHello, welcome to mad libs!\n")

# Variable =
animal = input("Name an animal: ")
noun_plural = input("Name a plural noun: ")
number = input("Type a number: ")
relative0 = input("List a relative: ")
relative1 = input("Lisa another relative: ")
place = input("Name a place: ")
adjectives = input("Type three adjectives separated by commas: ")
adjectives_separate = adjectives.split(","")


# "\n" to create a new line
print("\nThanks, here is your mad lib!\n")

# fstring: prints variables inside strings
# f instructs to just print the data in the Variable
print (f"Bah, Bah, Black {animal},\nHave you any {noun_plural}?\nYes sir, yes sir,\n{number} bags full.\nOne for my {relative0}\nOne for my {relative1}\nOne for the little kid\nwho lives down the {place}.\n")

print ("Random list of items: " + str(adjectives_separate))
