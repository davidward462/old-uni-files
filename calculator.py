#Adds var1 and var2
def add(var1, var2):
	return var1 + var2

#Subtracts var1 and var2	
def sub(var1, var2):
	return var1 - var2

#Multiplies var1 and var2	
def mult(var1, var2):
	return var1 * var2	

#Divides var1 and var2	
def div(var1, var2):
	return var1 / var2	
	
def main():
	
		num1 = int(input("Enter first value: "))
		action = input("What do you want to do? 1) add 2) subtract 3) multiply 4) divide. Enter number: ") #get input from user of mathamatical operation
		op = int(action) #changes action string to int
		num2 = int(input("Enter second value: "))
		if(op == 1):
			print(add(num1, num2))
		elif(op == 2):
			print(sub(num1, num2))
		elif(op == 3):
			print(mult(num1, num2))
		elif(op == 4):
			print(div(num1, num2))
		else:
			print('Does not compute.')
			

main()	
	