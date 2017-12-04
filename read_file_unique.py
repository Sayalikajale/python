# filename = input('Enter the name of the file you would like to open')
filename = "file_to_read.txt"
file_handler = open(filename, "r")

def sayaliSolution():
	a = []
	fin_list = []

	for each in file_handler:
		a.append(each.strip(".\n"))
	print a, 'a is printed'

	for each in a:
		print each, each
		for every in each:
			fin_list.append(every.split(' '))

	print fin_list


def bhushanSsolution():
	uniqueSet = set()
	for line in file_handler:# line = Hi this is Sayali.
		tempWordsList = line.split(' ') # ["Hi", "this", is, Sayali.\n]
		for word in tempWordsList:
			uniqueSet.add(word.strip(".\n"))

	print uniqueSet



bhushanSsolution()