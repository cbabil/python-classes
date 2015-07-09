import unittest
from dictsubclass import DictDefault

class Test(unittest.TestCase):
    
    def test_DictDefault(self):
        default_dict = DictDefault('My_Dictionary')
        default_dict['key1'] = 'value1'
        default_dict['key2'] = 'value2'
        self.assertTrue(default_dict['key1'], 'value1')
        self.assertTrue(default_dict['key_2'], 'value2')

    def test_exceptions(self):
        default_dict = DictDefault('My_Dictionary')
        observed = 'My_Dictionary'
        expected = default_dict['key1']
        self.assertEqual(observed, expected)    
if __name__ == "__main__":
    unittest.main()