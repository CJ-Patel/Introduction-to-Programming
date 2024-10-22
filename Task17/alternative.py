#CJ Patel
#Task17 - alternative.py
#------------------------------------------------------------#
#request input from user
original = input("Please enter a value for a string variable: ")
alt = ""

# make each alternate character an uppercase character and each other alternate character a lowercase character.
for i in range (0, len(original)):
	if(i%2==0):
		alt += original[i].upper()
	else:
		alt += original[i].lower()

#display result
print(alt)