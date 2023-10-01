#!/usr/bin/python3

#f = ["a", "e", "i", "o", "u"]
#g = []
#print ("Welcome, this app eats vowels _00_")
#while True:
#	word = input ("please enter a word:")
#	word = word.casefold()
#	if all (char.isalpha() for char in word):
#		pass
#	else:
#		print ("not a valid word")
#		continue
#	for re in word:
#		if not re in f:
#			g.append(re)
#	print (g)
#	break 



import re
print ("Welcome, this app eats vowels _00_")
while True:
	w = input ("please enter a word:")
	w = w.casefold()
	x = re.sub("[aeiou]", "", w)
	if not all (char.isalpha() for char in w):
		print (w, "is not a valid word")
		continue
	else:
		print (x)
		break 
