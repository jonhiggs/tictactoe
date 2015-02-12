from random import randint, shuffle

from board import *
from human import *
from ai import *
from mask import *

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
        winning_positions = [
            "0b111000000",
            "0b000111000",
            "0b000000111",
            "0b100100100",
            "0b010010010",
            "0b001001001",
            "0b100010001",
            "0b001010100",
        ]
        for position in winning_positions:
            if self.player.moves.bits_set(Mask(position, 'bin')):
                return True
        return False

    @property
    def board(self):
        print self._board.state


