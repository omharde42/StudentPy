# StudentPy
# Class 10 - Lists
# Program: Search for an Element in a List

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruit = input("Enter a fruit to search: ")

if fruit in fruits:
    print(fruit, "is present in the list.")
else:
    print(fruit, "is not present in the list.")
