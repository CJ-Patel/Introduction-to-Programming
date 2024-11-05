#CJ Patel
#Task22 - counting.py
#------------------------------------------------------------#
#initialise variable 'sampleString'
sampleString = "google.com"
charFrequency = {}

#calculate number of times a character occurs
for i in sampleString:
	if i in charFrequency:
		charFrequency[i] +=1
	else:
		charFrequency[i] = 1

#print frequency
print(charFrequency)