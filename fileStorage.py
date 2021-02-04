#file storage

def getCommand():
	command = input("Enter command: ")
	return command
	

def writeToFile():
	print("Write")
		
		

def readFromFile():
	print("Read")
		

def deleteFile():
	print("Delete")
		

def main():

	run = True
	while run:
		cmd = getCommand()
		
		if cmd == "quit" or cmd == "exit" or cmd == "stop":
			run = False
		elif cmd == "write":
			writeToFile()
		else:
			print("Invalid command

main()