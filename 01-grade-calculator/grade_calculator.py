# Student Grade Calculator that asks for a student name and marks, calculate the percentage and displayed if they passed or not
# Reject marks below 0 and over 100

student_name = input("Enter your name: ")
student_marks = int(input("Enter your marks: "))

if student_marks < 0 or student_marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
elif student_marks < 49:
    print(student_name + ": Failed")
else:
    print(student_name + ": Passed")
