#list overlap

def checkOverlap(a, b, c):
	for i in range(len(a)):
		if a[i] == b[i]:
			c.append(a[i])
	return c

def main():

	a = [1, 3, 4, 6, 0]
	b = [1, 2, 8, 4, 12]
	c = []
	
	if len(a) < len(b):
		c = checkOverlap(a, b, c)
	else: 
		c = checkOverlap(b, a, c)

	print(c)

main()