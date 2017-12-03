#Write a function which returns a copy of the list

def getlist():
	n = input('Enter the number of elements in the list')
	l = []
	for i in range(1, n+1):
		a = input('Enter a number')
		l.append(a)
	return l

def copy_of_list(l1):
	l3 = []
	for each_ele in l1:
		l3.append(each_ele)
	l3.append(l1)
	return l3


l1 = getlist()
# l2 = getlist()
l3 = copy_of_list(l1)
print l3