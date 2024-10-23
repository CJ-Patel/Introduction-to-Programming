#CJ Patel
#Task19 - combined.py
#------------------------------------------------------------#
#initialise variables
contents =""

num1 = 0
numbers1 = ""
numbers1 = numbers1.split()

num2 = 0
numbers2 = ""
numbers2 = numbers2.split()

all_numbers = ""
all_numbers = all_numbers.split()
#------------------------------------------------------------#
#open numbers1.txt
ofile = open('numbers1.txt', 'r+')
#read content of numbers1.txt into numbers1
for line in ofile:
  contents+=line
  num1 = int(line)
  numbers1.append(num1)
#close numbers1.txt
ofile.close()
#------------------------------------------------------------#
#open numbers2.txt
pfile = open('numbers2.txt', 'r+')
#read content of numbers2.txt into numbers2
for line in pfile:
  contents+=line
  num2 = int(line)
  numbers2.append(num2)
#close numbers2.txt
pfile.close()
#------------------------------------------------------------#
#combine contents of numbers1.txt and numbers2.txt
all_numbers = numbers1 + numbers2
#sort the combined contents of numbers1.txt and numbers2.txt
all_numbers = sorted(all_numbers)
#------------------------------------------------------------#
#create all_numbers.txt
newfile = open('all_numbers.txt', 'w')
#write content of all_numbers into all_numbers.txt
for i in range (0,len(all_numbers)):
  newfile.write(str(all_numbers[i]) + "\n")
#close numbers.txt
newfile.close()