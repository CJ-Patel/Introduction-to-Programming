#CJ Patel
#Task5 - manipulation.py
#------------------------------------------------------------#
#request input from user
str_manip = input("Please enter a sentence: ")

#determine and display length of variable str_manip
length = len(str_manip)
print(length)

#determine last character of variable str_manip and replace all occurences of the character in the variable str_manip
#output result
last = str_manip[length-1]
print(str_manip.replace(last, "@"))

#determine and print the last 3 characters of the variable str_manip backwards
print(str_manip[-3:length][::-1])

#create and print a 5-letter word consisting of the first 3 the characters and the last 2 characters of the variable str_manip
print(str_manip[0:3] + str_manip[-2:length])

#display each word in the variable str_manip on a new line
print(str_manip.replace(" ", "\n"))