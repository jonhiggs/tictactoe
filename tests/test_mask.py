#!/usr/bin/env python

import sys
import os
sys.path.append(
    os.path.realpath( os.path.dirname(__file__) + '/../lib/')
)

import random
import unittest
import mask

class TestMaskWithMask(unittest.TestCase):

    def setUp(self):
        self._mask = mask.Mask(754)

    def test_to_int(self):
        self.assertEqual(self._mask.to_int, 492)

    def test_to_bin(self):
        self.assertEqual(self._mask.to_bin, '0b111101100')

    def test_to_list(self):
        self.assertEqual(self._mask.to_list, list("111101100"))

    def test_bit(self):
        self.assertEqual(self._mask.bit(0), 0)
        self.assertEqual(self._mask.bit(1), 0)
        self.assertEqual(self._mask.bit(2), 1)
        self.assertEqual(self._mask.bit(3), 1)
        self.assertEqual(self._mask.bit(4), 0)
        self.assertEqual(self._mask.bit(5), 1)
        self.assertEqual(self._mask.bit(6), 1)
        self.assertEqual(self._mask.bit(7), 1)
        self.assertEqual(self._mask.bit(8), 1)

    def test_convert_from_bin(self):
        self.assertEqual(self._mask.convert_from_bin('0b111111111'), 777)
        self.assertEqual(self._mask.convert_from_bin('0b111101001'), 751)

    # FIXME
    #def test_convert_from_int(self):
    #    self.assertEqual(self._mask.convert_from_int(511), 777)
    #    self.assertEqual(self._mask.convert_from_int('511'), 777)

if __name__ == '__main__':
    unittest.main()
