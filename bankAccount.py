#bank account class

class bankAccount():
	def __init__ (self, balance = 0):
		self.__balance = balance
		
	def __str__ (self):
		return str(self.__balance)
	
	def getBalance(self):
		return self.__balance
	
	def deposit(self, value):
		self.__balance += value
	
	def widthdrawl(self, widthdrawlValue):
		self.__balance -= widthdrawlValue
		return widthdrawlValue
		
		
def main():
	
	account1 = bankAccount(100)
	account2 = bankAccount(200)
	
	value = float(input("Value: "))
	pocket = account1.widthdrawl(value)
	print("1:", account1)
	
	account2.deposit(pocket)
	print("2:", account2)
	
	
main()