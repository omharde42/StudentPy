# StudentPy
# Class 10 - File Handling
# Program: Copy File Content

with open("student.txt", "r") as source:
    content = source.read()

with open("student_copy.txt", "w") as destination:
    destination.write(content)

print("File content copied successfully.")
