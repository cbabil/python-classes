'''

Created on 6/13/2015

@author: cbabilotte
'''

import unittest
from ccn_safety2 import process_creditcard

class Test(unittest.TestCase):
      
    def test_process_creditcard(self):
        '''
        Test to assure that the credit card number is being substituted by the right message
        '''
        text = 'Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts.'
        observed = process_creditcard(text)
        
        expected = 'Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts.'
    
        self.assertEqual(observed,expected, "The converted text is not expected")
        self.assertTrue(('CCN REMOVED FOR YOUR SAFETY' in observed),"Credit card numbers are not being substituted")
        
    def test_process_phonenumber(self):
        '''
        Test to assure that all digits in a phone number are not substituted
        '''
        text = 'Have you ever noticed, in television and movies, that phone numbers and credit cards '
        text += 'are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number '
        text += 'that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and '
        text += 'security experts.'
        observed = process_creditcard(text)
        self.assertTrue('555-123-4567' in observed, "Phone number should not be substituted")
    
    def test_process_string(self):
        text = "This is a test with no number"

        observed = process_creditcard(text)
        expected = "This is a test with no number"
        self.assertEqual(observed,expected, "The converted text is not expected")   
        
if __name__ == "__main__":
    unittest.main()
        