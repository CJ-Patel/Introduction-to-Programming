#CJ Patel
#Task13 - names.py
#------------------------------------------------------------#
#request input from user
i=0
name = ""
while (name!="stop"):
	name=input("Please enter the names of all pupils in class: ").lower()
	i+=1

print("Number of pupils in class: " + str(i-1))