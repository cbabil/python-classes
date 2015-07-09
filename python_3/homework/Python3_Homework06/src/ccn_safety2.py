'''

Created on 6/13/2015

@author: cbabilotte
'''
import re

def process_creditcard(text):
    ''' Substitute creadit card number with CCN REMOVED FOR YOUR SAFETY '''
    regex = re.compile(r"""
            \d{4}-   # first 4 digits of a credit card and a hyphen
            \d{4}-   # second 4 digits of a credit card and a hyphen
            \d{4}-   # third 4 digits of a credit card and a hyphen
            \d{4}    # last 4 digits of a credit card
            """, re.VERBOSE)
    return regex.sub("CCN REMOVED FOR YOUR SAFETY", text)