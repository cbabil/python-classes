#!/usr/local/bin/python3
#
#   word_list.py
#
"""
1. Make the program read a string from the user and create a list of words from the input.
2. Create two lists, one containing the words that contain at least one upper-case letter and one of the words that don't contain any upper-case letters.
3. Use a single for loop to print out the words with upper-case letters in them, followed by the words with no upper-case letters in them, one word per line.
"""
uin = input("Input your text: ")
upperList = []  # List containing words with at least one upper-case letter
lowerList = []  # List that does not contain any upper-case letters

words = uin.strip().split()

for word in words:
   if word.islower():
       lowerList.append(word)
   else:
       upperList.append(word)

for word in (upperList + lowerList):
    print(word) 
    