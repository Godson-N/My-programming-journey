# This code plays the Rock, paper,scissors game

import random

rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)   '''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)   '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)   '''

options = [rock, paper, scissors]

print("Welcome to the rock, paper,scissors game!!!")
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors \n"))

computer_decision = random.randint(0, 2)
computer_choice = options[computer_decision]

if user_choice >= 3 or user_choice < 0:
    print(f"You typed a wrong input. \nComputer chose: {computer_choice} \nYou lose")
else:
    print("You chose:")
    print(options[user_choice])
        
    if user_choice == computer_decision:
        print(f"Computer chose: {computer_choice} \nIt's a draw")

    elif user_choice == 0 and computer_decision == 2:
        print(f"Computer chose: {computer_choice} \nYou win")

    elif user_choice == 1 and computer_decision == 0:
        print(f"Computer chose: {computer_choice} \nYou win")

    elif user_choice == 2 and computer_decision == 1:
        print(f"Computer chose: {computer_choice} \nYou win")

    else:
        print(f"Computer chose: {computer_choice} \nYou lose")