#this code asks for an integer input and prints if the number is odd or even using if/else statements

number = int(input("Welcome! \n Please enter the number your want to check:  "))

#for a number to be even, the remainder must be zero when divided by 2
if number % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")