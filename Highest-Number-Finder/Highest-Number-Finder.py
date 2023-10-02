#!/usr/bin/python3

print ('This app takes multiple numbers and tells you the highest one. _00_')
x = []
z = [0]
print ()
while True:
	num= input ('enter a number or press "s" to stop: ')
	if num == "s" or num == "S":
		print (f'the highest number is {z}')
		break
	if all(char.isnumeric() for char in num):
		pass
	else:
		print ("only numbers must be entered ")
		continue
	x.append(num)
	x.sort()
	z = x[-1]
