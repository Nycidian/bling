__author__ = 'Nycidian'

import unittest

from bling import Ring
from bling import Chain
from bling import Gem


class TestGem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_1 = 0, 'd', (1, 2)
        cls.test_2 = 1, 'a', (2, 3)
        cls.class_1 = Gem(*cls.test_1)
        cls.class_2 = Gem(*cls.test_2)
        cls.class_3 = Gem(*cls.test_1)
        cls.class_4 = Ring(*cls.test_1)

    def test_equals(self):
        self.assertTrue(self.class_1 != self.test_1)
        self.assertTrue(self.class_1 == self.class_3)
        self.assertFalse(self.class_1 == self.class_4)
        self.assertFalse(self.class_1 == self.class_2)

    def test_bool(self):
        self.assertTrue(self.class_1)



class TestChain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_1 = 0, 'd', (1, 2)
        cls.test_2 = 1, 'a', (2, 3)
        cls.class_1 = Chain(*cls.test_1)
        cls.class_2 = Chain(*cls.test_2)
        cls.class_3 = Chain(*cls.test_1)
        cls.class_4 = Ring(*cls.test_1)



    def test_equals(self):
        self.assertTrue(self.class_1 != self.test_1)
        self.assertTrue(self.class_1 == self.class_3)
        self.assertFalse(self.class_1 == self.class_4)
        self.assertFalse(self.class_1 == self.class_2)

    def test_bool(self):
        self.assertTrue(self.class_1)


class TestRing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_1 = 0, 'd', (1, 2)
        cls.test_2 = 'd', (1, 2), 0
        cls.class_1 = Ring(*cls.test_1)
        cls.class_2 = Ring(*cls.test_2)

    def test_hash(self):
        """
        Ring\'s made of different tuples of congruence should have the same hash
        """
        self.assertEqual(hash(self.class_1), hash(self.class_2))

    def test_equals(self):
        """
        Ring's made of different tuples of congruence should be equal
        A Ring should not ever equal a tuple even if congruent
        """
        self.assertEqual(self.class_1, self.class_2)
        self.assertTrue(self.class_1 == self.class_2)
        self.assertFalse(self.class_1 == self.test_1)
