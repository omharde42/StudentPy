# StudentPy
# Class 9 - Loops
# Program: Print a Star Pattern Using Nested Loops

rows = int(input("Enter the number of rows: "))

for row in range(1, rows + 1):
    for column in range(row):
        print("*", end=" ")
    print()
