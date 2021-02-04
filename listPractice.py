def simpleLists():
	friends = ["Bob", "Joe", "Steve"]
	print(friends)

	friends[2] = "Dale"
	print(friends)

	numbers = [1, 2, 3]

	bigList = friends + numbers
	print(bigList)
	
def appendList():
	stuff = ["bike", "car", "shirt"]
	stuff.append("sword")
	print(stuff)
	
def listSlice():
	longList = [1, 2, 3, 4, 5]
	shortList = longList[2:]
	print(shortList)
	print(longList)

def sortList():
	integers = [2, 5, 7, 9, 1]
	print(integers)
	sort(integers)
	print(integers)

def divide():
	value = 8
	answer = value // 2
	print(answer)

	
	
def main():
	#simpleLists()
	#listSlice()
	#appendList()
	#sortList()
	divide()
	
main()