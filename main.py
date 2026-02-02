# init
print(f"Welcome to this game of Hangman!")

#wordlist is from https://github.com/dwyl/english-words/blob/master/words_dictionary.json
# select randomly a word from word list
# add as many empty spaces as letters in the selected word
#wait for user input
print(f"Enter a letter:")
input1 = input()
# make it not case sensitive input1 = 

print(f"You entered this letter: " + input1)
# after user input either 1) remove a heart 2) uncover ALL the spaces with the correctly guessed letter
# 8 wrong guesses
