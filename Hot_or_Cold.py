'''
My first attempt at making a simple game using OOP concepts in
Python. 

Hot or Cold
How it works:
System will generate a number (from 1 - 100).
User will guess a number
System checks whether number equals to guessed number
if correct, game ends and display generated number and number of
guesses
if wrong, system will provide hints (Hot/Cold, warmer/cooler):
Hot - distance to generated number <= 10 (first guess only)
Cold - distance to generated number > 10 (first guess only)
warmer - distance to generated number is lower than previous attempt
cooler - distance to generated number is higher than previous attempt
process repeats until generated number equals to guessed number
'''

import random

playing = True

# Class
class system_number:
    def __init__(self,number = random.randint(1,100)):
        self.number = number
        
class user:
    def __init__(self):
        self.guess = 0
        self.prev_guess = 0
        self.no_of_guesses = 0
       
# Functions
def guess():
    while True:
        try:
            guess_input = int(input('\nTake a guess! Please enter a number: '))
            
        except ValueError:
            print('Please enter a number! No decimals!')
            continue
        
        else:
            if guess_input < 1:
                print('Number must be from 1 to 100!')
                continue
            elif guess_input > 100:
                print('Number must be from 1 to 100!')
                continue
            else:
                user.no_of_guesses += 1
                    
                if user.no_of_guesses > 1:
                    user.prev_guess = user.guess
                        
                user.guess = guess_input
                print('You have entered ',guess_input,' !')
                playing = False
                break


def first_guess(system_number,guess_input):
    if abs(system_number-guess_input) <= 10:
        print('You are hot! Nearly there!')
    else:
        print('You are cold!')
    playing = True

def subsequent_guess(system_number,guess_input,prev_guess):
    if abs(system_number-guess_input) <= 10:
        print('You are hot! Nearly there!')
        if abs(system_number-guess_input) > abs(system_number-prev_guess):
            print('You are further from the correct number than before!')
        elif abs(system_number-guess_input) < abs(system_number-prev_guess):
            print('You are closer to the correct number than before!')
        elif abs(system_number-guess_input) == abs(system_number-prev_guess):
            print('You are just as far from the correct number than before!')
    else:
        print('You are cold!')
        if abs(system_number-guess_input) > abs(system_number-prev_guess):
            print('You are further from the correct number than before!')
        elif abs(system_number-guess_input) < abs(system_number-prev_guess):
            print('You are closer to the correct number than before!')
        elif abs(system_number-guess_input) == abs(system_number-prev_guess):
            print('You are just as far from the correct number than before!')
    print("Your previous number was",prev_guess,".")
    playing = True
    
# Gameplay

while playing == True:
    print('Welcome to Hot or Cold!')
    system_number = system_number()
    print('A number has been generated!')
    user = user()
    print('User has been created!')
    while system_number.number != user.guess:
        guess()
        if user.guess == system_number.number:
            print("You've correctly guessed the number!")
            if user.no_of_guesses == 1:
                print('Wow! You got it right on your first try!')
            else:
                print("You've guessed ",user.no_of_guesses,"times before getting it right!")
            print('\nPlease restart the game to try again.')
            playing = False
        else:
            print('Incorrect guess!')
            if user.no_of_guesses == 1:
                first_guess(system_number.number,user.guess)
            else:
                subsequent_guess(system_number.number,user.guess,user.prev_guess)
