#Ch 10 programming exercise 3

class Information():
	def __init__(self, name = "", birthdate = "", address = "", phoneNum = ""):
		self.__name = name
		self.__birthdate = birthdate
		self.__address = address
		self.__phoneNum = phoneNum
		
	#name funtions
	def setName(self, name):
		self.__name = name
		
	def getName(self):
		return self.__name
		
	#birthdate funtions
	def setBirthdate(self, birthdate):
		self.__birthdate = birthdate
		
	def getBirthdate(self):
		return self.__birthdate
		
	#address funtions
	def setAddress(self, address):
		self.__address = address
		
	def getAddress(self):
		return self.__address
		
	#phoneNum funtions
	def setPhoneNum(self, phoneNum):
		self.__phoneNum = phoneNum
		
	def getPhoneNum(self):
		return self.__phoneNum
		

def main():

	print()
	
	#create
	infoSet1 = Information()
	infoSet2 = Information()
	infoSet3 = Information()
	
	#set
	infoSet1.setAddress("my house")
	infoSet1.setBirthdate("a while ago")
	infoSet1.setName("Me")
	infoSet1.setPhoneNum("7783591582")
	
	#print
	print(infoSet1.getAddress())
	print(infoSet1.getBirthdate())
	print(infoSet1.getName())
	print(infoSet1.getPhoneNum())
	


main()