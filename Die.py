#Dice class for 110 assignment 6
import random

class Die():
	def __init__ (self):
		self.__faceUp
	
	def throw(self):
		self.__faceUp = random.randint(1, 6)
	
	def get_faceUp(self):
		return self.__faceUp
		