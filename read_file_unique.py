# filename = input('Enter the name of the file you would like to open')
filename = "file_to_read.txt"
file_handler = open(filename, "r")


def unique_words():
	uniqueSet = set()
	for line in file_handler:# line = Hi this is Sayali.
		tempWordsList = line.split(' ') # ["Hi", "this", is, Sayali.\n]
		for word in tempWordsList:
			uniqueSet.add(word.strip(".\n"))

	print uniqueSet



unique_words()