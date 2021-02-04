def main():

	bugTotal = 0
	day = 1

	while day <= 5:
		collected = int(input("Bugs collected on day "+ str(day) + ":"))
		bugTotal += collected
		day += 1
	print("Total bugs collected:", bugTotal)

main()































