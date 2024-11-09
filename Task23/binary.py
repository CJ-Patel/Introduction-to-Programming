#CJ Patel
#Task23 - binary.py
#------------------------------------------------------------#
#import math library
import math

#request input from user
binary = list(input("Please enter a binary value: "))

#initialise variable for calculation of binary to decimal
decimal = 0

#calculations for binary to decimal
for i in range(0,len(binary)):
	digit = binary.pop()
	if digit == '1':
		decimal = decimal + pow(2,i)

#print decimal
print("Decimal: " + str(decimal))
#------------------------------------------------------------#
#alternative code without using math library or lists
##request input from user
#binary = input("Please enter a binary number: ")
#convert binary input to decimal
#decimal = int(binary,2)
#print decimal
#print("Decimal: " + str(decimal))
