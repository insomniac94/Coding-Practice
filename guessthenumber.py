# Simple python game to have a user enter their name and ask if they want to play a game, if 
# not the program will exit and if so the user will try and guess a number between 1-100.

import random

rNumber = random.randint(1,100)
attempts = 1

uName = input("Hello, what is your name? ")

print("Hello,", uName + "!",)

question = input("Would you like to play a game? [Y/N] ")

if question == 'N':
    print("oh okay... bye now..")

if question == 'Y':
    print("I'm thinking of a number between 1-100")

    guess = int(input("Have a guess: "))

    if guess > rNumber:
        print("Guess lower...")

    if guess < rNumber:
        print("Guess higher...")

    while guess != rNumber:
        attempts += 1
        guess = int(input("Try again: "))
        if guess < rNumber:
            print("Guess higher...")

        if guess > rNumber:
            print("Guess lower...")

        if guess == rNumber:
            print("You won", uName, "and it only took you", attempts, "attempts!!")