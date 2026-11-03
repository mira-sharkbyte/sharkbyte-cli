#!/usr/bin/env python3
"""A simple CLI number guessing game with argparse."""

import random
import sys
import argparse

def play(max_num):
    secret_number = random.randint(1, max_num)
    attempts = 0
    print(f"Welcome to Guess the Number! (1-{max_num})")
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
    parser = argparse.ArgumentParser(description="Guess the Number game.")
    parser.add_argument("-m", "--max", type=int, default=100, help="Maximum number (default: 100)")
    args = parser.parse_args()
    play(args.max)
