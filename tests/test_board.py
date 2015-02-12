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
import pdb

class TestBoard(unittest.TestCase):

    def setUp(self):
        self._board = board.Board()
        self._board.add_player(human.Human())

    def test_add_player(self):
        player = human.Human()
        self.assertFalse(self._board.add_player(player))
        self.assertIsNone(player.board)
        player.token = "X"
        self.assertTrue(self._board.add_player(player))
        self.assertIsNotNone(player.board)

    def test_rows(self):
        self.assertEqual(self._board.rows, 3)

    def test_columns(self):
        self.assertEqual(self._board.columns, 3)

    #def test_vacant(self):
    #    self.assertTrue(self._board.vacant(0))

    #def test_after_moved(self):
    #    #players[0].move(2)

    #def test_display(self):
    #    self.assertEqual(self._board.display, 3)

# test adding a player with duplicate token

if __name__ == '__main__':
    unittest.main()

