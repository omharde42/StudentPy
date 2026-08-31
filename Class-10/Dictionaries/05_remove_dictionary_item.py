# StudentPy
# Class 10 - Dictionaries
# Program: Remove an Item from a Dictionary

student = {
    "name": "Student",
    "age": 15,
    "city": "Pune"
}

removed_value = student.pop("city")

print("Removed value:", removed_value)
print("Updated dictionary:", student)
