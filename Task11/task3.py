#CJ Patel
#Task11 - task3.py
#------------------------------------------------------------#
#request input from user
swimming = float(input("Please enter time taken to complete swimming: "))
cycling = float(input("Please enter time taken to complete cycling: "))
running = float(input("Please enter time taken to complete running: "))

#calculate and diplay of total time taken
total_time = swimming + cycling + running
print("Total Time Taken: " + str(total_time))

#determine and display award
if(total_time<=100):
	print("Award: Provincial Colours")
elif(total_time<=105):
	print("Award: Provincial Half Colours")
elif(total_time<=110):
	print("Award: Provincial Scroll")
else:
	print("Award: No award")

