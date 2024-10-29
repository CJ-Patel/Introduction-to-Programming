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
#------------------------------------------------------------#
for line in userFile:
  contents = contents+line
contents=contents.split('\n')

while loggedIn == False:
  #request input from user
  userName = input("Please enter a username: ")
  password = input("Please enter password: ")
  
  #do not allow username to be equal to password
  if userName == password:
    print("Password cannot be same as username - please try again")
    continue

  for i in range(len(contents)):
    if contents[i].find(userName) != -1 and contents[i].find(password) != -1:
      loggedIn = True
      print("Log in successful!!")
  
  if loggedIn == False:
    print("Retry - ")
#------------------------------------------------------------#
#print empty line for readability
print()
#------------------------------------------------------------#
#print menu options
print("Please select one of the following options: ")
print("r - register user")
print("a - add task")
print("va - view all tasks")
print("vm - view all my tasks")
print("e - exit")
menu = input()

#register user
if menu == "r":
  confirmed = False
  while confirmed == False:
    #request input from user
    newUsername = input("Please enter a new username: ")
    newPassword = input("Please enter a password: ")
    #do not allow username to be equal to password
    if newUsername == newPassword:
      print("Password cannot be same as username - please try again")
      continue
    #request user for input
    confirmPassword = input("Please confirm password: ")  

    #write new user details and password to user.txt
    if (newPassword == confirmPassword):
      confirmed = True
      userFile.write("\n" + newUsername + ", " + newPassword)
      break
    else:
      print("Please Retry - ")

#add task
elif menu == "a":
  taskFile = open("tasks.txt",'a+')
  #request input from user
  person = input("Please enter the username of the person that the task is assigned to: ")
  title = input("Please enter the title of the task: ")
  description = input("Please enter a description of the task: ")
  dueDate = input("Please input the due date of the task: ")
  #determine current date
  today = date.today()
  currDate = str(today.strftime("%d-%b-%Y")).replace('-'," ")
  taskCompleted = "No"
  
  #write details to tasks.txt
  taskFile.write(person + ", " + title + ", " + description + ", " + currDate + ", " + dueDate + ", " + taskCompleted + "\n")
  taskFile.close()

#view all tasks
elif menu == "va":
  taskFile = open("tasks.txt", 'r+')
  for line in taskFile:
    line = line.replace(', ', '\t')
    print(line)
  print()
  taskFile.close()

#view all my tasks
elif menu == "vm":
  taskFile = open("tasks.txt", 'r+')
  for line in taskFile:
    myTask = ""
    line = line.split(', ')
    if line[0]==userName:
      for i in range (0, len(line)):
        myTask = myTask + line[i] +"\t"
      print(myTask)
  print()
  taskFile.close()

elif menu == "e":
  exit(0)
  print()

else:
  print("Invalid Input")
#------------------------------------------------------------#

#close files
#taskFile = open("tasks.txt",'r+')
#taskFile.close()
#userFile.open("user.txt", 'r+')
userFile.close()