#math quiz
import random

def generateValue():
	value = random.randint(1, 1000)
	return value

def getInput():
	userInput = int(input("Your answer: "))

def main():
	value1 = generateValue()
	value2 = generateValue()
	
	print(value1, "+", value2)	
	answer = value1 + value2
	
	userAnswer = getInput()
	
	if userAnswer == answer:
		print("Correct")
	else:
		print("Incorrect. The answer is %d" % answer)
		
	
	
	
	

main()