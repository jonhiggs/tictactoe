from operator import itemgetter
from random import randint
from player import *

class AI(Player):
    def __init__(self):
        self._board = None
        self._moves = Mask('000')
        self._token = None

    def move(self):
        position = randint(0,8)
        self.move_to(position, board_mask)

    @property
    def ideal_path(self):
        weights = {}
        for path in self.paths:
            weights[path] = self.paths[path].weight

        weights = sorted(weights.items(), key=itemgetter(1))
        return weights[0][0]

    @property
    def ideal_position(self):
        # get options from path
        # test which option is part of the most winning paths
        return None
