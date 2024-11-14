#CJ Patel
#Task24 - my_function.py
#------------------------------------------------------------#
#function prints out days of the week
def daysOfTheWeek():
	print("Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday")

#function call for daysOfTheWeek()
daysOfTheWeek()

#print empty line for readability
print()

#function takes in sentence and replaces every second word with the word 'Hello'
def replaceWithHello(sentence):
	newSentence = ""
	sentence = sentence.split()
	for i in range(0,len(sentence)):
		if(i%2 != 0):
			sentence[i] = 'Hello'
		if i!=len(sentence):
			newSentence += sentence[i] + " "
		else:
			newSentence += sentence[i]
	return newSentence

#initialise sampleSentence to test function
sampleSentence = "This is the sample sentence"
#print sampleSentence to compare original sentence with newSentence
print(sampleSentence)
#print results of function call for replaceWithHello()
print(replaceWithHello(sampleSentence))