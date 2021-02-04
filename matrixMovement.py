#matrixMovement

def getInput():
	dir = input("Enter direction: ")
	return dir

def printMap(map):
	print()
	for row in range(len(map)):
		for column in range(len(map)):
			print(map[row][column], end=' ')
		print()
	print()
	

def main():

	run = True
	
	map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	
	while run:
		printMap(map)
		dir = getInput()
		
		if dir == "0":
			run = False
		
		
		
		

main()