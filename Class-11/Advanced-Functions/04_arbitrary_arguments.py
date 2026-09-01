# StudentPy
# Class 11 - Advanced Functions
# Program: Arbitrary Positional Arguments

def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Sum:", calculate_sum(10, 20, 30))
print("Sum:", calculate_sum(5, 10, 15, 20, 25))
