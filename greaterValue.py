#greater value
def getValues():
	value1 = float(input("Enter a value: "))
	value2 = float(input("Enter another value: "))
	return value1, value2

def max(value1, value2):
	if value1 > value2:
		return value1
	elif value2 > value1:
		return value2
	else:
		return "They are equal."



def main():
	value1, value2 = getValues()
	greatestValue = max(value1, value2)
	
	print(greatestValue)


main()