#CJ Patel
#Task25 - task_manager.py
#------------------------------------------------------------#
from datetime import date
from datetime import datetime
#------------------------------------------------------------#
#functions
#------------------------------------------------------------#
#register user
def reg_user():
  confirmed = False
  while confirmed == False:
    #request input from user
    newUsername = input("Please enter a new username: ")
    
    for i in range(len(contents)):
      exists = False
      #determine if username already exists in user.txt
      if contents[i].find(newUsername) != -1:
        print("There is already a user with this username. Please retry - ")
        exists = True
        continue
    #retry - user input
    if exists == True:
      continue
    
    #request input from user
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
#------------------------------------------------------------#
#add task
def add_task():
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
#------------------------------------------------------------#
#view all tasks
def view_all():
	taskFile = open("tasks.txt", 'r+')
	for line in taskFile:
		line = line.replace(', ', '\t')
		print(line)
	print()	#print empty line for readability
	taskFile.close()
#------------------------------------------------------------#
#view all my tasks
def view_mine():
	taskFile = open("tasks.txt", 'r+')
	content = ""
	#variable count for numbering tasks
	count = 1
	for line in taskFile:
		myTask = ""

		line = line.split(', ')
		if line[0]==userName:
			for i in range (0, len(line)):
				myTask = myTask + line[i] +"\t"
			print("[" + str(count) + "] - " + myTask)
			count += 1
	print()	#print empty line for readability
	
	taskFile.close()
#----------------------#
	task = int(input("Select a task by entering the corresponding number or -1 to return to prev menu: "))
	print()
	if task == -1:
		menu()
	else:
		taskFile1 = open("tasks.txt", 'r+')
		count = 1
		for line in taskFile1:
			myTask = ""
			line = line.split(', ')
			if line[0]==userName:
				for i in range (0, len(line)):
					myTask = myTask + line[i] +"\t"
				if count == task:
					print("[" + str(count) + "] - " + myTask)
				count += 1
		print()	#print empty line for readability
		taskFile1.close()
		#----------------------#
		print("What would you like to do with this specific task? Please select the appropriate option:")
		print("A - mark task as complete")
		print("B - edit the task")
		selection = input().lower()

		if selection == 'a':
			taskFile2 = open('tasks.txt', 'r+')
			
			count = 1
			for line in taskFile2:
				if line[0]==userName:
					if count == task:
						taskFile2.write(line.replace('No', 'Yes'))
					count += 1
			print()	#print empty line for readability
		elif selection == 'b':
			replace = input("What would you like to replace? ")

			taskFile2.close()

#------------------------------------------------------------#
#generate reports in two textfiles 'task_overview.txt' and 'user_overview.txt'
def generate_reports():

	totalTasks = 0
	completedTasks = 0
	incompleteTasks = 0
	overdue = 0
	incompleteAndOverdue = 0

	rep_taskFile = open('tasks.txt', 'r')
	for line in rep_taskFile:
		totalTasks +=1
		line1 = line.split(', ')
		if 'Yes' in line1[len(line1)-1]:
			completedTasks +=1

		if 'No' in line1[len(line1)-1]:
			incompleteTasks +=1

		currDate = date.today()
		date_str = line1[len(line1)-2]
		dueDate = datetime.strptime(date_str, '%d %b %Y').date()
		#dueDate = dueDate.strptime("%d-%b-%Y").replace(' ',"-")


		if currDate > dueDate:
			overdue +=1

		if 'Yes' in line1[len(line1)-1] and currDate - dueDate > 0:
			incompleteAndOverdue +=1

	rep_taskFile.close()

	percentageOfIncomplete = incompleteTasks/totalTasks * 100
	percentageofOverdue = overdue/totalTasks * 100
	#----------------------#
	taskOverviewFile = open('task_overview.txt', 'w')

	taskOverviewFile.write("Total number of tasks: " + str(totalTasks) + "\n")
	taskOverviewFile.write("Total number of completed tasks: " + str(completedTasks) + "\n")
	taskOverviewFile.write("Total number of incomplete tasks: " + str(incompleteTasks) + "\n")
	taskOverviewFile.write("Total number of incomplete and overdue tasks: " + str(incompleteAndOverdue) + "\n")
	taskOverviewFile.write("Total percentage of incomplete tasks: " + str(percentageOfIncomplete) + "%" + "\n")
	taskOverviewFile.write("Total percentage of overdue tasks: " + str(percentageofOverdue) + "%" + "\n")

	taskOverviewFile.close()
	#----------------------#
	totalUsers = 0
	users = []
	userTotalNumberOfTasks = 0
	userCompletedTasks = 0
	userInCompleteTasks = 0
	userOverdue = 0
	userIncompleteAndOverDue = 0
	rep_userFile = open('user.txt', 'r')

	for line2 in rep_userFile:
		totalUsers +=1
		split = line2.split(', ')
		users.append(split[0])

	totalUsersGenerated = totalUsers-1
	
	userOverviewFile = open('user_overview.txt', 'w')
	userOverviewFile.write("Total number of users registered: " + str(totalUsers) + "\n")
	userOverviewFile.write("Total number of users generated and tracked: " + str(totalUsersGenerated) + "\n")
	
	for i in range(0, len(users)):
		rep_taskFile = open('tasks.txt', 'r')
		for line3 in rep_taskFile:
			if users[i] in line3:
				userTotalNumberOfTasks +=1
				line4 = line3.split(', ')
				if 'Yes' in line4[len(line4)-1]:
					userCompletedTasks +=1

				if 'No' in line4[len(line4)-1]:
					userInCompleteTasks +=1

				currDate = date.today()
				date_str = line4[len(line4)-2]
				dueDate = datetime.strptime(date_str, '%d %b %Y').date()

				if currDate > dueDate:
					userOverdue +=1

				if 'Yes' in line1[len(line4)-1] and currDate - dueDate > 0:
					userIncompleteAndOverDue +=1
		rep_taskFile.close()

		userPercentageOfCompletedTasks = userCompletedTasks/userTotalNumberOfTasks * 100
		userPercentageOfIncompleteTasks = userInCompleteTasks/userTotalNumberOfTasks *100
		userPercentageOfIncompleteAndOverdue = userIncompleteAndOverDue/userTotalNumberOfTasks * 100
		userPercentageofOverdue = userOverdue/userTotalNumberOfTasks * 100

		userOverviewFile.write("User: " + users[i])
		userOverviewFile.write("Total number of tasks: " + str(userTotalNumberOfTasks) + "\n")
		userOverviewFile.write("Percentage of tasks completed by user: " + str(userPercentageOfCompletedTasks) +"%" + "\n")
		userOverviewFile.write("Percentage of tasks not completed by user as yet: " + str(userPercentageOfIncompleteTasks) +"%" + "\n")
		userOverviewFile.write("Percentage of tasks incomplete and overdue: " + str(userPercentageOfIncompleteAndOverdue) +"%" + "\n")
		userOverviewFile.write("Percentage of tasks overdue: " + str(userPercentageofOverdue) +"%" + "\n")


	rep_userFile.close()
	userOverviewFile.close()
	reportsGenerated = True

#------------------------------------------------------------#
#display statistics
def display_statistics():
	generate_reports()
	taskOverviewFile = open('task_overview.txt', 'r')
	print("Task Overview File")
	for taskLine in taskOverviewFile:
		print(taskLine)

	taskOverviewFile.close()
	#----------------------#
	userOverviewFile = open('user_overview.txt', 'r')
	print("User Overview File:")
	for userLine in userOverviewFile:
		print(userLine)

	userOverviewFile.close()
#------------------------------------------------------------#
#print menu options
def menu():
	print("Please select one of the following options: ")
	print("r - register user")
	print("a - add task")
	print("va - view all tasks")
	print("vm - view all my tasks")
	print("gr - generate reports")
	print("ds - display statistics")
	print("e - exit")
	menuOption = input()

	#call register_user function
	if menuOption == "r":
	  reg_user()

	#call add_task function
	elif menuOption == "a":
	  add_task()

	#call view_all function
	elif menuOption == "va":
	  view_all()

	#call view_mine function
	elif menuOption == "vm":
	  view_mine()

	elif menuOption == "gr":
		generate_reports()

	elif menuOption == "ds":
		if reportsGenerated == True:
			display_statistics()
		else:
			generate_reports()
			display_statistics()

	#exit
	elif menuOption == "e":
	  exit(0)
	  print()

	#error message for invalid input
	else:
	  print("Invalid Input")

#------------------------------------------------------------#
#Main code
#------------------------------------------------------------#
#log in
#initialise variables
loggedIn = False
contents = ""
reportsGenerated = False

#open user.txt file
userFile = open("user.txt", 'r+')
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
#display menu
menu()
#------------------------------------------------------------#
#close user.txt file
userFile.close()
#------------------------------------------------------------#