grade = float(input())
valid_count = 0
total_grade = 0
average = 0

while grade != -1 :
    if (grade <= -1) or (grade >= 101) :
        grade = float(input())
        continue

    valid_count += 1 
    total_grade += grade
    average = total_grade / valid_count
    grade = float(input())

print(valid_count)
print(f"{average:.2f}")
