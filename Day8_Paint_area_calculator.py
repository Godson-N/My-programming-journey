#This code calculates the paint area of a wall in a defined function

import math
def paint_calc(height, width, coverage):

    #the math.ceil rounds any float result to the next integer regardless of the decimal value to avoid shortage
    cans_needed = math.ceil((height * width) / coverage)
    print(f"You'll need {cans_needed} can(s) for the painting")

print("Welcome to your paint calculator.")

h = float(input("What is the wall height:  "))
w = float(input("What is the wall width:  "))
c = 5

paint_calc(width = w, height = h, coverage = c)