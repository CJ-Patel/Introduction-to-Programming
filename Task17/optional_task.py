#CJ Patel
#Task17 - optional_task.py
#------------------------------------------------------------#
#request input from user
original = input("Please enter a value for a string variable: ").lower()

#determine if word is palindrome or not
if(original == original[::-1]):
	print("Your word is a palindrome")
else:
	print("Your word is not a palindrome")