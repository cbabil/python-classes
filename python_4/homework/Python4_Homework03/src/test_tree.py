'''
Test tree.py.

Created on July 01 2015
'''

import unittest
from tree import Tree


class TestTree(unittest.TestCase):

    def test_insert(self):
        t = Tree("t", "T")
        t.insert('u', "U")
        observed = list(t.walk())
        expected = ['t', 'u']
        self.assertEqual(observed, expected)

    def test_walk(self):
        t = Tree("t", "T")
        observed = list(t.walk())
        expected = ['t']
        self.assertEqual(observed, expected)

    def test_find(self):
        t = Tree('t', "T")
        observed = t.find('t')
        expected = 'T'
        self.assertEqual(observed, expected)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            t = Tree("t", "T")
            t.insert('t', "T")

        with self.assertRaises(KeyError):
            t = Tree('t', "T")
            t.find('z')        

if __name__ == '__main__':
    unittest.main()