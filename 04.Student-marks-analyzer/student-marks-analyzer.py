students = [
    {"name": "Lerato", "mark": 45},
    {"name": "Sipho", "mark": 88},
    {"name": "Thabo", "mark": 67},
    {"name": "Amina", "mark": 32},
    {"name": "Naledi", "mark": 76}
]

# Print all students and their marks
for student in students:
    print(f"{student['name']} : {student['mark']}")

# Calculate the total and average
total = 0

for student in students:
    total += student['mark']

average = total / len(students)

print(f"The total is {total}")
print(f"The average mark is {average}")

# Find the highest mark and the student who achieved it
highest_student = students[0]

for student in students:
    if student['mark'] > highest_student['mark']:
        highest_student = student

print(f"The highest mark is {highest_student['mark']}")
print(f"The student with the highest mark is {highest_student['name']}")

#Count who passed and and who failed
passed = 0
failed = 0 

for student in students:
    if student['mark'] >= 50:
        passed += 1
    else:
        failed += 1

print(f"Students who passed : {passed}")
print(f"Students who failed : {failed}")
