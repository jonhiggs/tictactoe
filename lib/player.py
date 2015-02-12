import pdb
from mask import Mask

class Player(object):

    def __init__(self):
        self._board = None
        self._moves = Mask('000')
        self._token = None

    @property
    def moves(self):
        return self._moves

    def move_to(self, position):
        if self.board == None:
            return False
        elif self.board.vacant(position):
            return self.moves.set_bit(position, 1)
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
