#CJ Patel
#Task6 - optional_task.py
#------------------------------------------------------------#
#request input from user
#cast accordingly
print("Please enter the lengths of all three sides of a triangle:")
side1 = float(input("Please enter the length of side1: "))
side2 = float(input("Please enter the length of side2: "))
side3 = float(input("Please enter the length of side3: "))

#calculations for area
s= (side1+side2+side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5

#print area
print("Area: " + str(area))