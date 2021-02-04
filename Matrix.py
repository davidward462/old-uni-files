#CSC 110 201809 Assignment 4
#David Ward
#V00920409
#1/11/18

def getMatrix(fileIn):

	try: #if data is the constant, not matrix
		line = fileIn.readline() #read first line
		list = line.split() #make string into list
		
		#get rows and columns
		rows = int(list[0])
		columns = int(list[1])
			
		#delete row/column indicators
		del list[0]
		del list[0]
			
		#format to matrix
		matrix = []
		for i in range(rows):
			innerList = []
				
			for j in range(columns):
				innerList.append(int(list[0])) #take first element of list and append to innerList
				del list[0] #delete first element
					
			matrix.append(innerList)
		return matrix, rows, columns
	except IndexError: #return constant 
		return int(list[0])
		
	
def addMatrix(A, B):
	C = []
	for i in range(len(A)):
		innerC = []
		for j in range(len(A[i])): #loop through inner lists
			try:
				sum = A[i][j] + B[i][j] #add list values at position i, j
				innerC.append(sum)
			except IndexError: #return empty list if lists are not same size
				C = []
				return C
		C.append(innerC) #append inner to matrix C
	return C #return matrix
	
	
def subMatrix(A, B):
	C = []
	for i in range(len(A)):
		innerC = [] #create inner list
		for j in range(len(A[i])): #loop through inner lists
			try:
				diff = A[i][j] - B[i][j]
				innerC.append(diff) 
			except IndexError: #if lists are not the same length, return an empty list
				C = []
				return C
		C.append(innerC) #append inner lists to outer list 
	return C #return matrix
	
	
def scalarMultiply(matrix, scalar):
	result = []
	for i in range(len(matrix)):
		innerResult = []
		for j in range(len(matrix[i])): #loop through inner lists
			product = matrix[i][j] * scalar #scalar * matrix at i,j
			innerResult.append(product)
		result.append(innerResult)
	return result #return matrix
	
def dot(A, D):	 #if the matrix A has the same number of columns as matrix D has rows. 
	matrix = []
	for rows in range(len(A)):
		innerResult = []
		for columns in range(len(D[0])):
			product = 0
			for counter in range(len(A[0])):
				product += A[rows][counter] * D[counter][columns]
			innerResult.append(product)
		matrix.append(innerResult)
	return matrix
	
	
	#write results to file
def outputMatrix(name, matrix, fileOut):
	fileOut.write(name + "= ")
		
	try: #exception will be raised if matrix isn't a list
		if len(matrix) != 0:	
			for i in range(len(matrix)):
				for j in range(len(matrix[i])):
					fileOut.write('\t') 
					fileOut.write(str(matrix[i][j]))
				fileOut.write('\n')
		else: 
			fileOut.write("\n")
		#Write constant if input is not a list	
	except:
		fileOut.write("\t") 
		fileOut.write(str(matrix))
		fileOut.write("\n") 
			
			#calc file length
def checkFileLength(fileIn):
	numOfLines = 0
	for x in fileIn:
		numOfLines += 1
	return numOfLines

def main():
	
	#Screen output
	print("MATRIX ARITHMETIC\n")
	print("Inputting Matrices A, B and D and scalar c . . . . . .")
	print(". . . . Result Written to file: MatrixResult.txt")
	
	#open read file
	fileIn = open(r"D:\nkfyn\Documents\CSC 110 assignments\Assignment 4\MatrixIn.txt", "r") 
	
	#create output file. Change file to MatrixResult.txt
	fileOut = open(r"D:\nkfyn\Documents\CSC 110 assignments\Assignment 4\MatrixResult.txt", "w")
	
	numOfLines = checkFileLength(fileIn) #get number of lines
	fileIn.seek(0) #reset read pointer to start of file
	
	#loop as many times as there are sets of data 
	
	#data lines are multiples of 4
	LINES_PER_SET = 4
	
	for i in range(numOfLines//LINES_PER_SET):
		#read/store data
		A, rowsA, columnsA = getMatrix(fileIn)
		B, rowsB, columnsB = getMatrix(fileIn)
		c = getMatrix(fileIn)
		D, rowsD, columnsD = getMatrix(fileIn)
			
		#print data
		outputMatrix('A', A, fileOut)
		outputMatrix('B', B, fileOut)
		outputMatrix('c', c, fileOut)
		outputMatrix('D', D, fileOut)
			
		#calculate operations
		sumAB = addMatrix(A, B)
		diffAB = subMatrix(A, B)
		scalarA = scalarMultiply(A, c)
		dotAD = dot(A, D)
			
		#print results
		outputMatrix('A+B', sumAB, fileOut)
		outputMatrix('A-B', diffAB, fileOut)
		outputMatrix('cA', scalarA, fileOut)
		outputMatrix('A dot D', dotAD, fileOut)

	fileIn.close() 
	fileOut.close()
	
	#matrixAdd(A, B)
# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	