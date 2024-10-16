#CJ Patel
#Task14 - task3.py
#------------------------------------------------------------#
#while loop displaying countdown from 20 to 0
i=20
while (i>-1):
	print(i)
	i=i-1

print()
#loop that will display all even numbers between 1 and 20
for j in range(1,20):
	if(j%2==0):
		print(j)

print()
#loop for pattern
for k in range (0,6):
	for l in range (0,k):
		print('*', end='')
	print()

print()
#determine the greatest common divisor/highest common factor of 2 positive integers
#request input from user
num1 = int(input("Please enter a positive integer for num1: "))
num2 = int(input("Please enter a positive integer for num2: "))

#sort smallest to biggest
if (num1>num2):
	temp = num1
	num1 = num2
	num2= num1

#determine gcd
for m in range (1,num1+1):
	if (num1%m==0 and num2%m==0):
		gcd=m
print("GCD: " + str(gcd))