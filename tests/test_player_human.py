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

class TestPlayerHuman(unittest.TestCase):

    def setUp(self):
        self._player = human.Human("X")

    def test_moves(self):
        moves = self._player.moves
        self.assertEqual(str(type(moves)), "<class 'mask.Mask'>")
        self.assertEqual(moves.mask, 0)

class TestPlayerHumanMoved


    #def test_display(self):
    #    self.assertEqual(self._board.display, 3)

if __name__ == '__main__':
    unittest.main()


