# StudentPy
# Class 10 - Functions
# Program: Check Even or Odd Using a Function

def is_even(number):
    return number % 2 == 0


number = int(input("Enter an integer: "))

if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")
