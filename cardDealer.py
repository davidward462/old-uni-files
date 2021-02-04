#card dealer

import random

def createDeck():
	#key is card name
	#value is card value
	deck = ['Ace of Spades', ' of Spades', ' of Spades' ' of Spades' ' of Spades'
	' of Spades', ' of Spades', ' of Spades', ' of Spades', ' of Spades' 
	'Jack of Spades', 'Queen of Spades', 'King of Spades',

	'Ace of Hearts', ' of Hearts', ' of Hearts', ' of Hearts', ' of Hearts',
	' of Hearts', ' of Hearts', ' of Hearts', ' of Hearts', ' of Hearts', 
	'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 

	'Ace of Diamonds', ' of Diamonds', ' of Diamonds', ' of Diamonds', ' of Diamonds',
	' of Diamonds', ' of Diamonds', ' of Diamonds', ' of Diamonds', ' of Diamonds', 
	'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 

	'Ace of Clubs', ' of Clubs', ' of Clubs', ' of Clubs', ' of Clubs',
	' of Clubs', ' of Clubs', ' of Clubs', ' of Clubs', ' of Clubs', 
	'Jack of Clubs', 'Queen of Clubs', 'King of Clubs']
	
	return deck


def deal(deck, handSize):
	hand = []
	for i in range(handSize):
		choiceIndex = random.randint(0, 52)
		hand.append(deck[choiceIndex])
		del deck.choiceIndex
		print(choiceIndex)
	#return hand

	
def main():

	deck = createDeck()
	handSize = int(input("How many cards to deal? "))
	deal(deck, handSize)
	#print(hand)
	
main()
