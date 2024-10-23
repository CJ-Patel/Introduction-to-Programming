#CJ Patel
#Task18 - compulsory_task.py
#------------------------------------------------------------#
#instantiate variables for names, surnames and DOBs
contents = ""
name = ""
name = name.split()
surname = ""
surname = surname.split()
DOB = ""
DOB = DOB.split()
i = 0

#open file and read data into appropriate lists
f = open('DOB.txt', 'r+')
for line in f:
  #contents = contents + line
  contents = line.split()
  name.append(contents[i])
  surname.append(contents[i+1])
  DOB.append(str(contents[i+2]) + " " + contents[i+3] + " " + contents[i+4])
  i+=i
#close file
f.close()

#display Names
print("Name")
for i in range (0, len(name)):
  print(name[i][0] + " " + surname[i])
print()

#display Birthdates
print("Birthdate")
for i in range (0, len(name)):
  print(DOB[i])
print()