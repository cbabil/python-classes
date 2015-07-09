import unittest
from ctxmgr import context

class TestContextManager(unittest.TestCase):

    def test_raises_exception(self):
        ''' Test should raise TypeError exception '''
        with self.assertRaises(TypeError):
            with context():
                raise TypeError

    def test_supresses_valueerror(self):
        ''' Test shouldn't raise ValueError exception '''
        with context():
            raise ValueError

if __name__ == "__main__":
    unittest.main()