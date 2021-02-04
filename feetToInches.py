def feetToInches():
	feet = int(input("Feet: "))
	return feet * 12, feet


def main():

	inches, feet = feetToInches()
	print("%.1f feet is %.1f inches." % (feet, inches))

main()

