# StudentPy
# Class 10 - Functions
# Program: Calculator Using Functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None

    return a / b


first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = add(first_number, second_number)
    print("Result:", result)

elif operator == "-":
    result = subtract(first_number, second_number)
    print("Result:", result)

elif operator == "*":
    result = multiply(first_number, second_number)
    print("Result:", result)

elif operator == "/":
    result = divide(first_number, second_number)

    if result is None:
        print("Cannot divide by zero.")
    else:
        print("Result:", result)

else:
    print("Invalid operator.")
