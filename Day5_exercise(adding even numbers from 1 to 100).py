# This code adds all even numbers from 1 to 100 using for loops and range function

sum_even_numbers = 0
for numbers in range(0, 101, 2):
    sum_even_numbers += numbers
print(f"The sum of the even numbers is: {sum_even_numbers}")