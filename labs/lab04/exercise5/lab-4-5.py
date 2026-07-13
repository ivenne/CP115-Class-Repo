scoreA = int(input())
scoreB = int(input())
if scoreA == scoreB:
    pointsA = 1
    pointsB = 1
else:
    if scoreA < 1:
        pointsB = 3 + 1
        pointsA = 0
    else:
        if scoreA > scoreB:
            pointsA = 3
        else:
            pointsB = 0
print(pointsA)
print(pointsB)
