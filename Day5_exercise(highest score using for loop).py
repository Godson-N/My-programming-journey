# This code finds the highest score from a list of input using For loops

student_scores = input("Enter the students scores: \n").split()

for s in range(0, len(student_scores)):
    student_scores[s] = int(student_scores[s])

print(student_scores)

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")
