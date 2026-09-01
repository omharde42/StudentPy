# StudentPy
# Class 11 - Advanced Functions
# Program: Variable Scope

message = "Outside function"


def show_message():
    message = "Inside function"
    print(message)


show_message()

print(message)
