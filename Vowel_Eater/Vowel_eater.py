#!/usr/bin/python3

# Importing Regular expression
import re

# This line prints a welcome display
print ("Welcome, this app eats vowels _00_")

# Creating a loop flow
while True:
# This takes the user input
	w = input ("please enter a word:")

# This converts uppercases to lowercase
	w = w.casefold()
	
# This regular expression substitutes a,e,i,o,u with an empty string
	x = re.sub("[aeiou]", "", w)

# This ensures that every character in the input is an alphabet
	if not all (char.isalpha() for char in w):
		print (w, "is not a valid word")
		continue
	else:
		print (x)
		break 
