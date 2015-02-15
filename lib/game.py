from random import randint, shuffle
from re import match

from board import *

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
    def drawn(self):
        return not self.won and self.over

    @property
    def won(self):
        for player in self.players:
            if player.won: return True
        return False

    @property
    def over(self):
        for position in self._board.positions:
            if position.vacant: return False
        return True

    @property
    def board(self):
        return self._board
