#CJ Patel
#Task6 - shopping.py
#------------------------------------------------------------#
#request input from user
product1 = input("Please enter the name of product1: ")
product2 = input("Please enter the name of product2: ")
product3 = input("Please enter the name of product3: ")

#request input from user
#cast and round-off appropriately
price1 = float(input("Please enter the price of product1: "))
price1 = round(price1,2)
price2 = float(input("Please enter the price of product2: "))
price2 = round(price2,2)
price3 = float(input("Please enter the price of product3: "))
price3 = round(price3,2)

#calculations for total and average price of three products
total = round(price1+price2+price3, 2)
ave_price = round(total/3,2)

#print appropriate message with total and average price
print("The Total of " + product1 + ", " + product2 + ", " + product3 + " is R" + str(total) + " and the average price of the items are R" + str(ave_price) + ".")