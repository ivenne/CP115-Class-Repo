# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

# Without \n - everything prints on one line
# Without \t - no spacing
                                      
Coffee = 3.5
QtyCoffee = int(input("Enter coffee quantity: ")) 
Muffin = 2.1
QtyMuffin = int(input("Enter muffin quantity:" ))
Water = 1.05
QtyWater = int(input("Enter water quantity:" ))
Total = (Coffee* QtyCoffee) + (Muffin * QtyMuffin) + (Water * QtyWater)
Receipt = "\n========== Receipt ==========\n\nItem\tPrice\tQty\tTotal\nCoffee\t$3.50\t{QtyCoffee}\t"
