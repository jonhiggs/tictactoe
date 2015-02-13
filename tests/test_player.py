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
import player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self._player = player.Player()
        self._player.token = "X"
        self._board = board.Board()
        self._board.add_player(self._player)

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

    def test_won(self):
        self.assertFalse(self._player.won)
        self._player.move_to(0)
        self.assertFalse(self._player.won)
        self._player.move_to(1)
        self._player.move_to(2)
        self.assertTrue(self._player.won)
        self._player.move_to(3)
        self.assertTrue(self._player.won)

    def test_board(self):
        self.assertIsNotNone(self._board)
        self.assertEqual(self._board, self._player._board)
        self.assertIn(self._player, self._board._players)

class TestPlayers(unittest.TestCase):
    def setUp(self):
        self._board = board.Board()

        self._player1 = player.Player()
        self._player1.token = "X"
        self._board.add_player(self._player1)

        self._player2 = player.Player()
        self._player2.token = "O"
        self._board.add_player(self._player2)

    def test_move_to(self):
        self.assertTrue(self._player1.move_to(0))
        self.assertFalse(self._player2.move_to(0))

    def test_opponents(self):
        self.assertEqual(self._player1.opponents, [ self._player2 ])
        self.assertIn(self._player1, self._board._players)
        self.assertIn(self._player2, self._board._players)

    #def test_display(self):
    #    self.assertEqual(self._board.display, 3)


if __name__ == '__main__':
    unittest.main()


