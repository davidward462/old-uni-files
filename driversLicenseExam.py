#Driver's license exam

def main():

	answers = ['A', 'A', 'B', 'B', 'C', 'C']
	student = []

	print(answers)
	
	fileIn = open(r"D:\nkfyn\Programming\Python\readWriteFiles\StudentAnswersFail.txt", "r")
	
	#make data into a list
	for line in fileIn:
		student.append(line.rstrip("\n")) 
		
	print(student)
	
	correct = 0
	for i in range(len(answers)):
		if student[i] == answers[i]:
			correct += 1
			
	print("You got %d questions right." % correct)
	if correct > 3:
		print("You passed!")
	else:
		print("You failed.")
	
	fileIn.close()
			

main()