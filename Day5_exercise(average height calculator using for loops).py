# this code uses For loops to calculate the average height of a given set of inputs

students_heights = input("Enter the list of the heights \n").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

print(students_heights)

total_height = 0
number_of_students = 0

for height in students_heights:
    total_height += height
    number_of_students += 1
   
average_height = round((total_height / number_of_students), 2)
print(f"Average height = {average_height} cm") 