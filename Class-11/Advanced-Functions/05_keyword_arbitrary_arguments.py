# StudentPy
# Class 11 - Advanced Functions
# Program: Arbitrary Keyword Arguments

def show_student(**details):
    for key, value in details.items():
        print(key, ":", value)


show_student(
    name="Student",
    age=16,
    class_name=11,
    city="Pune"
)
