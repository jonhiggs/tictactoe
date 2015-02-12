import pdb
from mask import Mask

class Player(object):

    def __init__(self, token):
        self._token = token
        self._moves = "000"

    @property
    def moves(self):
        return Mask(self._moves)

    @property
    def token(self):
        return self._token
