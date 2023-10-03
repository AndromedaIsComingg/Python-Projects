#!/usr/bin/python3
# This line displays the welcome messageg
print ('This app takes multiple numbers as input and tells you the highest one. _00_')

# Creates a list of all inputed numbers
x = []

# Creates a list of a sorted version of the above list after slicing
z = [0]
print ()

# Creates a loop flow
while True:
	num= input ('enter a number or press "s" to stop: ')	#Takes the user input
	if num == "s" or num == "S":							#Terminates the code
		print (f'the highest number is {z}')				#Prints the highest number
		break
	if all(char.isnumeric() for char in num):				#Ensures that all input are numeric
		pass
	else:
		print ("only numbers must be entered ")				#Wrong input warning message
		continue
	x.append(num)											#Apppends the input to the list x
	x.sort()												#Sorts the list x	
	z = x[-1]												#Slices the list x and picks the last value
