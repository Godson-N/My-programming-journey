# this code checks from a list of input and randomly picks a name to pay the bills

# using the split string method
names_string = input("Welcome!!! \nPlease give me the names of everyone, separated by a comma. \n")

names_in_list = names_string.split(", ")

# importing the random module and using the len() function
import random
names_length = len(names_in_list)

# Choosing randomly from the list
randomly_chosen_index = random.randint(0, names_length - 1)
bill_payer = names_in_list[randomly_chosen_index]

print(f"{bill_payer} gets to pay the bills")