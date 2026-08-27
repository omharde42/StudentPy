# StudentPy
# Class 10 - Strings
# Program: Count a Character

text = input("Enter a string: ")
character = input("Enter the character to count: ")

if len(character) == 1:
    count = text.count(character)
    print("Character count:", count)
else:
    print("Please enter exactly one character.")
