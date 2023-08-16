#####I have copied in some of the data from milestone_2.py 
#####This will need clean up/ making it into functions to stop duplication

import random               #This imports the random module for use to generate random letters later on

word_list = ['apple', 'kiwi', 'pineapple', 'strawberry', 'grapes']  #This is my source list of favourite fruits, printed in the following line
# print(word_list)

word = random.choice(word_list)  #This fucntion is what was imported from random at the start of this file, and generates a random word from the source list word_list
# print(word)

####New code ################

'''The code in green (below) is the inital code run- which was then tidied into 2 fucntions'''

# while True:
#     guess = input("Please enter a single letter ") 
#     if guess.isalpha() and len(guess) == 1:                 #Checks that input is both an alphabetic letter and is a single letter
#         # break
#         if guess in word:                                   #Checks that the letter the user is guessing in the word the comp has randomly picked from my word_list, then the while loop repeats
#             print(f"Good guess! {guess} is in the word.")
#         else:                                                   #And tells the user if the letter repeats
#             print(f"Sorry, {guess} is not in the word. Try again.")
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")

### Tidy up code ###############

def check_guess(guess):
    guess = guess.lower()
    if guess in word:                                   #Checks that the letter the user is guessing in the word the comp has randomly picked from my word_list, then the while loop repeats
        print(f"Good guess! {guess} is in the word.")
    else:                                                   #And tells the user if the letter repeats
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a single letter ") 
        if guess.isalpha() and len(guess) == 1:                 #Checks that input is both an alphabetic letter and is a single letter
            check_guess(guess)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# check_guess('a')
ask_for_input()