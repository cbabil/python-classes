#!/usr/local/bin/python3
#
#   guess.py
#
"""
Write a program that uses a while loop to ask the user to guess a number. Each guess should be checked 
against a number stored in the "secret" variable, to which a value between 1 and 20 should be assigned 
at the start. Otherwise it should report whether the guess was higher or lower than the secret. 
If the user guesses correctly, the loop should terminate. The loop should also keep a count of the user's guesses, 
and should terminate if the user makes five incorrect guesses. After the loop is over, the program should 
print the secret if the user didn't guess it, or a congratulatory message if the user guessed correctly.
"""
import random
secret = random.randint(1, 20)
numguess = 0
 
while numguess < 5: 
    guess = int(input("Guess a number: "))
    numguess +=1
    if guess > secret:
        print ("Guess lower")
    elif guess < secret:
        print ("Guess higher")
    elif guess == secret:
        break

if guess == secret:
    print("Correct! well done, the number was",secret)
else:
    print("Sorry, the number was", secret)