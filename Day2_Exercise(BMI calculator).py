#this program calculates the BMI of a person using their height and weight

print("Welcome to your BMI calculator!")

#assigning float data type to the input so both decimals and integers can be entered
#the float converts the input from a string to decimal numbers for easy mathematical operations
height = float(input("enter your height in metres:  "))
weight = float(input("enter your weight in kg:  "))

#using the formula for BMI calculation and leaving the result in integer(whole number) format
BMI = int(weight / (height)**2)

print("Your BMI is = ", BMI, "kg/m2")