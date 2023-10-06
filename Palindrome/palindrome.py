#Palindrome is a word a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam nun. This program tells if a word is a palindrome

print ("Palindrome is a word a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam nun. \nThis program tells if a word is a palindrome")

word = input('please enter a word: ')

palin = word[::-1]

if word == palin:
	print (f'{word} is a palindrome')
else:
	print (f'{word} is not a palindrome')