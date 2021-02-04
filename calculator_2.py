def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2."""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2."""
    return num1 * num2


def div(num1, num2):
    #Returns num1 divided by num2.
	try:
		return num1 / num2
	except ZeroDivisionError:
		print("Handled div by zero. Returning zero.")
		return 0

		
def runOperation(num1, num2, operation):
		#Determines operation to run based on user input
		if (operation == "+"):
			print("Adding...")
			print(add(num1, num2))
		elif (operation == "-"):
			print("Subtracting...") 
			print(sub(num1, num2))
		elif (operation == "*"):
			print("Multiplying...")
			print(mul(num1, num2))
		elif (operation == "/"):
			print("Dividing...")
			print(div(num1, num2))
		else:
			print("Does not compute.")
			
	
def main():
	user_continue = True
	while user_continue:
		validInput = False
		while not validInput:
			# Get user input
			try:
				num1 = int(input("What is number 1? "))
				operation = input("What do you want to do: (+,-,*,/) ")
				num2 = int(input("What is number 2? "))
				validInput = True
			except ValueError: 
				print("Invalid input. Try again.")
				return
			except: 
				print("Unknown error")
				return
			runOperation(num1, num2, operation)
			#ask user to continue
			user_yn = input("Do you want to continue? (y/n): ")
			if(user_yn == "n"):
				user_continue = False
				print("Shutting down...")
				break
			else:
				continue	


main()