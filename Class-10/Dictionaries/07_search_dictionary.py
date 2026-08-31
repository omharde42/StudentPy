# StudentPy
# Class 10 - Dictionaries
# Program: Search for a Key

student = {
    "name": "Student",
    "age": 15,
    "class": 10
}

key = input("Enter a key to search: ")

if key in student:
    print("Key found.")
    print("Value:", student[key])
else:
    print("Key not found.")
