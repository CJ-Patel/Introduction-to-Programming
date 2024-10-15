#CJ Patel
#Task13 - while.py
#------------------------------------------------------------#
#request input from user
i = 0
num = 0
sum1 = 0
while(num!=-1):
	sum1+=num
	num = int(input("Please enter a number: "))
	i+=1

#calculate average
if(i!=1):
	average = sum1/(i-1)
	print(average)
else:
	print("Please enter at least one number")