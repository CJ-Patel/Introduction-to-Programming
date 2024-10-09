#CJ Patel
#Task11 - task1.py
#------------------------------------------------------------#
#initialising number value to three variables
num1 = 13
num2 = 30
num3 = 24

#compare num1 and num2 and print the larger value
if(num1>num2):
	print("Larger value is num1: " + str(num1))
else:
	print("Larger value is num2: " + str(num2))

#determine if num1 is odd or even and print result
if(num1%2 == 0):
  print(str(num1) + " is an even number")
else:
	print(str(num1) + " is an odd number")

#sort from largest to smallest
if(num1<num2):
	temp = num1
	num1= num2
	num2 = temp
if(num2<num3):
	temp = num2
	num2 = num3
	num3 = temp

#display largest to smallest
#print("Largest to smallest:")
#print("num1: " + str(num1))
#print("num2: " + str(num2))
#print("num3: " + str(num3))
