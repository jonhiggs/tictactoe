#!/usr/bin/env python

import sys
import os
sys.path.append(
    os.path.realpath( os.path.dirname(__file__) + '/../lib/')
)

import random
import unittest
import board
import path
import pdb
import player

class TestPath(unittest.TestCase):

    def setUp(self):
        self._board = board.Board()

        self._player = player.Player()
        self._player.token = "X"
        self._board.add_player(self._player)

        self._opponent = player.Player()
        self._opponent.token = "O"
        self._board.add_player(self._opponent)

    def test_mask(self):
        self.assertEqual(self._player.paths["0:2"].mask.mask, "007")

    def test_board(self):
        self.assertIn(self._player, self._board._players)
        self.assertIn(self._opponent, self._board._players)

    def test_player(self):
        self.assertEqual(self._player, self._player.paths["0:2"]._player)

    def test_blocked(self):
        self.assertFalse(self._player.paths["0:2"].blocked)
        self._opponent.move_to(0)
        self.assertTrue(self._player.paths["0:2"].blocked)

    def test_moves_to_win(self):
        self.assertEqual(self._player.paths["0:2"].moves_to_win, 3)
        self._player.move_to(0)
        self.assertEqual(self._player.paths["0:2"].moves_to_win, 2)
        self._opponent.move_to(1)
        self.assertEqual(self._player.paths["0:2"].moves_to_win, None)

    def test_weight_unblocked(self):
        self.assertEqual(self._player.paths["0:2"].weight, 20)
        self._player.move_to(0)
        self.assertEqual(self._player.paths["0:2"].weight, 10)
        self._player.move_to(1)
        self.assertEqual(self._player.paths["0:2"].weight, 0)

    def test_weight_blocked(self):
        self._opponent.move_to(0)
        self.assertEqual(self._player.paths["0:2"].weight, 100)
        self._player.move_to(1)
        self.assertEqual(self._player.paths["0:2"].weight, 100)

if __name__ == '__main__':
    unittest.main()


