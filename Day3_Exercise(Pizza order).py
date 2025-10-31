#this code calculates the cost of pizza for a customer based on their order

print("Welcome to your pizza deliveries!")

size = input("Please enter the size of pizza you want. 'small', 'medium' or 'large': \n")

add_pepperoni = input("Do you want pepperoni? 'yes' or 'no':  ")
extra_cheese = input("Do you want extra cheese? 'yes' or 'no':  ")

bill = 0

if size == 'small':
    bill += 15
elif size == 'medium':
    bill += 20
elif size == 'large':
    bill += 25
else:
    print("Please enter the correct option from the menu")

if add_pepperoni == 'yes':
    if size == 'small':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'yes':
    bill += 1

print(f"Your bill is ${bill}")