from random import randint, shuffle

from ai import *
from human import *
from board import *

class Game(object):

    def __init__(self):
        players = 2
        rows = 3
        columns = 3

        self._players = []

        self._moves = []
        for player in range(0,players):
            human = raw_input('Player %s, Are you human? (y/n): ' % (player+1))
            if human in ['y']: self._players.append(Human())
            else: self._players[player] = AI()

        self._board = Board(players, rows, columns)
        shuffle(self._players)


    @property
    def next_player(self):
        # should pop and push
        if self._next_player == self._players:
            self._next_player = 0
        else:
            self._next_player += 1

        return self._next_player
