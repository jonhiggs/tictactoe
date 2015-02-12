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

    def test_state(self):
        state = "_________"
        self.assertEqual(self._board.state, state)

    def test_vacant(self):
        self.assertTrue(self._board.vacant(0))

    def test_display(self):
        b = "\n\n         |          |         \n-----------------------------\n         |          |         \n-----------------------------\n         |          |         \n"
        self.assertEquals(self._board.display, b)


class TestBoardWithMoves(unittest.TestCase):
    def setUp(self):
        self._board = board.Board()

        player1 = human.Human()
        player1.token = "X"
        self._board.add_player(player1)

        player2 = human.Human()
        player2.token = "O"
        self._board.add_player(player2)

        self._board._players[0].move_to(0)
        self._board._players[1].move_to(1)
        self._board._players[0].move_to(2)
        self._board._players[1].move_to(3)

    def test_state(self):
        state = "XOXO_____"
        self.assertEqual(self._board.state, state)

    def test_vacant(self):
        self.assertFalse(self._board.vacant(0))
        self.assertTrue(self._board.vacant(8))

    def test_display(self):
        b = "\n\n   X     |    O     |    X    \n-----------------------------\n   O     |          |         \n-----------------------------\n         |          |         \n"
        self.assertEquals(self._board.display, b)


# test adding a player with duplicate token

if __name__ == '__main__':
    unittest.main()

