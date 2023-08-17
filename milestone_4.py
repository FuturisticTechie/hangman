

#Milestone4

import random               #This imports the random module for use to generate random letters later on

word_list = ['apple', 'kiwi', 'pineapple', 'strawberry', 'grapes']  #This is my source list of favourite fruits, printed in the following line
# print(word_list)

word = random.choice(word_list)  #This fucntion is what was imported from random at the start of this file, and generates a random word from the source list word_list
# print(word)

list_of_guesses = []

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = ['_' for _ in range(len(word))]  #This loop comprehension takes a dash space every space- the range function generates a seq of numbers starting from 0 but not inc last value 
        self.num_letters = len(set(self.word))  #using the set fucntion helps you count the UNIQUE times a letter is present! 
        self.list_of_guesses = []   #list of the guesses that have already been tried. Set this to an empty list initially

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:                                   #Checks that the letter the user is guessing in the word the comp has randomly picked from my word_list, then the while loop repeats
            print(f"Good guess! {guess} is in the word.")
            for indx, char in enumerate(self.word):                 #indexes letters in comp chosen word
                if char == guess:                                   #checks if the character in the comp chosen word is the same as the letter guessed by user
                    self.word_guessed[indx] = guess                 #changes the index of the letter in the (word_guessed) attribute (which corresponds to the blank _) matches the guess made by the user
            self.num_letters -= 1                                   #reduces the number of guesses remaining for user by 1
            print(self.word_guessed)
            print(self.num_letters)                                  #instead of return 

        else:  
            self.num_lives -= 1                                                   
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter ") 
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)


the_game = Hangman(word_list)
# print(the_game.word_guessed)

# check_guess('a')
the_game.ask_for_input()
print(the_game.list_of_guesses)