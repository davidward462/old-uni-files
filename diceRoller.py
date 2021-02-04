import random

def getSides():
	sides = input(print("How many sides? ")
	return sides

def rollDice(diceType):
	rollValue = random.randrange(1, diceType)
	return rollValue

def main(): 
	diceType = getSides()
	output = rollDice(diceType)
	print(output)
	
main()	
	
	
	
#doesn't work	