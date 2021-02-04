#number stream
import random
import time
	
def main():
	run = 1000
	currentPos = 100
	lastPos = currentPos
	loop = 0
	while loop <= run:
		for space in range(2, currentPos):
			print(" ", end='')
		print("0")
		currentPos = currentPos + random.randint(-1, 1)
		time.sleep(0.03)
		loop += 1
	
	
	
main()