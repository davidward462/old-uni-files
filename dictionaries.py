#dictionaries 

def main():

	phoneNums = {"Paul":6046826930, "Dave":7786460013, "Mike":8873640284}

	
	run = True
	while run:
		searchName = input("Enter name: ")
		name = phoneNums[searchName]
		print(" ", name)
		yesNo = input("Find another? ")
		if yesNo != 'y':
			run = False

main()
