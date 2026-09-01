# StudentPy
# Class 11 - Advanced Functions
# Program: Passing a Function as an Argument

def square(number):
    return number * number


def calculate(function, number):
    return function(number)


number = int(input("Enter a number: "))

result = calculate(square, number)

print("Result:", result)
