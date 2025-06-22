def basic_operations(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    if b != 0:
        print(f"Division: {a} / {b} = {a / b}")
    else:
        print("Division: Cannot divide by zero")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function
basic_operations(num1, num2)
