minutesBefore = int(input())
membership = (input().lower == 'true')
if minutesBefore > 30:
    ticket = 80 - 15
else:
    if minutesBefore < 0:
        price = 0
    else:
        ticket = 80
if membership:
    price = price - 0.15 * price + ticket
else:
    price = price + ticket
print(price)
