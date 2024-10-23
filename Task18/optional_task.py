#CJ Patel
#Task18 - optional_task.py
#------------------------------------------------------------#
#insantiate variables
contents = ""
characters = 0
words = ""
lines = 0
vowels = 0
#open file and read data
f = open('input.txt', 'r+')
for line in f:
  contents = contents + line
  lines+=1
characters = len(contents)
words = contents.split()
f.close()

#determine number of vowels
for i in range (0,len(contents)):
  if(contents[i].lower() == "a" or contents[i].lower() == "e" or contents[i].lower() == "i" or contents[i].lower() == "o" or contents[i].lower() == "u"):
    vowels+=1

#display content of input.txt
print(contents)
print("------------------------------------------")
#display results
print("Number of characters: " + str(characters))
print("Number of words: " + str(len(words)))
print("Number of lines: " + str(lines))
print("Number of vowels: " + str(vowels))