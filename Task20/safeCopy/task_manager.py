#CJ Patel
#Task20 - task_manager.py
#------------------------------------------------------------#
from datetime import date

#initialise variables
loggedIn = False
contents = ""
#contents = contents.split()

#userName = ""
#password = ""

#open files
userFile = open("user.txt", 'r+')
taskFile = open("tasks.txt",'r+')

while loggedIn == False:
  #request input from user
  userName = input("Please enter a username: ")
  password = input("Please enter password: ")

  for line in userFile:
    #line = line.split(', ')
    print("------")
    if (line.find(userName) != -1 and line.find(password) != -1):
      print("WORKED")
      loggedIn = True
      break
  if loggedIn == False:
    print("Retry - ")
  else:
    break
##CHECK FOR INCORRECT INPUTS


print()
#------------------------------------------------------------#
print("Please select one of the following options: ")
print("r - register user")
print("a - add task")
print("va - view all tasks")
print("vm - view all my tasks")
print("e - exit")
menu = input()

if menu == "r":
  confirmed = False
  while confirmed == False:
    #request input from user
    newUsername = input("Please enter a new username: ")
    newPassword = input("Please enter a password: ")
    confirmPassword = input("Please confirm password: ")
    #write new user details and password to user.txt
    if (newPassword == confirmPassword):
      confirmed = True
      userFile.write("\n" + newUsername + ", " + newPassword)
      break
    else:
      print("Please Retry - ")

elif menu == "a":
	#request input from user
	person = input("Please enter the username of the person that the task is assigned to: ")
	title = input("Please enter the title of the task: ")
	description = input("Please enter a description of the task: ")
	dueDate = input("Please input the due date of the task: ")
	#determine current date
	today = date.today()
	currDate = str(today.strftime("%d-%b-%Y")).replace('-'," ")
	taskCompleted = "No"

	taskFile.write(person + ", " + title + ", " + description + ", " + currDate + ", " + dueDate + ", " + taskCompleted)


elif menu == "va":
	for line in taskFile:
		line = line.replace(', ', '\t')
		print(line)
	print()

elif menu == "vm":
	for line in taskFile:
		if line.find(userName) != -1:
			line = line.replace(', ', '\t')
			print(line)
	print()

elif menu == "e":
	exit(0)
	print()

else:
	print("Invalid Input")
#------------------------------------------------------------#

toRead = input()



#close files
#taskFile = open("tasks.txt",'r+')
taskFile.close()
#userFile.open("user.txt", 'r+')
userFile.close()