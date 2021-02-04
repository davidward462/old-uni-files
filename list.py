def main():

	a = [1, 6, 8, 3]

	print(a[2])
	
	x = 99
	
	a[0] = x
	
	print(a)
	
	listIndex = a.index(8)
	
	print(listIndex)
	
	a.append(4)
	
	print(a)
	
	
	
	b = []
	
	for i in range(0, 5):
		b.append(i+1)
	print(b)

	print(len(b))

	
main()