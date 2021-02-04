import random

nameList = []
for i in range(0, 3):
	name = input("Enter a name: ")
	nameList.append(name)
	
value = random.randint(0, 3)

print(nameList[value])