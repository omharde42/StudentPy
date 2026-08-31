# StudentPy
# Class 10 - File Handling
# Program: Read a File

with open("student.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)
