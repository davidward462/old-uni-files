#Greater than n

import random

def main():

	n = int(input("Enter an integer: "))
	list = []

	#generate list
	for i in range(0, 7):
		value = random.randint(0, 9)
		list.append(value)
	print("\nList: ", list)
	
	print()
		
	for i in range(len(list)):
		if list[i] > n:
			print(list[i])
		
			

main()