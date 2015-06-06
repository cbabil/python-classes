#!/usr/local/bin/python3
#
#   guessing_game.py
#
"""
1. Import the random module.
2. Use the help() function on the random module to determine how to generate a random number between 1 and 99 inclusive.
3. Generate a random number between 1 and 99 and store it in a variable.
4. Use a while loop to accept integers from the user (don't forget—you'll need to convert the input string).
5. Compare the user's guess with the saved random number.
6. If the user successfully guesses the target number, inform them and terminate the program.
7. Otherwise, inform the user whether their guess was higher or lower than the saved random number and loop around to allow them to guess again.
"""
import random

num = random.randint(1,99)

while True:
    uin = int(input("Guess a number: "))

    if uin < num:
        print("Too Low")
    elif uin > num:
        print("Too High")
    else:
        print("You guess it!")
        break 