def average(marks):
    return sum(marks) / len(marks)

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A Grade"
    elif avg >= 75:
        return "B Grade"
    elif avg >= 50:
        return "C Grade"
    else:
        return "Fail"

marks = [85, 90, 75, 80, 95]

avg = average(marks)

print("Average:", avg)
print("Highest:", highest(marks))
print("Lowest:", lowest(marks))
print("Grade:", grade(avg))