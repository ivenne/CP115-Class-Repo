weight = int(input())
ticketPrice = int(input())
if baggage > 0:
    finalPrice = ticketPrice - 10
else:
    if weight > 16:
        finalPrice = 4 * weight - 15
    else:
        finalPrice = ticketPrice
print(finalPrice)
