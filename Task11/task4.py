#CJ Patel
#Task11 - task4.py
#------------------------------------------------------------#
#request input from user
num = int(input("Please enter an integer: "))


#determine if num is divisible by 2 and 5, by 2 or 5, or by neither
if(num%2==0 and num%5==0):
	print(str(num) + " is divisible by 2 and 5")
elif(num%2==0 or num%5==0):
	print(str(num) + " is divisible by 2 or 5")
else:
	print(str(num) + " is not divisible by 2 or 5")
