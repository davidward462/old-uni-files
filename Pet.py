#Ch 10 programming exercise 1

class Pet():
	def __init__(self, name  = "none", animalType = "none", age = 0):
		self.__name = name
		self.__animalType = animalType
		self.__age = age
		
	#set methods	
	def setName(self, name):
		self.__name = name
		
	def setAnimalType(self, animalType):
		self.__animalType = animalType
		
	def setAge(self, age):
		self.__age = age
	
	#get methods
	def getName(self):
		return self.__name
		
	def getAnimalType(self):
		return self.__animalType
		
	def getAge(self):
		return self.__age
		
		
def main():
	
	pet1 = Pet()
		
	#set
	name = input("Enter pet name: ")
	type = input("Enter pet type: ")
	age = int(input("Enter pet age: "))
	
	#assign
	pet1.setName(name)
	pet1.setAnimalType(type)
	pet1.setAge(age)
	
	#print
	
	print(pet1.getName())
	print(pet1.getAnimalType())
	print(pet1.getAge())
	
main()
	
		