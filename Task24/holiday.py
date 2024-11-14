#CJ Patel
#Task24 - holiday.py
#------------------------------------------------------------#
#function for cost of hotel per night
def hotel_cost(noOfNights):
	pricePerNight = 1300
	#return noOfNights*pricePerNight
	#calculation for totalHotelCost
	totalHotelCost = noOfNights*pricePerNight
	return totalHotelCost

#function for cost of flight based on city
def plane_cost(city):
	#determine flightCost
	if city == "johannesburg":
		flightCost = 720
	elif city == "durban":
		flightCost = 670
	elif city == "cape Town":
		flightCost = 1100
	else:
		#exit with message of invalid input
		exit("No flights to this city, or input was invalid. Exiting.")
	return flightCost

#function for cost of car rental per day
def car_rental(days):
	carRent = 500
	#return days* carRent
	#calculation for totalCarRent
	totalCarRent = days* carRent
	return totalCarRent

def holiday_cost():
	#request input from user
	noOfNights = int(input("Please enter the number of nights that you will be staying at the hotel: "))
	print()#print empty line for readability
	city = input("Please enter the city that you wish to travel to:\n- Johannesburg\n- Durban\n- Cape Town\n").lower()
	print()#print empty line for readability
	days = int(input("Please enter the numbers of days that you would like to rent a car for: "))
	print("--------------------------------------")#print line for readability

	#print details about holiday
	print("Hotel Cost: \tR" + str(hotel_cost(noOfNights)))
	print("Flight Cost: \tR" + str(plane_cost(city)))
	print("Car Rental: \tR" + str(car_rental(days)))
	print()#print empty line for readability

	#calculate totalHolidayCost by calling and adding all three functions together
	totalHolidayCost = hotel_cost(noOfNights) + plane_cost(city) + car_rental(days)
	return totalHolidayCost

#print results of function call for holiday_cost()
print("Total Holiday Cost: \tR"+ str(holiday_cost()))