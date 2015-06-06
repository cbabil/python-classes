#!/usr/local/bin/python3
#
#   multuple.py
#
"""
1. Write a program that takes as data a tuple of two-element tuples, 
   such as ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98)). 
   This and/or similar data should be hard-coded (no need for user input).
2. Loop over the tuple and print out the results of multiplying the two 
   numbers together, and use string formatting to display nicely.
"""
tup = ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for (x,y) in tup:
    print("{0:>4d} = {1:>2d} x {2:>2d}".format((x*y), x, y))
