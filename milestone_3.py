import random

# List of my favourite fruits
word_list = ['apples', 'bananas', 'raspberries', 'strawberries', 'peaches']

# Random word is chosen from the list
word = random.choice(word_list)
print(word)
   

def check_guess(guess):
    
    guess = guess.lower() # convert letter to lowercase
    
    # checks if the letter is in the word
    if guess in word:
        print(f'Good guess {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.') 


def ask_for_input():
    while True:
        guess = input('Guess a letter: ')

    # if the input is in the alphabet as is a letter...
        if guess.isalpha() == True and len(guess) == 1:
            break #leave the loop
        else: 
            print('Invalid letter. Please, enter a single alphabetical character.')

    check_guess(guess)

ask_for_input()    