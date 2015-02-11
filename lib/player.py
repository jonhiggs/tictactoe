import pdb

class Player(object):

    def __init__(self, token):
        self._token = token
        self._moves = 0

    @property
    def token(self):
        return self._token
