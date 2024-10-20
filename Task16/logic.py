#CJ Patel
#Task16 - logic.py
#------------------------------------------------------------#
#request user input
lap1 = input("Please enter time taken to finish lap1 in seconds: ") #logical error - needs to be converted to int
lap2 = input("Please enter time taken to finish lap2 in seconds: ") #logical error - needs to be converted to int
lap3 = input("Please enter time taken to finish lap3 in seconds: ") #logical error - needs to be converted to int

duration = lap1 + lap2 + lap3 #logical error - adding three string variables

print("Total time taken to complete race: " + duration) #logical error - variable duration's output value is equivalent to a mesh of variables lap1,lap2 and lap3