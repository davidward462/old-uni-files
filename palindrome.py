#check if string is a palindrome

def main():
	
	stringIn = input("Enter a word: ")
	
	#convert string to list
	text = []
	for letter in stringIn:
		text.append(letter)
	
	#reverse text and make into list
	reverseText = list(reversed(text))
	
	#print and make into string
	print("".join(reverseText))
		
	
main()