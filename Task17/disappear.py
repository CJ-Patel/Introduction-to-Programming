#CJ Patel
#Task17 - disappear.py
#------------------------------------------------------------#
#request input from user
original = input("Please enter a value for a string variable: ")
characters = input("Which characters would you like to make disappear? ") #to be entered without commas or spaces
#characters = characters.replace(",","") ; if characters are seperated by commas
disappear = original

#remove specified characters
for i in range (0,len(characters)):
  disappear = disappear.replace(characters[i],"")

print(disappear)