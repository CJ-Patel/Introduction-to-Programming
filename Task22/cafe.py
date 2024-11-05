#CJ Patel
#Task22 - cafe.py
#------------------------------------------------------------#
#initialise variable
totalStockWorth = 0
#create list variable 'menu' containing 4 items
menu = ['coffee', 'espresso', 'cappuccino', 'vanilla latte']
stock = { 'coffee': 31, 'espresso': 47, 'cappuccino': 52, 'vanilla latte': 25}
price = { 'coffee': 4, 'espresso': 3, 'cappuccino': 5, 'vanilla latte': 7}

#calculate total stock worth in cafe
for index, element in enumerate(menu):
	stockWorth = stock[element]*price[element]
	#print(element + ": \t" + str(stockWorth))
	totalStockWorth += stockWorth

#print total stock worth
print("Total Stock Worth: " + str(totalStockWorth))