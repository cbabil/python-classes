#!/usr/local/bin/python3
#
#   caser.py
#
"""
1. Create a new Python source file named caser.py.
2. Create these functions:
   capitalize accepts a string parameter and applies the capitalize() method.
   title accepts a string parameter and applies the title() method.
   upper accepts a string parameter and applies the upper() method.
   lower accepts a string parameter and applies the lower() method.
   exit ends the program.
3. Store these functions in a dict with the keys matching the function names.
4. Create a while loop that requests two inputs from the user: one of the above function names, and any string.
5. Use function dispatch to get the correct function based on the first input, and then apply that function to the second input.
"""
import sys

def capitalize(data):
    """ applies the capitalize() method """
    return data.capitalize()

def title(data):
    """ applies the title() method """
    return data.title()

def upper(data):
    """ applies the upper() method """
    return data.upper()

def lower(data):
    """ applies the lower() method """
    return data.lower()

def exit(data=None):
    """ ends the program """
    print("Goodbye for now!")
    sys.exit()



if __name__ == "__main__":
    switch = {
        'capitalize': capitalize,
        'title': title,
        'upper': upper,
        'lower': lower,
        'exit': exit
    }

    options = switch.keys()
    while True:

        uinf = input('Enter a function name ({0}): '.format(', '.join(options)))
        uins = input("Enter a string: ")
        option = switch.get(uinf, None)
        if option:
            print(option(uins))
        else:
            print("Please select a valid function name")
