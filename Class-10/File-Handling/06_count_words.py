# StudentPy
# Class 10 - File Handling
# Program: Count Words in a File

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Number of words:", len(words))
