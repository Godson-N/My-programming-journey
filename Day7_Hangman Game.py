# hangman game that loops based on a user's input

play_game = True

while play_game is True:

     #importing the words module and calling on the english_words list
     import words
     word_list = words.english_words
     
     #importing header and stages list from the hangman_art module(file)
     from art import header, stages

     print(f"Welcome to the Hangman Game. Let's play!! \n{header} \n")

     import random
     chosen_word = random.choice(word_list)

     display = []
     lives = 6

     for letter in chosen_word:
          display += "_"

     #converting the display list into a string
     print(" ".join(display))

     while "_" in display and lives > 0:
          guess = input("Guess a letter: ").lower()
          
          if guess not in chosen_word:
               lives -= 1
               print(f"The letter '{guess}' is not in the word, so you lose a life")
               print(stages[lives])

          elif guess in display:
               print("You have already guessed this letter")

          for position in range(len(chosen_word)):
               if guess == chosen_word[position]:
                    display[position] = guess
          
          new_display = " ".join(display)
          print(new_display)

          if "_" not in display:
               print("You won!!!")
          elif "_" in display and lives == 0:
               print(f"You lose. \nThe correct word is: '{chosen_word}'.")
     
     #making the game to loop again or stop based on user response
     go_again = True

     while go_again:
          response = input("Do you want to play again? Please choose 'yes' or 'no':  ").lower()

          if response == 'yes':
               go_again = False   # '=' assigns True to the variable go_again
               play_game = True 
          elif response == 'no':    # '==' compares the LHS and RHS
               go_again = False
               play_game = False 
          else:
               print("You did not enter a valid option. Please choose either 'yes' or 'no' ")  #loops 'go_again'