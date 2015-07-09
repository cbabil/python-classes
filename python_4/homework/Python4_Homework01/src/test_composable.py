'''
test_composable.py performs simple tests of composable functions.

Created on June 30th 2015

'''
import unittest
from composable import Composable

def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]

def square(x):
    "Multiplies a number by itself."
    return x*x


class ComposableTestCase(unittest.TestCase):
    
    def test_higher_power(self):
        squarer = Composable(square)
        po4 = squarer ** 3
        for v, r in ((1, 1),
                     (2, squarer(squarer(squarer(2)))),
                     (3, squarer(squarer(squarer(3))))):
            self.assertEqual(po4(v), r)
    
    def test_inverse_odd(self):
        reverser = Composable(reverse)
        tran = reverser ** 5
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(reverse(s), tran(s))

    def test_inverse(self):
        reverser = Composable(reverse)
        nulltran = reverser ** 2 
        for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)
    
    def test_square(self):
        squarer = Composable(square)
        po4 = squarer ** 2
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)
            
    def test_exceptions(self):
        fc = Composable(square)
        with self.assertRaises(TypeError):
            fc = fc * 3
        with self.assertRaises(TypeError):
            fc = square * fc
        with self.assertRaises(TypeError):
            fc = fc ** 2.5
        with self.assertRaises(ValueError):
            fc = fc ** -1

if __name__ == "__main__":
    unittest.main()