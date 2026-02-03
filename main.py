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
        word.lower()
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

def validate_input(input1):
    if len(input1) == 1:
        if input1.isalpha():
            return input1
        else: 
            print(f"Please input a single letter of the alphabet")
    else: 
        print(f"Please input a single letter of the alphabet")

def main():
    playing = True
    start_game()

    while playing:
        print(f"Enter a letter:")
        user_input = input()
        input1 = user_input.lower()
        validate_input(input1)

    playing = False

main()