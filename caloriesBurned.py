def main():
	CAL_PER_MIN = 4.2
	for minutes in range(10, 31, 5):
		calories = minutes * CAL_PER_MIN
		print(calories)


main()