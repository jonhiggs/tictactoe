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
import game
import player
import pdb

class TestPosition(unittest.TestCase):
    def setUp(self):
        self._board = board.Board()

        self._player = player.Player()
        self._player.token = "X"
        self._board.add_player(self._player)

        self._opponent = player.Player()
        self._opponent.token = "O"
        self._board.add_player(self._opponent)

    def test_vacant(self):
        path = self._player.paths["0:2"]
        position = path.position(0)



if __name__ == '__main__':
    unittest.main()


