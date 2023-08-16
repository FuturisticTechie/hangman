
import random               #This imports the random module for use to generate random letters later on

word_list = ['apple', 'kiwi', 'pineapple', 'strawberry', 'grapes']  #This is my source list of favourite fruits, printed in the following line
print(word_list)

word = random.choice(word_list)  #This fucntion is what was imported from random at the start of this file, and generates a random word from the source list word_list
print(word)


guess = input("Please enter a single letter ")      #This variable includes a fucntion that requires a user to input a single letter
if len(guess) == 1 and isinstance(guess, str):      #This ensures that 2 conditions are met: that the length of input is one letter only, and that the input is a str
    print("Good guess!")
else:
    print("Oops! That is not a valid input!")

print(guess)

