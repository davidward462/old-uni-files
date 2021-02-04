#matrix grid

def getInput():
	direction = input("Enter direction: ")
	return direction
	
def printGrid(field):

	for row in range(len(field)):
		print("\t", end='')
		for column in range(len(field)):
			print(field[row][column], end=' ')
		print()
		
def move(direction):
	if direction == 'w':
		playerX = 1
	elif direction == 's':
		playerY = 1
	

def main():
	print()
	
	field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	field[2][1] = "x" # player position
	
	printGrid(field)
	
	direction = getInput()
	
	
	
		

main()