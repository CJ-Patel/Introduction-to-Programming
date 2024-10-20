# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.
 
name = "Tim"
surname = " Jones" #syntax error - incorrect space indentation; #possible logical error - extra spacing in beginning of string
age = 21
 
fullMessage = name + surname + " is " + str(age) + " years old" #Runtime error - variable age needs to be converted to string; #syntax error - 'is' is under the wrong syntax, needs to be within quotations; #possible logical error - missing appropriate spacing between name and surname;
 
print (fullMessage) #syntax error - missing parenthesis for python3;
