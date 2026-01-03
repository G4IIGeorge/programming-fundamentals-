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

print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter choice (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == "1":
    print("Result:", add(num1, num2))
elif operation == "2":
    print("Result:", subtract(num1, num2))
elif operation == "3":
    print("Result:", multiply(num1, num2))
elif operation == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")
