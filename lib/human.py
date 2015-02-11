from player import *

class Human(Player):

    def __init__(self, token):
        self._token = token
        self._moves = 0
        super(Player, self).__init__()

