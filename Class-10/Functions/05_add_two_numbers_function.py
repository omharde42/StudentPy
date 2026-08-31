# StudentPy
# Class 10 - Functions
# Program: Add Two Numbers Using a Function

def add(first_number, second_number):
    return first_number + second_number


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

result = add(first_number, second_number)

print("Sum:", result)
