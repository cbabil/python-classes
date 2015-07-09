'''

Created on 6/7/2015

@author: cbabilotte
'''
import re

def process_creditcard(cardnumber):
    ''' Substitute x for all but the last four digit of any credit card '''
    return re.sub("\d{4}-\d{4}-\d{4}", "XXXX-XXXX-XXXX", cardnumber)