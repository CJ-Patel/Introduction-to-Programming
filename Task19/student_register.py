#CJ Patel
#Task19 - student_register.py
#------------------------------------------------------------#
#request input from user
numberOfStudents = int(input("How many students are registering? "))

#create file
ofile = open('reg_form.txt', 'w')

#request ID and write to file
for i in range (0,numberOfStudents):
	ID = input("Please enter your ID: ")
	ofile.write(ID+"\n")

#close file
ofile.close()