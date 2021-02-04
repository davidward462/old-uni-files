#guessing game

import random

def getInput():
	guess = input("Enter guess: ")
	return guess

def main():
	print()
	
	num = random.randint(0,9)
	#print(num)
	
	guess = getInput()
	
	while guess != "exit":
	
		if int(guess) == num:
			print("You are correct, sir!")
			quit()
		elif int(guess) < num:
			print("Higher")
			guess = getInput()
		elif int(guess) > num:
			print("Lower")
			guess = getInput()
			
		
		
		
		


main()