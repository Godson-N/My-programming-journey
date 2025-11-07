# This code prints the numbers from 1 to 100 but prints Fizz when the number is divisible by 3
# Buzz when the number is divisible by 5 and FizzBuzz when the number is divisible by both 3 and 5

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)