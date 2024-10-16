#CJ Patel
#Task14 - task2.py
#------------------------------------------------------------#
#request input from user
startYear = int(input("What year do you want to start with?\t"))
years = int(input("How many years do you want to check?\t"))
print()

#determine if year is a leap year or not
for i in range(startYear, startYear+years):
	if(i%4==0):
		print(str(i) + " is a leap year")
	else:
		print(str(i) + " isn't a leap year")
