"""
Simple calculator built while learning Python fundamentals.
Supports addition, subtraction, multiplication, and division.
"""



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
    choice = input("Choose: ")

    if choice == "5":
        print("Goodbye!")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print(add(num1, num2))
    elif choice == "2":
        print(subtract(num1, num2))
    elif choice == "3":
        print(multiply(num1, num2))
    elif choice == "4":
        print(divide(num1, num2))
    else:
        print("Invalid option")
