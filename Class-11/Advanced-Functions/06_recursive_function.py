# StudentPy
# Class 11 - Advanced Functions
# Program: Recursion

def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    print("Factorial:", factorial(number))
