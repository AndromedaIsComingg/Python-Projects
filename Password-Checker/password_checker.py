#!/usr/bin/python3
# This program propmts a user to input a password, giving several condition as prompt 
# & also counting down upon every attemp.

c = 0 # This sets the beginning of the counter


# Creating a while loop
while c < 5:
	c +=1
	password  = input ("enter password: ")
	
	# Creating conditional statements
	if len(password ) < 6:
		print ("password  must be up to 6 characters")
		print ("you have", (5 - c), "attempts remaining")
		continue 
	if any(char.isalpha() for char in password ):
		pass
	else:
		print ("password  must contain an alphabet")
		print ("you have", (5 - c), "attempts remaining")
		continue 
	if any(char.isnumeric() for char in password ):
		pass
	else:
		print("password  must contain a number ")
		print ("you have", (5 - c), "attempts remaining")
		continue 
	if any(not char.isalnum()for char in password ):
		pass
	else:
		print ("password  must contain a special character")
		print ("you have", (5 - c), "attempts remaining")
		continue 
	if any(char.isupper() for char in password):
		pass
	else:
		print ("password must contain at least one capital letter")
		print ("you have", (5 - c), "attempts remaining")
		continue
	print ("password accepted")
	break 
if c == 5:
	print ("you have exhausted your attempts")
	