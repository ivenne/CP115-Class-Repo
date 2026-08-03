item1 = input("Enter item 1: ")
price1 = int(input("Enter price 1: "))
item2 = input("Enter item 2: ")
price2 = int(input("Enter price 2: "))
item3 = input("Enter item 3: ")
price3 = int(input("Enter price 3: "))

totalPrice = (price1 + price2 + price3) 
subtotal = totalPrice
taxRate = (price1 + price2 + price3) * 0.06
totalcost = totalPrice - ((price1 + price2 + price3) * 0.06)

print(subtotal)
print(taxRate)
print(totalcost)