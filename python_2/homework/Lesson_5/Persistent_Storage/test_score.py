import unittest
import score
import os
import glob

class TestScore(unittest.TestCase):
    
    def test_score(self):    
        self.assertEqual(5, score.high_score("Dempsey", 5))
        self.assertEqual(10, score.high_score("Altidor", 10))
        self.assertEqual(15, score.high_score("Beckerman", 15))
        self.assertEqual(20, score.high_score("Brooks", 20))
        
        self.assertEqual(20, score.high_score("Dempsey", 20))
        self.assertEqual(10, score.high_score("Altidor", 5))

    def tearDown(self):
        files = glob.glob('playerscore.shlf.*')
        for file in files:
            os.remove(file)
    
if __name__ == "__main__":
    unittest.main()