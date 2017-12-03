def union1(l1, l2):
	l3 = []
	for element in l1:
		if element not in l3:
			print element, 'element'
			count = 0
			a = l1.count(element)
			print a, 'value of a'
			b = l2.count(element)
			print b, 'value of b'
			if a >= b:
				count1 = a
			else:
				count1 = b
			print count1, 'count'
			while count1 > 0:
				l3.append(element)
				print l3, 'l3 is'
				count1 -= 1
	for element in l2:
		if element not in l3:
			print element, 'element'
			count = 0
			a = l1.count(element)
			print a, 'value of a'
			b = l2.count(element)
			print b, 'value of b'
			if a >= b:
				count1 = a
			else:
				count1 = b
			print count1, 'count'
			while count1 > 0:
				l3.append(element)
				print l3, 'l3 is'
				count1 -= 1
	print l3


def getlist():
	l = []
	n = input('Enter the number of elements int he list')
	for i in range(1, n+1):
		a = input('Enter the number')
		l.append(a)
	return l	


l1 = getlist()
l2 = getlist()
union1(l1, l2)

