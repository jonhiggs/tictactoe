import pdb
from mask import Mask

class Player(object):

    def __init__(self, token):
        self._token = token
        self._moves = Mask('000')

    @property
    def moves(self):
        return self._moves

    def move_to(self, position):
        return self.moves.set_bit(position, 1)

    @property
    def token(self):
        return self._token
