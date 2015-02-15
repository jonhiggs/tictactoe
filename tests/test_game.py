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
import pdb

class TestGameNoPlayers(unittest.TestCase):
    def setUp(self):
        self._game = game.Game([])

    def test_players(self):
        self.assertEquals(len(self._game.players), 0)

class TestGameTwoHumanPlayers(unittest.TestCase):
    def setUp(self):
        players = []
        for i in range(0,2):
            p = human.Human()
            p.token = i
            players.append(p)

        self._game = game.Game(players)

    def test_players(self):
        self.assertEquals(len(self._game.players), 2)

    def test_game_drawn(self):
        self.assertFalse(self._game.drawn)
        for p in [ 1, 3, 4, 8 ]:
            self._game.players[0].move_to(p)

        for p in [ 0, 2, 5, 6, 7 ]:
            self._game.players[1].move_to(p)

        self.assertTrue(self._game.drawn)

    def test_game_won(self):
        for p in range(0,3):
            self._game.players[0].move_to(p)
        self.assertTrue(self._game.won)

if __name__ == '__main__':
    unittest.main()

