#!/usr/local/bin/python3
#
#   input_counter.py
#
"""
1. Write a program that creates an empty set and dict.
2. Write a while loop that repeatedly creates a list of words from a line of input 
   from the user.
3. Loop through the list of words and add each one to the set. If the set increases
   in size (indicating this word has not been processed before), add the word to the
   dict as a key with the value being the new length of the set.
4. Using another loop, display the list of words in the dict along with their value,
   which represents the order in which they were discovered by the program.
5. If the user presses Enter without any text, print Finished and exit.
"""
import string

newset = set() # Create a New Set
wordslst = [] # Initialize the words list
wordsdict = {}    # Initialize the word dictionary
setlength = 0 # The length of the set


while True:
    uin = input("Enter text: ")
    
    # Break out of the loop if user presses Enter
    # without any text
    if not uin:
        break
        
    # Remove any punctuation
    for punc in string.punctuation:
        uin = uin.replace(punc,"")
    
    # Create a list of words from user input  
    wordslst = uin.strip().split()
    
    for word in wordslst:
        newset.add(word)
        if setlength < len(newset):
            wordsdict[word] = len(newset)
            setlength = len(newset)
        
    for key, value in wordsdict.items():
        print(key, value)  
 
 
    