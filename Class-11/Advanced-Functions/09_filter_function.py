# StudentPy
# Class 11 - Advanced Functions
# Program: Using filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
