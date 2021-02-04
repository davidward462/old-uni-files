#classes practice

def printClass(self):
	print(self.name, self.age, str(self.height) +"m") 

def main():

	class Human:
		def __init__(self, name, age, height):
			self.name = name
			self.age = age
			self.height = height
	
	h1 = Human("Billy", 40, 1.8)
	
	printClass(h1)
	
	
main()

