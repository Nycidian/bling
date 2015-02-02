__author__ = 'Nycidian'

import unittest

from ring import Ring, Loop, Setting, Band


def alpha():
    pass


class TestLoop(unittest.TestCase):

    def test_get(self):
        loop = Loop(0, 'hello', alpha)
        self.assertEqual(loop[1], 'hello')
        self.assertEqual(loop[0], 0)
        self.assertEqual(loop[2], alpha)
        with self.assertRaises(IndexError):
            loop[3]

    def test_set(self):

        def func():
            a = 2

        this = 'hell no'
        loop = Loop(func, 0, 12345, 'about', this, 'hell no')
        loop2 = Loop(0, 12345, 'about', this, 'hell no', func)
        loop3 = Loop(12345, 0, 'about', this, 'hell no', func)
        loop4 = Loop(func, 0, 12345, 'about', this, 'hell no')

        s = set([loop, loop2, loop3, loop4])
        self.assertEqual(len(s), 3)

    def test_isinstance(self):

        def func():
            a = 2

        one = Loop(1, 3, 2)
        two = Loop('1', 3, func)
        three = Loop(2, (2, func))

        for O in [one, two, three]:
            for T in [Loop, Band]:
                self.assertTrue(isinstance(O, T))

        for O in [one, two, three]:
            for T in [int, str, list, tuple, dict, Ring]:
                self.assertFalse(isinstance(O, T))

    def test_equals(self):

        one = Loop(1, 3, 2)
        two = Loop(1, 3, 2)
        three = (1, 3, 2)
        four = Loop(2, 1, 3)

        for O in [one]:
            for T in [two]:
                self.assertTrue(O == T)

        for O in [one]:
            for F in [three, four]:
                self.assertFalse(O == F, '{} is equal to {}'.format(O, F))


    def test_in(self):
        loop_true = ['a', 'p']
        loop_false = ['p', 'a']

        loop_test = Loop('o', 'o', 'a', 'p', 'n')

        self.assertTrue(loop_true in loop_test)
        self.assertFalse(loop_false in loop_test)


class TestRing(unittest.TestCase):

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

    def test_isinstance(self):

        def func():
            a = 2

        one = Ring(1, 3, 2)
        two = Ring('1', 3, func)
        three = Ring(2, (2, func))

        for O in [one, two, three]:
            for T in [Ring, Band]:
                self.assertTrue(isinstance(O, T))

        for O in [one, two, three]:
            for T in [int, str, list, tuple, dict, Loop]:
                self.assertFalse(isinstance(O, T))

    def test_equals(self):

        one = Ring(1, 3, 2)
        two = Ring(1, 3, 2)
        three = (1, 3, 2)
        four = Ring(2, 1, 3)

        for O in [one]:
            for T in [four, two]:
                self.assertTrue(O == T, '{} is not equal to {}'.format(O, T))

        for O in [one]:
            for F in [three]:
                self.assertFalse(O == F, '{} is equal to {}'.format(O, T))


class TestContains(unittest.TestCase):

    def test_contains(self):

        def true_in(I, O):
            self.assertTrue(I in O, '{} is not in {}'.format(I, O))

        def false_in(I, O):
            self.assertFalse(I in O, '{} is in {}'.format(I, O))

        ap = 'a', 'p'
        pa = 'p', 'a'
        no = 'n', 'o'
        ring_test = Ring('o', 'o', 'a', 'p', 'n')
        loop_test = Loop('o', 'o', 'a', 'p', 'n')

        true_in(ap, ring_test)
        true_in(Loop(*ap), ring_test)
        true_in(Ring(*ap), ring_test)

        false_in(pa, ring_test)
        true_in(Ring(*pa), ring_test)
        false_in(Loop(*pa), ring_test)
        true_in(no, ring_test)

        true_in(ap, loop_test)
        false_in(pa, loop_test)
        true_in(Ring(*pa), loop_test)
        false_in(no, loop_test)


if __name__ == '__main__':

    unittest.main()