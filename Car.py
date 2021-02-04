#Ch 1 programmming exercise 2

class Car():
	def __init__(self, yearModel, make, speed = 0):
		self.__yearModel = yearModel
		self.__make = make
		self.__speed = speed
	
	def accelerate(self):
		self.__speed += 5
		
	def deccelerate(self):
		self.__speed -= 5
	
	def getSpeed(self):
		return self.__speed
		
def main():

	car1 = Car("1974", "Pontiac Firebird")
	print()
	
	print("accelerating...")
	for i in range(5):
		car1.accelerate()
		print(car1.getSpeed())

	print("breaking...")
	for i in range(5):
		car1.deccelerate()
		print(car1.getSpeed())
		
main()
	
	