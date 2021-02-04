#generate lottery number

import random

def main():

	number = []

	for i in range(0, 7):
		value = random.randint(0,9)
		number.append(value)
		print(number[i], end='')
	print()
	

main()