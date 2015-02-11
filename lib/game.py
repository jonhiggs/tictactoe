from random import randint, shuffle

from board import *
from human import *
from ai import *

class Game(object):
    def __init__(self, board):
        self._board = board
        self._players = []
        self._tokens = [ 'O', 'X', '1', '3' ]
        #self._board = Board(players, rows, columns)

    def add_player(self, style="human"):
        if style == "human":
            player = Human
        else:
            player = AI

        player.token = self._tokens.pop()
        shuffle(self._players)
        self._players.append(player)

    def move(self, position):
        token = self.next_player.token
        print "vacant %s" % True
        print "moving %s" % token
        return self._board.move(token,position)

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
        return self._board.print_board()
