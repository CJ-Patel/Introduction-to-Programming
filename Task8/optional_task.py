#CJ Patel
#Task8 - optional_task.py
#------------------------------------------------------------#
#initialise boolean variables as False
temperature = False
weekend = False
sunny = False

#series of yes/no questions for each variable
question = input("Is the temparature greater than 20? yes/no: ").lower()
if (question == "yes"):
	temperature = True

question = input("Is it the weekend? yes/no: ").lower()
if (question == "yes"):
	weekend = True

question = input("Is it sunny? yes/no: ").lower()
if (question == "yes"):
	sunny = True
	
#determine clothes based off variables
if (temperature==True):
	shirt = "short-sleeved"
else:
	shirt = "long-sleeves"

if (weekend==True):
	pants = "shorts"
else:
	pants = "jeans"

if (sunny==True):
	extra = "cap"
else:
	extra = "raincoat"

#print sentence that fully describes the user's outfit
print("The user's outfit consists of: " + shirt + ", " + pants + " and a " + extra)