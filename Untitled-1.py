


# word = "example"
# guesses = ['_' for _ in range(len(word))]
# print(guesses)

word = 'bana'

def updated_guessed_word(word_guessed, letter):
        # letter = input("Please enter a letter ")
    for indx, char in enumerate(word):
        if char == letter:
            word_guessed[indx] == letter
    return print(word_guessed)

updated_guessed_word('apple', 'a')