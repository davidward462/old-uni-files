#cpu guesses a number
import random


#generate list of even numbers
#List has length "limit"
def genList(list, value, limit):
	while len(list) < limit:
		if value % 2 == 0:
			list.append(value)
			value += 1
		else:
			value += 1
	return list
		

def binSearch(list, searchValue):
	min = 0
	max = len(list) - 1 #max is greatest index in list
	
	while min < max:
		guess = (min + max) // 2 #guess is average of min and max
		if list[guess] == searchValue:
			print("Found your value %d at index %d" % (list[guess], guess))
			quit()
		elif list[guess] < searchValue:
			min = guess + 1
		elif list[guess] > searchValue:
			max = guess - 1

	
def main():

	list = []
	value = 1
	limit = 25
	searchValue = 2
	
	guessList = genList(list, value, limit)
	print(guessList)
	
	binSearch(guessList, searchValue)
	

main()