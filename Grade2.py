# Author: L. Jackson  January 2018
# Purpose: Calculated the weighted grade for a student in a course
# Filename: Grade.java
# Inputs: Assignments, Labs and Exam grades

# This program contains functions for calculating the
# weighted average of a number of assessments, the letter
# grade given a percentage grade and an overall course 
# percentage grade.

def main():
	
	# Contstants: eases changing numbers of assessments, weightings, maximums
	NUM_ASSGTS = 7
	NUM_LABS = 10
	NUM_MTs = 2
	NUM_FINAL = 1
	
	WEIGHT_ASSGTS = 3.0
	WEIGHT_LABS = 0.5
	WEIGHT_MTs = 16.0
	WEIGHT_FINAL = 42.0
	
	MAX_ASSGTS = 10.0
	MAX_LABS = 1.0
	MAX_EXAMS = 100.0
	
	
	# Intro
	print("\n\n\n C O U R S E   G R A D E   C A L C U L A T O R\n\n\n")
	print("    Purpose: Calculates the weighted grade for a student in a course")
	print("       Inputs: Assignment, Lab and Exam grades\n\n")

	# Define Passing Grade
	passingGrade = float(input("Passing Grade for Final ==>  "))
	
	grade = 0.0

	grade += weightedAverage("Assignment ", MAX_ASSGTS, NUM_ASSGTS, WEIGHT_ASSGTS) 
	grade += weightedAverage("Lab ", 1, MAX_LABS, NUM_LABS, WEIGHT_LABS)
	grade += weightedAverage("Midterm ", MAX_EXAMS, NUM_MTs, WEIGHT_MTs)

	finalExam = weightedAverage("Final Exam " MAX_EXAMS, NUM_FINAL, WEIGHT_FINAL)

	# Failed final exam?
	if finalExam < passingGrade / 100.0 * WEIGHT_Final:
		if (grade + finalExam) > 49.5:
			grade = 49
		else:
			grade += finalExam 
	else:
		grade += finalExam

	# Output percent and letter grade
	print("\n")
	print(" Grade: %2.2f"% grade, calculateLetter(grade))


# weightedAverage - Calculates the weighted grade for a certain course activity
def weightedAverage(activity, max, number, weight):
	sum = 0.0
	print()
	
	print("Input " + activity + "(maximum " + str(max) +"):")
	for count in range(0, number):
		# Start with a grade that is too high
		# repeat until a valid grade is enterd
		one_grade = max + 1
		
		# test for correct grade input
		while one_grade > max or one_grade < 0: 
			prompt = "  #" + str(count+1) + "==>"
			one_grade = float(input(prompt))
			if one_grade > max or one_grade < 0:
				print("  Incorrect input, try again:")
		
		# once good value input, add to sum 
		sum += one_grade / max
		
	# multiply sum by weight and return
	return  sum * weight		

	
# calculateLetter - determines the letter grade - as defined in CSc 110 course outline
# INPUT: grade - the weighted final grade, in percent.
# RETURNS: letter - the course letter grade
def calculateLetter(grade):
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

	return letter

	
if  __name__ == '__main__':
	main()