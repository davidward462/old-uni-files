#file head display

def getFileName():
	fileName = input("Enter file name: ")
	return "\\" + fileName


def main():
	
	name = getFileName()
	
	fileIn = open(r"D:\nkfyn\Programming\Python\readWriteFiles" + name, "r")
	print()
	
	for line in range(0, 5):
		lineData = fileIn.readline()
		print(lineData)
	
	
	fileIn.close()


main()

