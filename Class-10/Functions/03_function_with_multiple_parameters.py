# StudentPy
# Class 10 - Functions
# Program: Function with Multiple Parameters

def introduce(name, age, grade):
    print("Name:", name)
    print("Age:", age)
    print("Class:", grade)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
grade = int(input("Enter your class: "))

introduce(name, age, grade)
