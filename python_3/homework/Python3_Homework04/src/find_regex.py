'''
Created on  06/06/2015

@author: cbabilotte
'''
import re

def findregex(text, words):
    '''
    Find the position of a search string in a given text
    return tuple containing start and end position
    '''
    m = re.search(words, text)
    return m.span()