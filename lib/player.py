from path import *

class Player(object):
    def __init__(self):
        self._board = None
        self._token = None

    @property
    def moves(self):
        moves = []
        for position in self._board.positions:
            if position.owner == self:
                moves.append(position)
        return moves

    @property
    def paths(self):
        return {
                "0:2": Path("0:2", self),
                "3:5": Path("3:5", self),
                "6:8": Path("6:8", self),
                "0:6": Path("0:6", self),
                "1:7": Path("1:7", self),
                "2:8": Path("2:8", self),
                "0:8": Path("0:8", self),
                "3:6": Path("3:6", self),
                }

    def move_to(self, position):
        if self._board.positions[position].owner == None:
            self._board.positions[position].owner = self
            return True
        else:
            return False

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def board(self):
        return self._board

    @property
    def won(self):
        for path in self.paths:
            if self.paths[path].moves_to_win == 0: return True
        return False

    @property
    def opponents(self):
        return [p for p in self._board._players if p != self]
