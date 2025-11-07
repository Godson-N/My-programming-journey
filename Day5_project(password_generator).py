# This code generates random passwords using certain specifications of the user

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z'
    ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to your password generator!")
num_letters = int(input("How many letters would you like to use? \n"))
num_numbers = int(input("How many numbers would you like to use? \n"))
num_symbols = int(input("How many symbols would you like to use? \n"))

for items in letters:
    password_letters = random.choices(letters, k=num_letters)

for items in numbers:
    password_nummbers = random.choices(numbers, k=num_numbers)

for items in symbols:
    password_symbols = random.choices(symbols, k=num_symbols)

sum_password_characters = password_letters + password_nummbers + password_symbols

#shuffling the items in the list
random.shuffle(sum_password_characters)

#changing the list to a string
password = ''.join(sum_password_characters)

print(f"Your generated password is:  {password}")