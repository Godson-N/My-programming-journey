#this code predicts if a given year is a leap year or not using a set of mathematical logic

year = int(input("Welcome, \nPlease enter the year you want to check:  "))

# the logic used is (i) the year must be divisible by 4 and must not be divisible by 100 without remiander
# (ii) if it is divisible by 100 without remainder, it must also be divisible by 400 without a remainder
# for this operation, I used the modulo (%) operator

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")