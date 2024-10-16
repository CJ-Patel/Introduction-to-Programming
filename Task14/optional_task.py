#CJ Patel
#Task14 - optional_task.py
#------------------------------------------------------------#
#request input from user
num = int(input("Please enter a number: "))

#if num is more than 10 use for loop to print out num num amount of times, else display alt message
if(num>10):
	for i in range(0,num):
		print(num)
else:
	print("Sorry, too small")