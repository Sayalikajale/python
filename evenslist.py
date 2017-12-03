n = input('Enter the number of elements in the list')
l = []

for i in range(1, n+1):
	a = input('Enter the number')
	l.append(a)

print l

ret = []
for each in l:
	if each == 0:
		ret.append(each)
	elif each%2 == 0:
		ret.append(each)

print ret

