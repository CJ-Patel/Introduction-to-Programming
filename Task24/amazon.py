#CJ Patel
#Task24 - amazon.py
#------------------------------------------------------------#
#open file input.txt
inFile = open('input.txt', 'r+', encoding='utf-8-sig')
#create file output.txt
outFile = open('output.txt','w')
#initialise variables
content = ""
total=0

#read contents of input.txt
for line in inFile:
	content += line
content = content.split('\n')

#determine operation and convert respective numbers from string to int
for i in range(0,len(content)):
  content[i] = content[i].split(':')
  numbers = list(content[i])
  numbers[1] = numbers[1].split(',')
  for j in range(len(numbers[1])):
      numbers[1][j] = int(numbers[1][j])
  #determine minimum int and write to output.txt
  if(numbers[0]=='min'):
    minimum = min(numbers[1])
    outFile.write("The min of " + str(numbers[1]) +" is " + str(minimum) + "\n")
  #determine maximum int and write to output.txt
  elif(numbers[0]=='max'):
    maximum = max(numbers[1])
    outFile.write("The max of " + str(numbers[1]) +" is " +str(maximum) + "\n")
  #determine average and write to output.txt  
  elif(numbers[0]=='avg'):
    for j in range(len(numbers[1])):
      total += numbers[1][j]
    average = total/len(numbers[1])
    outFile.write("The avg of " + str(numbers[1]) +" is " + str(average) + "\n")

#close file input.txt
inFile.close()
#close file output.txt
outFile.close()