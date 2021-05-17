#!/usr/bin/env python3

from geo import validatePostCode
import unittest

class TestPostCode(unittest.TestCase):
    def test_PC_AA9A_9AA(self):
        data = "EC1A 1BB"
        self.assertTrue(validatePostCode(data))

    def test_PC_A9A_9AA(self):
        data = "W1A 0AX"
        self.assertTrue(validatePostCode(data))

    def test_PC_A9_9AA(self):
        data = "M1 1AE"
        self.assertTrue(validatePostCode(data))

    def test_PC_A99_9AA(self):
        data = "E20 3EL"  #Olympic Velodrome
        self.assertTrue(validatePostCode(data))

    def test_PC_AA9_9AA(self):
        data = "CR2 6XH"
        self.assertTrue(validatePostCode(data))

    def test_PC_AA99_9AA(self):
        data = "BH14 9HP"
        self.assertTrue(validatePostCode(data))

    def test_PC_lowercase_A9_9AA(self):
        data = "m1 1ae"
        self.assertTrue(validatePostCode(data))

    def test_PC_nospace_lowercase_A9_9AA(self):
        data = "m11ae"
        self.assertTrue(validatePostCode(data))

    def test_PC_ZeroLength(self):
        data = ""
        self.assertFalse(validatePostCode(data))

    def test_PC_AllNumbers(self):
        data = "90210"
        self.assertFalse(validatePostCode(data))

    def test_PC_AllCharacters(self):
        data = "QWERTY"
        self.assertFalse(validatePostCode(data))

unittest.main()
