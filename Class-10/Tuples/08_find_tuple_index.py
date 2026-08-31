# StudentPy
# Class 10 - Tuples
# Program: Find the Index of an Element

fruits = ("Apple", "Banana", "Mango", "Orange")

fruit = input("Enter a fruit to find: ")

if fruit in fruits:
    position = fruits.index(fruit)
    print("Index:", position)
else:
    print("Fruit not found.")
