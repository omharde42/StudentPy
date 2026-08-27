# StudentPy
# Class 9 - Input and Output
# Program: Total Marks and Percentage

maths = float(input("Enter Mathematics marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total_marks = maths + science + english
percentage = (total_marks / 300) * 100

print("\n--- Result ---")
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
