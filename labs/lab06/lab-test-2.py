"programmer: ivenne"
"problem description: Make a python program that use appropriate escape characters and arithmetic expression"

"enter the student's marks"
mark = int(input("Enter your marks:"))
fullmark = 2 * mark

"Student info will be shown here"
StudentInfo = f"""\nName: Ahmad Bin Abu\t\tMatric. No: MS2025123499\n\n*\t\t\t*\n**\t\t**\n***\t***\n********\n***\t***\n**\t\t**\n*\t\t\t*\n\n\nThis is my\n\tsecond\n\t\tassignment\nI want 2x 10 marks, which is {fullmark} full marks """
print(StudentInfo)
