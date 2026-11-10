marks = [85, 90, 25, 60, 30, 75]

print("Student Marks:", marks)

print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

average = sum(marks) / len(marks)
print("Average Mark:", average)

passed =0 

for mark in marks:
    if mark >= 35:
        passed +=1

print("Number of Passed Students:", passed)
