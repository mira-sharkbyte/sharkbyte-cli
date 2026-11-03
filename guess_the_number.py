#!/usr/bin/env python3
"""A simple CLI number guessing game."""

import random
import sys

def play():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            guess_str = input("Your guess: ")
            if guess_str.lower() == 'quit':
                print(f"The number was {secret_number}. Goodbye!")
                sys.exit(0)
                
            guess = int(guess_str)
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! You got it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play()
