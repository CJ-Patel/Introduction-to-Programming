#CJ Patel
#Task9 - courier.py
#------------------------------------------------------------#
#request input from user
price = float(input("Please enter the price of the package that you would like to purchase: "))
distance = float(input("Please enter the total distance of the delivery in kms: "))

#determine parcel final cost based on delivery preferences
question = input("Air or freight? ").lower()
if (question == "air"):
	deliveryCost = 0.36 * distance
else:
	deliveryCost = 0.25 * distance

question = input("Full or limited insurance? ").lower()
if (question == "full"):
	insurance = 50.00
else:
	insurance = 25.00

question = input("Gift or no gift? ").lower()
if (question == "gift"):
	gift = 15.00
else:
	gift = 0.00

question = input("Priority or standard delivery? ").lower()
if (question == "priority"):
	deliveryType = 100.00
else:
	deliveryType = 20.00

#Calculate total cost
totalDeliveryCost = round((price+deliveryCost+insurance+gift+deliveryType), 2)

#print total delivery cost
print("Total Delivery Cost: R" + str(totalDeliveryCost))