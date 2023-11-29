import random

# List of my favourite fruits
word_list = ['apples', 'bananas', 'raspberries', 'strawberries', 'peaches']

# Random word is chosen from the list
word = random.choice(word_list)

# Take user input to guess the random word
guess = input('Choose a single letter: ')

if len(guess) == 1:
    print('Good Guess!')
else: 
    print('Oops! That is not a valid input')