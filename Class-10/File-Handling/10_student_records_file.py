# StudentPy
# Class 10 - File Handling
# Program: Store Student Records in a File

name = input("Enter student name: ")
age = input("Enter student age: ")
grade = input("Enter student class: ")

with open("students.txt", "a") as file:
    file.write(
        f"Name: {name}, Age: {age}, Class: {grade}\n"
    )

print("Student record saved successfully.")
