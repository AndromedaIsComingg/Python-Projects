#!/usr/bin/python3


#name = "Jonathan"
#for char in name:
#	if char == "a":
#		continue
#	print (char)
#name = name.replace("a", "o")
#print (name)

print(f"This program counts the number of odd and even numbers inputted")
odd= []
even= []

while True:
	lenEven = len(even)
	lenOdd = len(odd)
	num = input (f"enter a number  or type 's' to stop:")
	if num == "s" or num == "S":
		print (f"the number of odd numbers is {lenOdd}")
		print (f"the number of even numbers is {lenEven}")
		break
	if all (char.isnumeric() for char in num):
		pass
	else:
		print (f"only numbers are allowed")
		continue 
	num = int(num)
	if num % 2 == 0:
		even.append(num)
	else:
		odd.append(num)
		continue 
