

def askUser(bound):
	highOrLow = input(print("higher or lower than %d ?" % bound))

def algorithm(highOrLow, bound): 
	if(highOrLow == "h"): 
		bound += (bound / 2)
	else: 
		bound -= (bound / 2)
	return bound	

def main():
	correct = False
	bound = 50
	while not correct:
		highOrLow = askUser(bound)
		algorithm(highOrLow, bound)
	correct = True	
	print("I guessed it!")
	