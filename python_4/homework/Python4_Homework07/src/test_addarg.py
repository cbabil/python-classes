'''
Created on July 02 2015
'''

import unittest
from addarg import addarg

@addarg(1)
def prargs(*args):
    return args

@addarg(1)
def prkwargs(*args, **kw):
    return args, kw

class TestAddArg(unittest.TestCase):
    def test_addarg(self):
        self.assertEqual(prargs(2,3), (1, 2, 3))
        self.assertEqual(prargs("child"), (1, "child"))
        self.assertEqual(prkwargs(one=1, two=2), ((1,), {'one':1, "two":2}))
        self.assertEqual(prargs.__name__, 'prargs')
        
if __name__ == "__main__":
    unittest.main()