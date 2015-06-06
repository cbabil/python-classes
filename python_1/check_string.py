#!/usr/local/bin/python3
#
# check_string.py
# 
"""Detect if a string is all in upper case and ends with a period. 
If either of these fails, an appropriate message is displayed."""

uin = input("Enter an upper-string ending with a period: ")
if not uin.isupper() and not uin.endswith("."):
    print("Input is not all upper case")
    print("Input does not end with a period")
elif not uin.isupper():
    print("Input is not all upper case.")
elif not uin.endswith("."):
    print("Input does not end with a period.")
else:
    print("Input meets both requirements.")