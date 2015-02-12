#!/usr/bin/env python

import sys
import os
sys.path.append(
    os.path.realpath( os.path.dirname(__file__) + '/../lib/')
)

import pdb
import random
import unittest
import mask

class TestMaskWithMask(unittest.TestCase):

    def setUp(self):
        self._mask = mask.Mask('754')

    def test_mask(self):
        self.assertEqual(self._mask.mask, '754')

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

    def test_set_bit(self):
        self.assertEqual(self._mask.bit(0), 0)
        self.assertFalse(self._mask.set_bit(0,0))
        self.assertEqual(self._mask.bit(0), 0)
        self.assertTrue(self._mask.set_bit(0,1))
        self.assertEqual(self._mask.bit(0), 1)

    def test_convert_from_bin(self):
        self.assertEqual(self._mask.convert_from_bin('0b111111111'), '777')
        self.assertEqual(self._mask.convert_from_bin('0b111101001'), '751')

    def test_not_bits(self):
        self._mask.not_bits
        self.assertEqual(self._mask.mask, "023")

    def test_convert_from_int(self):
        self.assertEqual(self._mask.convert_from_int(511), '777')

    def test_bits_set(self):
        """ if bits set in 'bits' are also set in 'self', return true """
        self.assertTrue(self._mask.bits_set(mask.Mask("700")))
        self.assertTrue(self._mask.bits_set(mask.Mask("500")))
        self.assertTrue(self._mask.bits_set(mask.Mask("750")))
        self.assertFalse(self._mask.bits_set(mask.Mask("755")))

if __name__ == '__main__':
    unittest.main()
