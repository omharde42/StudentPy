# StudentPy
# Class 11 - Advanced Functions
# Program: Local and Global Variables

score = 50


def update_score():
    global score
    score = 100


print("Before:", score)

update_score()

print("After:", score)
