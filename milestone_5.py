import random

class Hangman:

    def __init__(self, word_list = [], num_lives = 5):
        
        #self.word_list = ['apples', 'bananas', 'raspberries', 'strawberries', 'peaches']
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word)) # no. of unique letters in the word
        self.list_of_guesses = []


    def check_guess(self, guess):
        users_guess = str(guess.lower()) # convert letter to lowercase
        
        # checks if the letter is in the word
        if users_guess in self.word:
            print(f'Good guess {users_guess} is in the word')

            # If the guess is correct, replace _ in word_guessed[] with the letter
            for letter in range(len(self.word)):
                    if users_guess == self.word[letter]:
                        self.word_guessed[letter] = users_guess
            self.num_letters -= 1
                    
        else:
            self.num_lives -= 1
            print(f'Sorry, {users_guess} is not in the word. Try again.') 
            print(f'You have {self.num_lives} lives left.')
            


    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            # if the input is in the alphabet as is a letter...
            if guess.isalpha() != True or len(guess) != 1: 
                print('Invalid letter. Please, enter a single alphabetical character.')
        
            # checks if the users input is already in the list of their guesses
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            
            else:
                # is the letter the user inputted in the word?
                self.check_guess(guess)
                # add the letter to the list of guesses
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
                break
                
                

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You Lost!')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        elif not game.num_letters > 0 and game.num_lives != 0:
            print('You Won The Game!!!')
            break

play_game(['Italy', 'Albania', 'Germany', 'Spain', 'France', 'Turkey', 'Norway', 'Amsterdam', 'Greece'])

