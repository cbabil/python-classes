#!/usr/local/bin/python3
#
#   three_param.py
#
"""
1. Write a program that has a function named my_func with three parameters, 'a', 
  'b', and 'c'. The first parameter is required, and the second two parameters
   have the default values of 'b was not entered' and 'c was not entered'. 
   The function must print the value of each parameter.
2. In your program, call my_func three times. The first time, just provide a 
   value for the first parameter. The second time, provide values for the 
   first and second parameters. The third time, provide values for all three 
   parameters.
3. In your program, print the function itself.
"""
def my_func(a,b="b was not entered",c="c was not entered"):
    """ Print value of each parameter
        Return nothing
    """
    print(a)
    print(b)
    print(c)

my_func("test_a")
my_func("test_a","test_b")
my_func("test_a","test_b","test_c")
print(my_func)
