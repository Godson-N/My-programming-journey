#this code collects two names of two people and calculates their love scores

print("Welcome to your love calculator!")

#Asking for name input and converting all letters to lower case using the lower() function
name1 = input("Please enter a name:\n").lower()
name2 = input("Please enter the other name:\n").lower()

#Assigning the words 'true' and 'love' to 'word1' and 'word2'
word1 = "true"
word2 = "love"

#Concatenating name1 and name2
combined_names = name1 + name2

#Assigning the sum of the occurences for each word
summation1 = 0
summation2 = 0

#using the for loop to scan for the letters in each word and count them
for letter in word1:
    count = combined_names.count(letter)
    summation1 += count

for letter in word2:
    count = combined_names.count(letter)
    summation2 += count

#converting summation1 and summation2 to string and concatenating
love_score = int(str(summation1) + str(summation2))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}. you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
    print(f"Your love score is {love_score}. You are alright together")
else:
    print(f"Your love score is {love_score}.")