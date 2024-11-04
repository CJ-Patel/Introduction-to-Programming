#CJ Patel
#Task21 - John.py
#------------------------------------------------------------#
#initialise variable 'name' and empty list variable 'incorrectNames'
name = ""
incorrectNames = []

while name != "John":
	#request input from user
	name = input("Enter your name: ")
	#add name to list if not John
	if name != "John":
		incorrectNames.append(name)

#print incorrectNames
print("Incorrect names: " + str(incorrectNames))
