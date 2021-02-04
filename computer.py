#Classes lab 

class computer:
	#constructor
	def __init__(self, brand = "not defined", type = "not defined"):
		self.__brand = brand
		self.__type = type
		
	#this will be called when you try to print an instance of the class
	def __str__ (self):
		return self.__brand + " " + self.__type
	
	#"setter" method
	def setBrand(self, brand):
		self.__brand = brand
	
	#"getter" method
	def getBrand(self):
		return self.__brand
	
		#"setter" method
	def setType(self, type):
		self.__type = type
	
	#"getter" method
	def getType(self):
		return self.__type
		
	def checkBrand(self, string):
		if string == self.__brand:
			return True
		else:
			return False
		

def main():

	#create objects(instances) of the class
	comp1 = computer() #computer1 is and instance of the class computer
	print(comp1)
	
	comp1.setBrand("acer")
	comp1.setType("laptop")
	print(comp1)
	
	comp2 = computer("windows", "desktop")
	print(comp2)
	
	TrueFalse = comp2.checkBrand("windows")
	if TrueFalse:
		print("true")
	else:
		print("false")

if __name__ == "__main__":
	main()

