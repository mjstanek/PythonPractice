#!/usr/bin/env python3

# This script runs a simple game of hangman in the terminal.
# It utilizes an API to herokuapp.com, so shoutout to them.
# It *has* gone down in testing, so I added a single default word.

import requests
import random
import sys
import os
# import json

# Global initialization of variables
word = ''
errors = 0
mistakes = []
scoreboard = []
gallows = []

# Difficulty function to determine the length of the word to guess
def difficulty():
    print('Welcome to Hangman! Please choose how long of a word you would like to guess.')
    print('Enter "1" for a short word.')
    print('Enter "2" for a medium length word.')
    print('Enter "3" for a long word.')
    print('Enter "4" for a completely random word.')
    print('Enter any other input to quit.')
    difficulty = input('Please enter a length: ')
    # Check input and set word length range
    if difficulty.isnumeric() and int(difficulty) <= 4:
        difficulty = int(difficulty)
        if difficulty == 1:
            randmin = 3
            randmax = 6
        elif difficulty == 2:
            randmin = 7
            randmax = 11
        elif difficulty == 3:
            randmin = 12
            randmax = 16
        else:
            randmin = 3
            randmax = 16
        get_word(randmin, randmax)
        return word
    else:
        print('Goodbye!')
        return False

#Function to call the API and get a word of determined length  
def get_word(randmin, randmax):
    global word
    length = random.randint(randmin, randmax)
    url = f'https://random-word-api.herokuapp.com/word?length={length}'
    response = requests.get(url)
    try:
        data = response.json()
        word = data[0].upper()
        # print(response.text)
    except:
        # Default word if API fails
        word = 'artiodactyls'.upper()
    return word

# Function to clear the terminal screen
def reset_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_gallows(gallows):
    reset_screen()
    global errors
    for row in gallows:
        if row == gallows[0] and mistakes:
            print(''.join(row), ' '*10, 'Wrong Guesses: ', ' '.join(mistakes))
        else:
            print(''.join(row))
    if errors < 6:
        print('\n', ' '.join(scoreboard))
    elif errors >= 6:
        print('Oh no, you didn\'t guess the word!')
        result = ''.join(scoreboard)
        print(f'The word was {word}, and you had {result}')


# Function to check and see if the play has won
def victory_check(scoreboard):
    if '_' not in scoreboard:
        if errors == 1:
            print(f'Wow, you did it! You guessed the word with only {errors} mistake!')
        else:
            print(f'Wow, you did it! You guessed the word with only {errors} mistakes!')
        sys.exit()

# This function will check how many mistakes the player has made
# then it will add the corresponding parts to the gallows
# If the user has made less than 6 mistakes, it will keep going
def add_parts(errors, gallows):
    if errors == 1:
        gallows[2][6] = 'O'
    elif errors == 2:
        gallows[3][6] = '|'
    elif errors == 3:
        gallows[3][5] = '/'
    elif errors == 4:
        gallows[3][7] = '\\'
    elif errors == 5:
        gallows[4][5] = '/'
    elif errors == 6:
        gallows[4][7] = '\\'
    display_gallows(gallows)
    if errors < 6:
        input_guess()

# This function checks the the user's input against the word and previous guesses
# If the guess is correct, it updates the scoreboard
def guess_checker(guess):
    global scoreboard, errors, mistakes, gallows
    if guess in scoreboard or guess in mistakes:
        print(f'You have already guessed {guess}. Please try again.')
        # print(scoreboard)
        # print(mistakes)
        input_guess()
    elif guess not in word:
        errors += 1
        mistakes.append(guess)
        print(f'Sorry, {guess} is incorrect.')
        add_parts(errors, gallows)
    else:
        position = 0
        for letter in word:
            # print(scoreboard)
            if letter == guess:
                scoreboard[position] = guess
            position += 1
        display_gallows(gallows)
        victory_check(scoreboard)
        # print(' '.join(scoreboard))
        input_guess()

# Setting up Gameboard
def initialize_gallows():
    global gallows
    gallows = [['X' for i in range(8)] for j in range(6)]

    gallows[0] = [' ', '_', '_', '_', '_', '_', ' ', ' ', ' ']
    gallows[1] = ['|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ',]
    gallows[2] = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    gallows[3] = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    gallows[4] = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    gallows[5] = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    display_gallows(gallows)

# This function converts the random word into a scoreboard of underscores
def initialize_scoreboard(word):
    # print(word)
    global scoreboard
    scoreboard = ['_' for x in word]
    display = ' '.join(scoreboard)
    print(display)
    input_guess()

# This function ensures that the user has input a single letter
def guess_sanitizer(guess):
    if guess.isalpha() and len(guess) == 1:
        guess_checker(guess.upper())
    else:
        print('Please only enter a single letter.')
        input_guess()

# This function simply prompts and accepts the user's input
def input_guess():
    guess = input('Please enter a letter to guess: ')
    guess_sanitizer(guess)

# This function initializes the game and begins running it
def initialization():
    word = difficulty()
    if word != False:
        initialize_gallows()
        initialize_scoreboard(word)

if __name__ == '__main__':
    initialization()