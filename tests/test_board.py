#!/usr/bin/env python

import sys
import os
sys.path.append(
    os.path.realpath( os.path.dirname(__file__) + '/../lib/')
)

import random
import unittest
import board
import human

class TestBoard(unittest.TestCase):

    def setUp(self):
        players = [ human.Human("X") ]
        self._board = board.Board(players)

    def test_rows(self):
        self.assertEqual(self._board.rows, 3)

    def test_columns(self):
        self.assertEqual(self._board.columns, 3)

    def test_vacant(self):
        self.assertTrue(self._board.vacant(0))

    #def test_display(self):
    #    self.assertEqual(self._board.display, 3)

if __name__ == '__main__':
    unittest.main()

