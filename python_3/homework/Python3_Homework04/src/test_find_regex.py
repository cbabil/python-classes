'''
Created on 06/06/2015

@author: cbabilotte
'''

import unittest
from find_regex import findregex

class Test(unittest.TestCase):
    
    def test_findregex(self):
        '''
        Test the start and end position of "Regular Expressions" in the text bellow
        '''
        words = 'Regular Expressions'
        text = 'In the 1950s, mathematician Stephen Cole Kleene described automata '
        text += 'theory and formal language theory in a set of models using a notation'
        text += ' called "regular sets" as a method to do pattern matching. Active usage'
        text += ' of this system, called Regular Expressions, started in the 1960s and '
        text += 'continued under such pioneers as David J. Farber, Ralph E. Griswold, '
        text += 'Ivan P. Polonsky, Ken Thompson, and Henry Spencer.'
        observed = findregex(text, words)
        
        self.assertEqual(observed, (231, 250), "Expected position are (231, 250), Observed position are %s" % str(observed))

if __name__ == "__main__":
    unittest.main()