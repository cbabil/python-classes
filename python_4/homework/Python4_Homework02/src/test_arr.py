'''
Test 3D-array implementations using tuple subscripting.

Created on July 01 2015
'''

import unittest
import arr


class TestArray(unittest.TestCase):

    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], 0)

    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], i == j and j == k)

    def _index(self, a, x, y, z):
        return a[x, y, z]

    def test_key_validity(self):
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 4)
        self.assertRaises(KeyError, self._index, a, 10, 1, 10)
        self.assertRaises(KeyError, self._index, a, 1, -1, 4)
        self.assertRaises(KeyError, self._index, a, 1, 10, 10)


if __name__ == '__main__':
    unittest.main()