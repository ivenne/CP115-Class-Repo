hours = int(input())
if hours < 3:
    parkingFee = 0
else:
    if hours <= 5:
        parkingFee = 2 * hours
    else:
        parkingFee = 3 * hours
if parkingFee > 31:
    parkingFee = 30
print(parkingFee)
