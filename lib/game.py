from random import randint, shuffle
from re import match

from board import Board

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
    def drawn(self):
        if self.won:
            return False
        elif match(".*_.*", self._board.state):
            return False
        else:
            return True

    @property
    def won(self):
        for player in self.players:
            if player.won: return False
        return False

    @property
    def over(self):
        return self.drawn or self.won

    @property
    def board(self):
        print self._board.display


