import json
import random

#add some try and catch for exceptions

# select randomly a word from word list
def choose_random_word():
    with open('words_dictionary.json', 'r') as fp:
        wordList = json.load(fp)
        longWords = [word for word in wordList.keys() if len(word) > 3] # when choosing a word, it should be >=4 letters long to filter out weird words in the word list
        if not longWords:
            return None

        word = random.choice(longWords)
        return word
    print(f"List of words imported successfully")

# add as many empty spaces as letters in the selected word
def start_game(): 
    print(f"Welcome to this game of Hangman!")

    livesRemaining = 8
    selectedWord = choose_random_word()
    letterCount = len(selectedWord)
    print(f"Number of letters in the word: {letterCount}")
    print("_ " * letterCount)

def validate_input(input):
    if len(input1) == 1:
        if input1.isalpha():
            validLetter = input1
            return validLetter
    else: 
        print(f"Please input a single letter of the alphabet")

def ask_input():
    return 

def main():
    start_game()


#wait for user input
print(f"Enter a letter:")
input1 = input()
validate_input(input1)
# input has to be validated: can only be 1 single letter. no numbers. no special character.
# input also has to be not case sensitive. a = A

# then there has to be some loop
#user has to get feedback whether the game accepted some letter or if a heart was removed

print(f"You entered this letter: " + input1)
# after user input either 1) remove a heart 2) uncover ALL the spaces with the correctly guessed letter