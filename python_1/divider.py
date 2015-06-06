#!/usr/local/bin/python3
#
#   divider.py
#
"""
1. Create a while loop, request an integer value from the user, and bind the value as an integer to a variable.
2. Then divide the value of 10 by your new integer and print the results.
3. Use a try statement followed by a series of except statements to catch ValueError and ZeroDivisionError. When those errors are caught, print response statements to the user informing them of their mistake.
"""print("Dividing 10 by an interger")
while True:
    
    uinint = input("Provide an integer: ")

    # Break out of the loop if user
    # enter a blank 
    if not uinint:
        break

    try:
        print(10/int(uinint))
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")




