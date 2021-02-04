#move items in lists
import random

def createList():
	sourceList = [1, 2, 3, 4, 5]
	return sourceList

def moveItems(sourceList, newList, itemChoice):
	for i in range(len(itemChoice)):
		newList.append(sourceList[itemChoice[i]])
		sourceList[itemChoice[i]] = "null"
	return newList, sourceList

def main():
	sourceList = createList()
	newList = []
	print("source:", sourceList)
	
	run = True
	while run:
		choiceString = input("Input index: ")
		choiceList = sorted(choiceString.split())
		for i in range(len(choiceList)):
			choiceList[i] = int(choiceList[i])
		print(choiceList)
		
		newList, sourceList = moveItems(sourceList, newList, choiceList)
		print("New list:", newList)
		print("Updated source list:", sourceList)
		yesNo = input("Run again? ")
		if yesNo != 'y':
			run = False
		
main()
