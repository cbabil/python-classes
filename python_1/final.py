#!/usr/local/bin/python3
#
#   final.py
#
"""
1. Write a program that meets the following specifications:
2. Call the program with an argument, it should treat the argument as a
   filename, and process the content of the file.
3. The program reads all the input, splitting it up into words, and
   computes the length of each word. Punctuation marks should not be
   included as a part of the word, so "it's" should be counted as a
   three-character word, and "final." should be counted as a
   five-character word.
4. The example text includes a "word" of zero length (the "&"); your
   solution should handle this.
5. When all input has been processed, the program should print a table
   showing the word count for each of the word lengths encountered. Your
   mentor will run your code against several standardized inputs to verify
   the correctness of your logic.

"""
import sys
import string


def count_letters(text):
    """counts number of character in each word
       return integer
    """
    count = 0
    for char in text:
        count += 1

    return count


try:
    # Open file for reading
    fh = open(sys.argv[1], 'r')
    infile = fh.read()

    # Remove all punctuation
    for punc in string.punctuation:
        infile = infile.replace(punc, "")

    freq = {}
    for word in infile.strip().split():
        wordlen = count_letters(word)
        freq[wordlen] = freq.get(wordlen, 0) + 1

    print("Length Count")
    for wordlen in sorted(freq.keys()):
        print("{0:<3d} {1:<4d}".format(wordlen, freq[wordlen]))

except IOError:
    print("No such file or directory: %s" % sys.argv[1])