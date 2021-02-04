#Print file with line numbers

def getFileName():
	name = input("Enter file name: ")
	return "\\" + name

def main():
	name = getFileName()
	fileIn = open(r"D:\nkfyn\Programming\Python\readWriteFiles" + name, "r")
	
	print()
	count = 0
	
	#read file
	for line in fileIn:
		count += 1 #count number of lines
		print(str(count) + ": " + line)
	
	fileIn.close()

main()