# StudentPy
# Class 10 - Strings
# Program: Find a Substring

text = input("Enter a string: ")
substring = input("Enter the text to find: ")

position = text.find(substring)

if position != -1:
    print("Found at index:", position)
else:
    print("Text not found.")
