# StudentPy
# Class 10 - File Handling
# Program: Search for Text in a File

search_text = input("Enter text to search: ")

with open("student.txt", "r") as file:
    content = file.read()

if search_text in content:
    print("Text found in the file.")
else:
    print("Text not found.")
