import unittest
from groffle import groffle_slow, groffle_fast, groffle_faster

class TestGroffle(unittest.TestCase):
    
    def setUp(self):
        self.mass = 2.5
        self.density = 12.0
        self.total = 33.28958002253529

    def test_groffle_slow(self):
        observed = groffle_slow(self.mass, self.density)
        self.assertEqual(self.total, observed)

    def test_groffle_fast(self):
        observed = groffle_fast(self.mass, self.density)
        self.assertEqual(self.total, observed)

    def test_groffle_faster(self):
        observed = groffle_faster(self.mass, self.density)
        self.assertEqual(self.total, observed)

if __name__ == "__main__":
    unittest.main()