student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]        #calling the value(score) of the dictionary
    if score > 90:
        student_grades[student] = "outstanding"         #assigning the key(student) and value(grades) to a new dictionary...
    elif score > 80:                                              #...from the previous dictionary after changing the values
        student_grades[student] = "Exceeds expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)