#CJ Patel
#Task22 - optional_task.py
#------------------------------------------------------------#
#dictionary containing 4 abbreviations and their meanings
abbreviation = {'ADSL':'Asymmetric Digital Subscriber Line', 'WWW': 'World Wide Web', 'HTTP':'HyperText Transfer Protocol', 'CPU': 'Central Processing Unit'}

#add 2 more abbreviations and their meanings
abbreviation['API'] = 'Application Programming Interface'
abbreviation['IDE'] = 'Integrated Development Environment'

#request input from user
abb = input("Please enter an abbreviation (not case sensitive): ").upper()

#check if abbreviation is in dictionary and print out meaning or error message
for i in abbreviation:
	if(i in abb):
		print(abbreviation[abb]) #prints value where key is abbreviation given by user
		break
else:
	print("Abbreviation not found")