# StudentPy
# Class 10 - File Handling
# Program: Append Data to a File

text = input("Enter text to add: ")

with open("student.txt", "a") as file:
    file.write("\n" + text)

print("Data appended successfully.")
