# StudentPy
# Class 10 - Functions
# Program: Calculate Area Using Functions

def rectangle_area(length, width):
    return length * width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = rectangle_area(length, width)

print("Area of rectangle:", area)
