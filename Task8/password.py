#CJ Patel
#Task8 - password.py
#------------------------------------------------------------#
#initialise boolean variables as False
have_length = False
up_case = False
low_case = False
have_num = False

#variable for characteristics met
count = 0

#series of yes/no questions for each variable
question = input("Is your password at least 6 characters long? yes/no: ").lower()
if (question == "yes"):
	have_length = True
	count= count+1

question = input("Does your password contain an Upper Cased letter? yes/no: ").lower()
if (question == "yes"):
	upper_case = True
	count= count+1

question = input("Does your password contain an Lower Cased letter? yes/no: ").lower()
if (question == "yes"):
	lower_case = True
	count= count+1	

question = input("Does your password contain numbers? yes/no: ").lower()
if (question == "yes"):
	have_num = True
	count= count+1

#display message based off characteristics met
if (count>=3):
	print("Your password is suitable")
#else:
#  print("Your password is not suitable")