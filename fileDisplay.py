#File display

def main():

	fileIn = open(r"D:\nkfyn\Programming\Python\readWriteFiles\numbers.txt", "r")
	
	data = fileIn.read()
	print(data)
	
	fileIn.close()

main()