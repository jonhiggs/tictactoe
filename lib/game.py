from random import randint, shuffle

from board import *
from human import *
from ai import *

class Game(object):
    def __init__(self, players):
        shuffle(players)
        self._board = Board()
        for player in players:
            self._board.add_player(player)

    def move(self, player):
        player.move(self._board)

    @property
    def players(self):
        return self._board._players

    @property
    def next_player(self):
        player = self._board._players.pop(0)
        self._board._players.append(player)
        return player

    @property
    def won(self):
        return False

    @property
    def board(self):
        print self._board.state


