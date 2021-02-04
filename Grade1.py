# Author: L. Jackson  January 2018
# Purpose: Calculated the weighted grade for a student in a course
# Filename: Grade.py
# Inputs: Assignments, Labs and Exam grades 

# The class Grade contains methods for calculating the
# weighted average of a number of assessments, the letter
# grade given a percentage grade and an overall course 
# percentage grade.

def main():
	
	# Contstants: eases changing numbers of assessments, weightings, maximums
	NUM_ASSGTS = 7
	NUM_LABS = 10
	NUM_MTs = 2
	NUM_Final = 1
	
	WEIGHT_ASSGTS = 3.0
	WEIGHT_LABS = 0.5
	WEIGHT_MTs = 16.0
	WEIGHT_Final = 42.0
	
	MAX_ASSGTS = 10.0
	MAX_LABS = 1.0
	MAX_exams = 100.0
	
	
	# Intro
	print("\n\n\n C O U R S E   G R A D E   C A L C U L A T O R\n\n\n")
	print("    Purpose: Calculates the weighted grade for a student in a course")
	print("       Inputs: Assignment, Lab and Exam grades\n\n")

	# Define Passing Grade
	passingGrade = float(input("Passing Grade for Final ==>  "))
	
	#Cummulative sum for grade
	grade = 0.0
	
	# Assignments:
	assignment_Sum = 0.0
	print("\n\nInput Assignments (maximum", MAX_ASSGTS, "):")
	for count in range(0, NUM_ASSGTS):
		# Start with an Assignment grade that is too high
		# repeat until a valid grade is enterd
		assignment = MAX_ASSGTS + 1
		
		# test for correct grade input
		while assignment > MAX_ASSGTS or assignment < 0: 
			prompt = "  #" + str(count+1) + "==>"
			assignment = float(input(prompt))
			if assignment > MAX_ASSGTS or assignment < 0:
				print("  Incorrect input, try again:")
		
		# once good value input, add to sum of Assignments
		assignment_Sum += assignment / MAX_ASSGTS
		
	# add Assignments to total course grade with weight
	grade +=  assignment_Sum * WEIGHT_ASSGTS
		
	# Labs:
	lab_Sum = 0.0
	print("\n\nInput Labs (maximum", MAX_LABS, "):")
	for count in range(0, NUM_LABS):
		# Start with a Lab grade that is too high
		# repeat until a valid grade is enterd
		lab = MAX_LABS + 1
		
		# test for correct grade input
		while lab > MAX_LABS or lab < 0: 
			prompt = "  #" + str(count+1) + "==>"
			lab = float(input(prompt))
			if lab > MAX_LABS or lab < 0:
				print("  Incorrect input, try again:")
		
		# once good value input, add to sum of Labs
		lab_Sum += lab / MAX_LABS
		
	# add Labs to total course grade with weight
	grade +=  lab_Sum * WEIGHT_LABS		
		
	# Midterms:
	MT_Sum = 0.0
	print("\n\nInput Midterms (maximum", MAX_exams, "):")
	for count in range(0, NUM_MTs):
		# Start with an Exam grade that is too high
		# repeat until a valid grade is entered
		midterm = MAX_exams + 1
		
		# test for correct grade input
		while midterm > MAX_exams or midterm < 0: 
			prompt = "  #" + str(count+1) + "==>"
			midterm = float(input(prompt))
			if midterm > MAX_exams or midterm < 0:
				print("  Incorrect input, try again:")
		
		# once good value input, add to sum of Labs
		MT_Sum += midterm / MAX_exams
		
	# add Midterms to total course grade with weight
	grade +=  MT_Sum * WEIGHT_MTs		

	# Final:
	Final_Sum = 0.0
	print("\n\nInput Final (maximum", MAX_exams, "):")
	for count in range(0, NUM_Final):
		# Start with an Exam grade that is too high
		# repeat until a valid grade is entered
		final = MAX_exams + 1
		
		# test for correct grade input
		while final > MAX_exams or final < 0: 
			prompt = "  #" + str(count+1) + "==>"
			final = float(input(prompt))
			if final > MAX_exams or final < 0:
				print("  Incorrect input, try again:")
		
		# once good value input, add to sum of Labs
		Final_Sum += final / MAX_exams
		
	# Determine if Failed final exam and add Final to course grade
	if Final_Sum < (passingGrade / MAX_exams) :
		if ((grade + final_Sum* WEIGHT_Final) > 49.5):
			grade = 49
		else:
			grade += Final_Sum * WEIGHT_Final
	else:
		grade += Final_Sum * WEIGHT_Final

	# Determine Letter Grade
	if grade < 49.5:
		letter = "F"
	elif grade < 59.5:
		letter = "D"
	elif grade < 64.5:
		letter = "C"
	elif grade < 69.5:
		letter = "C+"
	elif grade < 72.5:
		letter = "B-"
	elif grade < 76.5:
		letter = "B"
	elif grade < 79.5:
		letter = "B+"
	elif grade < 84.5:
		letter = "A-"
	elif grade < 89.5:
		letter = "A"
	else:
		letter = "A+"

	# Output percent and letter grade
	print("\n\n\n")
	print(" Grade: %2.2f"%grade, letter)

	
	
# Program entry point
if __name__ == '__main__':
	main()