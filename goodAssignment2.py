print("G P A   C A L C U L C A T O R")
# Your code goes here
#David Ward V00920409
    
#Formatting
print("  Determines a student's letter grades and term GPA")
print()
print()
    
continueInput = True 
while continueInput:
	print("Course input: ")
	#units = float(input("  Units: "))
	grade = float(input("  Grade (in percent)"))
	if grade < 50:
		print("  Letter grade =  F")
	elif (grade >= 50) and (grade <= 59):
		print("  Letter grade =  D")
	elif (grade >= 60) and (grade <= 64):
		print("  Letter grade =  C")
	elif (grade >= 65) and (grade <= 69):
		print("  Letter grade =  C+")
	elif (grade >= 70) and (grade <= 72):
		print("  Letter grade =  B-")
	elif (grade >= 73) and (grade <= 76):
		print("  Letter grade =  B")
	elif (grade >= 77 ) and (grade <= 79):
		print("  Letter grade =  B+")
	elif (grade >= 80) and (grade <= 84):
		print("  Letter grade =  A-")
	elif (grade >= 85) and (grade <= 89):
		print("  Letter grade =  A")
	elif (grade >= 90):
		print("  Letter grade =  A+")
	
		print()
	userInput = input("Another Course? (y/n)")
	if userInput != 'y':
		continueInput = False
	print()