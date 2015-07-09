'''
Created on June 06, 2015

@author: cbabilotte
'''
import unittest
from adder import adder

class Test(unittest.TestCase):

    def test_adder_integer(self):
        ''' Test to ensure that integer data passes '''
        observed = adder(1,6)
        expected = 7
        self.assertEqual(observed, expected)
    
    def test_adder_float(self):
        ''' Test to ensure that float data fails '''
        self.assertRaises(TypeError, adder, 1.1, 6.1)
        
    def test_adder_string(self):
        ''' Test to ensure that string data fails '''
        self.assertRaises(TypeError, adder, "one", "two")
            
if __name__ == "__main__":
    unittest.main()