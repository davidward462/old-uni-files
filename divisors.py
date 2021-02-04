#find divisors

def getInput():
	value = int(input("Enter a value: "))
	return value

def main():
	
	run = True
	while run:
		print()
		
		invalidInput = True
		
		while invalidInput:
			try:
				value = getInput()
				invalidInput = False
			except ValueError:
				print("Invalid input")

		divisors = []

		for i in range(1, value):
			if value % i == 0:
				divisors.append(i)
				
		print("\n ", divisors)
		
		if len(divisors) > 1:
			print("  Not prime")
		else:
			print("  Prime")
		
		print()
		
		yesNo = input("Enter another? (y/n): ")
		if yesNo != "y":
			run = False

main()