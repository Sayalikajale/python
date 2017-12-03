def intersect(l1, l2):
	l3 = []
	for each_ele in l1:
		if each_ele not in l3:
			count = 0
			a = l1.count(each_ele)
			print a, 'a is'
			b = l2.count(each_ele)
			print b, 'b is'
			if a < b:
				count = a
			else:
				count = b
			print count, 'count'
			while count > 0:
				l3.append(each_ele)
				count -= 1

	print l3, 'l3 is'

def getlist():
	l = []
	num_of_ele = input('Enter the number of elements in the list: ')

	for i in range(1, num_of_ele+1):
		a = input('Enter a number')
		l.append(a)
		# print l, 'l is'
	return l

l1 = getlist()
l2 = getlist()
intersect(l1,l2)