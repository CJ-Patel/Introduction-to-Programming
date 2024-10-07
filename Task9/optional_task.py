#CJ Patel
#Task9 - optional_task.py
#------------------------------------------------------------#
#request input from user
employee = input("Are you a salesperson or a manager? ").lower()

#determine total monthly wage based on employee type
if(employee == "salesperson"):
	grossSales = float(input("What were your gross sales for the month? "))
	wages = 2000+(0.8 * grossSales)
else:
	hours = float(input("How many hours did you work for the month? "))
	wages = 40.00*hours

#print total monthly wage
print("Total monthly wage for employee: R" + str(wages))