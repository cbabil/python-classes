""" Lesson 2 Unit Testing Project 1 """
import unittest


def title(s):
    "Capitalize the first character of a string"
    return s[0].upper() + s[1:]


class TestTitle(unittest.TestCase):

    def test_loop_words(self):

        word_arr = [
            "t",
            "test",
            "python is wonderful.",
            "hi, my name is Python"
        ]

        for s in word_arr:
            self.assertEqual(title(s), s.title(
            ), "These should be the same: \nbuilt-in: {}\ntitle(): {}".
                format(s.title(), title(s)))

if __name__ == "__main__":
    unittest.main()