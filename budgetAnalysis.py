def main():
	budget = float(input("Budget: "))
	loop = True
	while loop:
		value = float(input("Enter expence: "))
		budget -= value
		yesNo = input("Enter another? (y/n) ")
		if yesNo != "y":
			if budget > 0:
				print("You are $%.2f over budget." % budget)
			elif budget < 0:
				budget *= -1
				print("You are $%.2f under budget." % budget)
			else:
				print("You broke even.")
			loop = False


main()