#CJ Patel
#Task5 - optional_task.py
#------------------------------------------------------------#
#request input from user
#use casting of string to int for variable int_fav
fav_rest = input("Please enter your favourite restuarant: ")
int_fav = int(input("Please enter your favourite number: "))

#print variable values
print(fav_rest)
print(int_fav)

#attempt to cast from string to int where string consists of letters, hence not valid input for int variable
#fav_rest = int(fav_rest)
#casting string to int causes an error as you cannot convert strings to integers, because the the types differ such that an int data type is to contain integers only and cannot contain letters or symbols, however the reverse conversion is still applicable.