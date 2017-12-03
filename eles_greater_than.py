n = input('Enter the number of elements in the list')

l = []

for i in range(1, n+1):
	a = input('Enter the number')
	l.append(a)

ele_grt_than = input('Enter the element whose greater eles you want')

ret = []

for each in l:
	if each > ele_grt_than:
		ret.append(each)

print ret
