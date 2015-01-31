__author__ = 'Nycidian'

import unittest
import math

from ring import Ring


def alpha():
    pass


class TestRingBase(unittest.TestCase):

    def setUp(self):
        pass

    def test_get(self):
        ring = Ring(0, 'hello', alpha)
        self.assertEqual(ring[1], 'hello')
        self.assertEqual(ring[0], 0)
        self.assertEqual(ring[2], alpha)
        self.assertEqual(ring[3], 0)

    def test_set(self):

        def func():
            a = 2

        this = 'hell no'
        ring = Ring(func, 0, 12345, 'about', this, 'hell no')
        ring2 = Ring(0, 12345, 'about', this, 'hell no', func)
        ring3 = Ring(12345, 0, 'about', this, 'hell no', func)

        s = set([ring, ring2, ring3])
        self.assertEqual(len(s), 2)


if __name__ == '__main__':
    unittest.main()