#!/usr/bin/env python
import sys
import os
sys.path.append(
    os.path.realpath( os.path.dirname(__file__) + '/../lib/')
)

import random
import unittest
import board
import ai

class TestPlayerAI(unittest.TestCase):
    def setUp(self):
        self._board = board.Board()

        self._player = ai.AI()
        self._player.token = "X"
        self._player._board = self._board

        self._opponent = ai.AI()
        self._opponent.token = "O"
        self._opponent._board = self._board

    def test_ideal_path(self):
        self._opponent.move_to(0)
        self.assertTrue(self._player.ideal_path)


if __name__ == '__main__':
    unittest.main()

