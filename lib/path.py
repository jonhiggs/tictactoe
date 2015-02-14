import pdb
from mask import Mask
from position import Position

class Path(object):
    def __init__(self, path, player):
        positions = {
                "0:2": [ Position(0), Position(1), Position(2) ],
                "3:5": [ Position(3), Position(4), Position(5) ],
                "6:8": [ Position(6), Position(7), Position(8) ],
                "0:6": [ Position(0), Position(4), Position(6) ],
                "1:7": [ Position(1), Position(5), Position(7) ],
                "2:8": [ Position(2), Position(6), Position(8) ],
                "0:8": [ Position(0), Position(5), Position(8) ],
                "3:6": [ Position(3), Position(5), Position(6) ],
                }

        self._positions = positions[path]
        self._player = player

    @property
    def weight(self):
        weight = 0

        if self.moves_to_win == 1:
            weight += 0
        elif self.moves_to_win == 2:
            weight += 10
        elif self.moves_to_win == 3:
            weight += 20
        else:
            """ cannot be won """
            weight += 100

        return weight

    @property
    def moves_to_win(self):
        moves = 0
        for position in self._positions:
            if position.owner == self._player:
                continue
            elif position.owner == None:
                moves += 1
            else:
                return None
        return moves

    @property
    def blocked(self):
        return (self.moves_to_win == None)

    @property
    def positions(self):
        return self._positions


    #def winning_positions(self):
