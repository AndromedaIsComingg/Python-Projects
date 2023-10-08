#!/usr/bin/python3


c = 0

while c < 5:
	c +=1
	password  = input ("enter password: ")
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
	