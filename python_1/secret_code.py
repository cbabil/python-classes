#!/usr/local/bin/python3
#
#   secret_code.py
#
"""
1. Write a program to read a line of input from 
   the user, and encode it using the following cipher:

   Take each character of the string individually, 
   and make the corresponding character in the output 
   string be that whose ordinal value is 1 more than 
   the ordinal value of the input character. Once the 
   output string has been constructed in this way, the 
   output of the program should be the reverse of the 
   constructed output string.
"""
cipher = []
uin = input("Enter text: ")

for letter in reversed(uin):
    cipher.append(chr(ord(letter)+1))

print("".join(cipher))
