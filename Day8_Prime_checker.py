
import math
def prime_checker(number):

    int_square_rt = int(math.sqrt(number))
    is_prime = True
    
    if number == 0 or number ==1:
        print(f"{number} is not a prime number.")
        return

    for divisor in range(2, int_square_rt + 1):

        if number % divisor == 0:
            is_prime = False

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

print("Welcome to your prime checker.")
n = int(input("Enter the number:  "))
prime_checker(number = n)