#!/usr/bin/env python3
"""Sharkbyte CLI - A tiny Swiss Army knife for the terminal."""

import argparse
import secrets
import string
import random
import sys

QUOTES = [
    "It works on my machine.",
    "Have you tried turning it off and on again?",
    "The best code is no code at all.",
    "There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.",
    "Debugging: Being the detective in a crime movie where you are also the murderer.",
    "I don't always test my code, but when I do, I do it in production."
]

def generate_password(length=16):
    """Generate a secure random password."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def flip_coin():
    return random.choice(["Heads", "Tails"])

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    parser = argparse.ArgumentParser(description="Sharkbyte CLI - A tiny Swiss Army knife.")
    parser.add_argument("-p", "--password", type=int, metavar="LENGTH", help="Generate a secure password of given length")
    parser.add_argument("-c", "--coin", action="store_true", help="Flip a coin")
    parser.add_argument("-d", "--dice", type=int, nargs="?", const=6, metavar="SIDES", help="Roll a dice (default: 6 sides)")
    parser.add_argument("-q", "--quote", action="store_true", help="Get a random developer quote")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.password:
        print(f"Password: {generate_password(args.password)}")
    if args.coin:
        print(f"Coin flip: {flip_coin()}")
    if args.dice:
        print(f"Dice roll (d{args.dice}): {roll_dice(args.dice)}")
    if args.quote:
        print(f"Quote: {random.choice(QUOTES)}")

if __name__ == "__main__":
    main()
