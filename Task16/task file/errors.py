# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program") #syntax error - missing parenthesis for python3;
print ("\n")  #syntax error - incorrect space indentation; #syntax error - missing parenthesis for python3;

ageStr = "24" #I'm 24 years old. #runtime error - double equal sign is for comparison; #syntax error - incorrect space indentation; #logic error - only integer values are needed
age = int(ageStr) #syntax error - incorrect space indentation;
print("I'm "+str(age)+" years old.") #syntax error - incorrect space indentation; #logical error - does not appropriate spacing required; #runtime error - need to convert variable age to string for print output
three = 3 #syntax error - incorrect space indentation; #logic error - adding quotes to value saves value as a string and not an int to be used efficiently in calculations (can be converted in calculations, but not efficient);

answerYears = age + three #syntax error - incorrect space indentation;

print ("The total number of years:" + str(answerYears)) #syntax error - missing parenthesis for python3; #logical error - variables should not be printed using quotations; #runtime error - need to convert variable answerYears to string for print output
answerMonths = answerYears*12 + 6 #runtime error - variable answer is not declared, should be answerYears; #logical error - need to compensate for another 6 months by adding 6
print ("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") #syntax error - missing parenthesis for python3; #runtime error - need to convert variable answerMonths to string for print output

#HINT, 330 months is the correct answer

