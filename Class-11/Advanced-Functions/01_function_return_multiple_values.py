# StudentPy
# Class 11 - Advanced Functions
# Program: Return Multiple Values

def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product


a = 20
b = 8

total, difference, product = calculate(a, b)

print("Sum:", total)
print("Difference:", difference)
print("Product:", product)
