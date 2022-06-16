# Program to play a guessing game.

import random

Number = random.randint(1, 101)

print("Mo's Guessing Game")
print("Think of a number between 1 and 100 ...")
print()
GuessCtr = 0
while True:
    Guess = int(input("Enter your guess: "))
    GuessCtr += 1
    if Guess == Number:
        print()
        print("You are correct.  The number was " + str(Number) + ".")
        break
    elif Guess < Number:
        print()
        print("The number is higher than your current guess.")
    else:
        print()
        print("The number is lower than your current guess.")

print("You had " + str(GuessCtr) + " guesses.")
print()
print("Thanks for playing our little game.")
print()

Anykey = input("Press any key to continue.")