#!/usr/local/bin/python3
#####################################################
#    Syntax Analysis and Graphic Reporting Tool     #
#                     ----------                    #
#      yet another awesome Python application       #
#                 by: Christophe Babilotte          #
#                                                   #
#        OST Python 1, Lesson 16, Project 3         #
#                 February 6th 2015                 #
#####################################################

import sys
import string


def histogram(lenghts):
    """Draw an ascii history base on a dictionary
       return nothing
    """
    xmax = max(lenghts.keys()) + 2
    ymax = max(lenghts.values()) + 2
    symbol = ''
    indexing = ''

    # Choose the step based on the ymax
    # If the ymax is less than 100 then
    # we increment the y axis by 2 units at a time
    # If the ymax is more than 100 then
    # we increment the y axis by 10 units at a time
    if ymax < 100:
        step = 2
    else:
        step = 10

    for j in range(ymax, 0, -step):
        if j % 10 < step:
            symbol = "{0:>3}{1:>3}".format(j, "-|")
        else:
            symbol = "{0:>3}{1:>3}".format(" ", "|")

        # Fill histogram
        for i in range(1, xmax + 1):
            if i in lenghts.keys() and lenghts[i] >= j:
                symbol += '  *'
            else:
                symbol += '   '
        print(symbol)

    # x-axis
    symbol = "{0:>8}".format("0 -+--")
    for i in range(1, xmax + 1):
        symbol += "+--"
    print(symbol)

    # Indexing x-axis
    indexing = '     |'
    for i in range(1, xmax + 1):
        indexing += '{0:>3}'.format(i)
    print(indexing)


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

    print(" ")
    histogram(freq)

except IOError:
    print("No such file or directory: %s" % sys.argv[1])
except IndexError:
    print("Enter a valid filename")
