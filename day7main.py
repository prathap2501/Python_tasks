import day7calc
from datetime import date

print("===== Calculator Menu =====")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", day7calc.add(a, b))

elif choice == 2:
    print("Result:", day7calc.sub(a, b))

elif choice == 3:
    print("Result:", day7calc.mul(a, b))

elif choice == 4:
    print("Result:", day7calc.div(a, b))

else:
    print("Invalid choice")

print("Today's Date:", date.today())