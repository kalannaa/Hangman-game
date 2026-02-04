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
    selectedWord = choose_random_word()
    letterCount = len(selectedWord)
    print(f"Number of letters in the word: {letterCount}")
    #print("_ " * letterCount)
    wordArray = list(selectedWord)
    emptyWord = ["_"] * len(selectedWord)
    print(" ".join(emptyWord))
    print(" ".join(wordArray))
    return selectedWord

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
    selectedWord = start_game()
    livesRemaining = 8

    while playing:
        print(f"Enter a letter:")
        user_input = input()
        input1 = user_input.lower()
        validate_input(input1)
        if input1 in selectedWord:
            print(f"Letter found!")

        else: #FIX NEEDED: life is removed even when the input is invalid (ie a number)
            livesRemaining = livesRemaining - 1
            print(f"Letter not found :( Remaining lives: {livesRemaining}")

    #FIX NEEDED: print array after each user input!! (now it just asks for a letter)
    playing = False

main()