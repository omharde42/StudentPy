# StudentPy
# Class 10 - Tuples
# Program: Search for an Element in a Tuple

fruits = ("Apple", "Banana", "Mango", "Orange")

fruit = input("Enter a fruit to search: ")

if fruit in fruits:
    print(fruit, "is present in the tuple.")
else:
    print(fruit, "is not present in the tuple.")
