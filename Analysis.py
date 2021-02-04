#CSC 110 201809 Assignment 5
#David Ward
#15/11/18
#V00920409

import re

#count words
def wordTotal(wordList):
	count = 0
	for word in wordList: #loop through each element in wordlist
		count += 1
	return count

	
def wordFrequency(wordList):
	lowerWordList= []
	for item in wordList: #loop through each element in wordlist
		item = item.lower() #make each element lowercase
		lowerWordList.append(item)
	wordDict = {}
	for word in lowerWordList: #loop through each element in wordlist
		if word not in wordDict:
			wordDict[word] = 1
		else:
			wordDict[word] += 1
	return wordDict
	
	
def letterFrequency(wordList):
	letterDict = {}
	for word in wordList: #loop through each element in wordlist
		for ch in word: #loop through each char in the element
			if ch not in letterDict:
				letterDict[ch] = 1
			else:
				letterDict[ch] += 1
	return letterDict
		
	
#count uppercase and lowercase letters	
def letterCount(wordList):
	lower = 0
	upper = 0
	for word in wordList: #loop through each element in wordlist
		for ch in word: #loop through each char in the element
			if ch.islower(): #if char is lowercase
				lower += 1
			elif ch.isupper(): #if char is uppercase
				upper += 1
	return lower, upper #return num of upper and lower case letters
	

def formatData(data):
	data = data.strip() #strip newline

	list = re.split(" |\n",data) #split on space and newline
	
	#remove non-alphanumerical characters
	alNumList = []
	for word in list:
		for ch in word:
			if not ch.isalnum(): 
				#replace non alnum characters
				word = word.replace("(", "")
				word = word.replace(")", "")
				word = word.replace(".", "")
				word = word.replace(",", "")
				word = word.replace(":", "")
				word = word.replace(";", "")
				word = word.replace("'", "")
				word = word.replace("?", "")
				word = word.replace("!", "")
		alNum = word.isalnum() #check if word is an alphanum word
		if alNum:
			alNumList.append(word) #append to list
	
	return alNumList #return alphapetized list
	
	
def main():

	#open input and output files
	fileIn = open(r"D:\nkfyn\Documents\CSC 110 assignments\Assignment 5\balena.txt", "r")
	fileOut = open(r"D:\nkfyn\Documents\CSC 110 assignments\Assignment 5\balenaOutTest.txt", "w")
	
	data = fileIn.read() #read file
	
	wordList = formatData(data) #create formatted list 
	
	numWords = wordTotal(wordList) #get num of words
	
	lowerTotal, upperTotal = letterCount(wordList) #get num of upper and lower case letters
	
	wordFreqDict = wordFrequency(wordList)
	sortedWords = sorted(wordFreqDict)	#sort dictionary
	
	letterFreqDict = letterFrequency(wordList)
	sortedLetters = sorted(letterFreqDict) #sort dictionary
	
	#write to file
	fileOut.write("Words:" + str(numWords) + "\n")
	for word in sortedWords: #loop through alphapatized list
		fileOut.write(str(wordFreqDict[word]) + ": " + word.lower() + "\n")
	fileOut.write("Upper Case Letters: " + str(upperTotal) + "\n")
	fileOut.write("Lower Case Letters: " + str(lowerTotal) + "\n")
	for ch in sortedLetters: #loop through alphabetized letters
		fileOut.write(ch + ":" + str(letterFreqDict[ch]) + "\n")
	
	fileIn.close()
	fileOut.close()

# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	