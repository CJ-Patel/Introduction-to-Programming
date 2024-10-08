#CJ Patel
#Task10 - bmi_task.py
#------------------------------------------------------------#
#request input from user
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

#calculate bmi
bmi = weight/(height**2)

#display bmi and category associated
if (bmi >=30):
	print("BMI: " + str(bmi) + " - user is obese")
elif (bmi >=25):
	print("BMI: " + str(bmi) + " - user is overweight")
elif (bmi >=18.5):
	print("BMI: " + str(bmi) + " - user is normal")
elif (bmi <18.5):
	print("BMI: " + str(bmi) + " - user is underweight")