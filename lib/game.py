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

    @property
    def move(self):
        self.player.move()

    @property
    def players(self):
        return self._board._players

    @property
    def player(self):
        return self.players[0]

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


