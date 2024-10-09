#CJ Patel
#Task11 - task2.py
#------------------------------------------------------------#
#import math library for use of pi
import math

#request input from user
shape = input("Please enter the shape of the building. Square, rectangular or round? ").lower()

#request dimensions of square and calculate area
if(shape == "square"):
	length = float(input("Please enter length: "))
	area = length**2
	print("Area: " + str(area))

#request dimensions of rectangular shape and calculate area
if(shape == "rectangular"):
	length = float(input("Please enter length: "))
	width = float(input("Please enter width: "))
	area = length*width
	print("Area: " + str(area))

#request dimensions of round shape and calculate area
if(shape == "round"):
	radius = float(input("Please enter radius: "))
	area = math.pi*(radius**2)
	print("Area: " + str(area))