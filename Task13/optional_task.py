#CJ Patel
#Task13 - optional_task.py
#------------------------------------------------------------#
#request input from user
num = int(input("Please enter a number less than 100: "))
while(num>=100):
	num = int(input("Please enter a number less than 100: "))

#determine if num is an odd or even number
if(num%2==0):
	print(str(num*2))
else:
	print(str(num*3))