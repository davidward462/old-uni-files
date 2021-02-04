def main():

	#open files
	firstFile = open(r"C:\Users\nkfyn\Desktop\TextCompareFile1.txt", "r")
	secondFile = open(r"C:\Users\nkfyn\Desktop\TextCompareFile2.txt", "r")

	#read files
	firstString = firstFile.read()
	secondString = secondFile.read()

	if firstString != secondString:
		print("They are different")



main()