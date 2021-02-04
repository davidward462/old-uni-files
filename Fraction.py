class Fraction():
	def __init__ (self):
		self.__num = 0
		self.__den = 1
	
	def getNum(self):
		return self.__num

	def getDen(self):
		return self.__den

	def setNum(self, newNum):
		self.__num = newNum

	def setDen(self, newDen):
		self.__den= newDen

	def toDec (self):
		return self.__num/self.__den

