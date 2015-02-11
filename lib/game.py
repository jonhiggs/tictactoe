from random import randint, shuffle

from board import *
from human import *
from ai import *

class Game(object):
    def __init__(self, board, players):
        shuffle(players)
        self._board = board
        self._players = players

    def move(self, player, position):
        player.move(position, self._board.mask(self._players))

    @property
    def players(self):
        return len(self._players)

    @property
    def next_player(self):
        player = self._players.pop(0)
        self._players.append(player)
        return player

    @property
    def won(self):
        return False

    @property
    def board(self):
        return self._board.display(self._players)
