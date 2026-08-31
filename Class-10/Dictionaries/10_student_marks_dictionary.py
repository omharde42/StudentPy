# StudentPy
# Class 10 - Dictionaries
# Program: Store and Display Student Marks

marks = {
    "Mathematics": 85,
    "Science": 78,
    "English": 92
}

total = sum(marks.values())
average = total / len(marks)

print("--- Student Marks ---")

for subject, mark in marks.items():
    print(subject, ":", mark)

print("Total:", total)
print("Average:", average)
