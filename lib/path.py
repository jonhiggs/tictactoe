import pdb
from mask import Mask

class Path(object):
    def __init__(self, path, player):
        masks = {
                "0:2": "0b111000000",
                "3:5": "0b000111000",
                "6:8": "0b000000111",
                "0:6": "0b100100100",
                "1:7": "0b010010010",
                "2:8": "0b001001001",
                "0:8": "0b100010001",
                "3:6": "0b001010100",
                }

        self.mask = Mask(masks[path], 'bin')
        self._player = player


    def weight(self):
        weight = 0

        if self.blocked:
            weight += 100

        if self.moves_to_win == 1:
            weight += 0
        elif self.moves_to_win == 2:
            weight += 10
        else:
            weight += 20

        return weight

    @property
    def moves_to_win(self):
        return 3

    @property
    def blocked(self):
        for opponent in self._player.opponents:
            if (opponent.moves.to_int & self.mask.to_int) != 0:
                return True
        return False

    #def winning_positions(self):
