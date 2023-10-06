#Palindrome is a word a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam nun. This program tells if a word is a palindrome


# welcome message
print ("Palindrome is a word a word, phrase, or sequence that reads \n the same backwards as forwards, e.g. madam, nun. \nThis program tells if a word is a palindrome")


# Taking user input
word = input('please enter a word: ')

# List slicing
palin = word[::-1]

if word == palin:
	print (f'{word} is a palindrome')
else:
	print (f'{word} is not a palindrome')