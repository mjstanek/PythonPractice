#!/usr/bin/env python3

# This script will generate a random number between 1 and 10
# The user will guess a number
# Using a while loop, the user will be given additional chances to guess

import random

def initiation():
    start = input('Would you like to play a guessing game? Press "Y" to start: ')
    if start.strip().upper() != 'Y':
        print("Maybe next time!")
        return
    else:
        print("Great! Let's play!")
        guessing_game()

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    previous_guess = None
    guess = None
    print("I have selected a number between 1 and 10. Try to guess it!")
    while True:
        previous_guess = guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue
            if guess == number_to_guess:
                if attempts == 1:
                    print(f"WOW! You guessed it on your first try! I was thinking of {number_to_guess}.")
                else:
                    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
                break
            elif attempts == 1:
                print(f"Sorry, {guess} is not the number I was thinking of. Try again!")
            else:
                if abs(guess - number_to_guess) == 1:
                    print(f"{guess} is very close! You're on fire!")
                elif previous_guess is not None:
                    if abs(previous_guess - number_to_guess) < abs(guess - number_to_guess):
                        print(f"{guess} is getting colder. Try again!")
                    elif abs(previous_guess - number_to_guess) > abs(guess - number_to_guess):
                        print(f"{guess} is getting warmer. Try again!")
                    else:
                        print(f"{guess} is the same temperature as your last guess. Try again!")
                else:
                    print(f"Try again!")
        except ValueError:
            print("That's not a valid number. Please enter a number between 1 and 10.")
          
    
if __name__ == "__main__":
    initiation()