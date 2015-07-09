from sstr import sstr
import unittest


class TestSstr(unittest.TestCase):

    def test_sstr(self):
        s1 = sstr("abcde")
        self.assertTrue(s1 << 0 == 'abcde', "'abcde' is expected")
        self.assertTrue(s1 >> 0 == 'abcde', "'abcde' is expected")
        self.assertTrue(s1 << 2 == 'cdeab', "'cdeab' is expected")
        self.assertTrue(s1 >> 2 == 'deabc', "'cdeab' is expected")
        self.assertTrue(s1 >> 5 == 'abcde', "'abcde' is expected")
        self.assertTrue((s1 >> 5) << 5 == 'abcde', "'abcde' is expected")

if __name__ == '__main__':
    unittest.main()
