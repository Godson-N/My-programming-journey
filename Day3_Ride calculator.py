# this code determines if a person is qualified to take a rollercoaster ride from their height,
# and gives the cost of their bill

height = float(input("Welcome! Enter your height in cm: "))

if height > 120:
    age = int(input("Enter your age:  "))
    bill = 0
    photos = input("Would like some photos at a small cost, 'yes' or 'no':  ")
    if age < 12:
        bill += 5
        if photos == 'yes':
            bill += 3
        print(f"Your bill is ${bill}")
    elif age >= 12 and age <= 18:
        bill += 7
        if photos == 'yes':
            bill += 3
        print(f"Your bill is ${bill}")
    elif age >= 45 and age <= 55:
        print("You can enjoy the ride for free!!!")
    else:
        bill += 12
        if photos == 'yes':
            bill += 3
        print(f"Your bill is ${bill}")
else:
    print("You're not qualified to take this ride because you did not meet the height requirements. \nPlease try next time when you're taller. ")
