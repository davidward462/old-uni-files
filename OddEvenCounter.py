#generate numbers, check if even or odd
import random

def generateNum(ValueRange):
	num = random.randint(1, ValueRange)
	return num


def main():
	NumOfPrint = int(input("How many numbers to print? "))
	ValueRange = int(input("Print numbers in range 1 to: "))
	even = 0
	odd = 0
	for number in range(0, NumOfPrint):
		num = generateNum(ValueRange)
		print(num)
		if num % 2 == 0:
			even += 1
		else:
			odd += 1
	print("\nEven: %d" % even)
	print("Odd : %d" % odd)
		

main()