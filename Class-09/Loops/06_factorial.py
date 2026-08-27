# StudentPy
# Class 9 - Loops
# Program: Calculate Factorial

number = int(input("Enter a non-negative integer: "))

factorial = 1

for value in range(1, number + 1):
    factorial *= value

print("Factorial:", factorial)
