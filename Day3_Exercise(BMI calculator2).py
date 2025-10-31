#this code calculates the BMI of a person and tells if the person is underweight or overweight

print("Welcome to your BMI calculator!")

height = float(input("enter your height in metres:  "))
weight = float(input("enter your weight in kg:  "))

#using the formula for BMI calculation and leaving the result in float format and in 2 d.p
BMI = round((weight / (height)**2), 2)

print(f"Your BMI is = {BMI} kg/m2")

#using nested if statements to tell if the user is underweight or overweight

if BMI < 18.5:
    print("You are underweight! Eat up but eat healthy")

elif BMI < 25:
    print("You have a normal weight. keep it up!")

elif BMI < 30:
    print("You are overweight. Take it easy on the diet bro and lose some weight")

elif BMI < 35:
    print("You are obese!!")

else:
    print("You are clinically obese. OMG!!!")