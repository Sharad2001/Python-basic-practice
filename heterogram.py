def isSet(word):

	# separate out list of alphabets using list comprehension
	# ord function returns ascii value of character
	alphabets = [ ch for ch in word if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]

	# convert list of alphabets into set and compare lengths
	if len(set(alphabets))==len(alphabets):
		print ('True')
	else:
		print ('False')

if __name__ == "__main__":
	word = input("Enter the word: ")
	isSet(word)
