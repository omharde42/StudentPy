# StudentPy
# Class 10 - File Handling
# Program: Check Whether a File Exists

import os

filename = input("Enter the filename: ")

if os.path.exists(filename):
    print("File exists.")
else:
    print("File does not exist.")
