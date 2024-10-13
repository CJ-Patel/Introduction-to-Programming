#CJ Patel
#Task12 - finance_calculators.py
#------------------------------------------------------------#
import math

#request user input
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print()
print("investment\t - to calculate the amount of interest you'll earn on interest")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan")
print()
calculation = input().lower()

#calculation for investment
if(calculation=="investment"):
	#request user for input
	deposit = float(input("Please enter amount that you wish to deposit: R"))
	interestRate = float(input("Please enter the interest rate in %: "))
	years = float(input("Please enter the amount of years that you plan on investing for: "))
	interest = input("Simple/compound interest? ").lower()

	#calculate amount according to simple or compound interest and display
	if(interest=="simple"):
		amount = round(deposit*(1+(interestRate/100)*years),2)
		print("Amount: R" + str(amount))
	elif(interest == "compound"):
		amount = round(deposit*math.pow(1+(interestRate/100), years),2)
		print("Amount: R" + str(amount))
	else:
		print("Invalid input")

#calculation for bond
elif(calculation=="bond"):
	#request user for input
	presentValue = float(input("Please enter the present value of the house: R"))
	interestRate = float(input("Please enter the interest rate in %: "))
	months = float(input("Please enter the amount of months you plan to take to repay the bond: "))

	#calculate amount and display
	amount = round(presentValue*(((interestRate/100/12)*(math.pow((1+(interestRate/100/12)),months)/((math.pow((1+(interestRate/100/12)),months)-1))))),2)

	print("Amount to repay per month: R" + str(amount))

#display error message for invalid input
else:
	print("Invalid input. Aborting all calculations")