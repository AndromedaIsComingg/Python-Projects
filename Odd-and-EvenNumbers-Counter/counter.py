#!/usr/bin/python3

# Welcome line
print(f"This program counts the number of odd and even numbers inputted")

#Creating two lists to append odd or even inputs
odd= []
even= []

# Creating a loop flow
while True:
	lenEven = len(even)
	lenOdd = len(odd)

# This line takes in the user input
	num = input (f"enter a number  or type 's' to stop:")

# Creating conditional statement to terminate the program
	if num == "s" or num == "S":
		print (f"the number of odd numbers is {lenOdd}")
		print (f"the number of even numbers is {lenEven}")
		break
	
# Creating conditions to ensure that input are numbers only
	if all (char.isnumeric() for char in num):
		pass
	else:
		print (f"only numbers are allowed")
		continue 

# Making input integer for arithematic and appending to the earlier created lists
	num = int(num)
	if num % 2 == 0:
		even.append(num)
	else:
		odd.append(num)
		continue 
