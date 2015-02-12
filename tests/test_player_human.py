#!/usr/bin/env python

import sys
import os
sys.path.append(
    os.path.realpath( os.path.dirname(__file__) + '/../lib/')
)

import pdb
import random
import unittest
import board
import human

class TestPlayerHuman(unittest.TestCase):

    def setUp(self):
        self._player = human.Human()
        self._player.token = "X"

    def test_token(self):
        self.assertEqual(self._player.token, "X")

    def test_moves(self):
        moves = self._player.moves
        self.assertEqual(str(type(moves)), "<class 'mask.Mask'>")
        self.assertEqual(moves.mask, '000')

    def test_move_to(self):
        self.assertEqual(self._player.moves.bit(0), 0)
        self.assertTrue(self._player.move_to(0))
        self.assertEqual(self._player.moves.bit(0), 1)
        self.assertFalse(self._player.move_to(0))
        self.assertEqual(self._player.moves.bit(0), 1)

class TestPlayerMoveClash(unittest.TestCase):
    def setUp(self):
        self._player = human.Human("X")


    #def test_display(self):
    #    self.assertEqual(self._board.display, 3)

if __name__ == '__main__':
    unittest.main()


