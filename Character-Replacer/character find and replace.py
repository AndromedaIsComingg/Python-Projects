#!/usr/bin/python3
# Program Description - This program finds and replace characters 

# Welcome message
print ("This program finds and replace characters")

# user inputs
text = input ("please enter a text:")
letter = input ("please enter the letter(s) you want to replace ")
replacement = input ("please enter a replacement ") 
text = text.replace(letter, replacement) # Replacement line
print (text)