import pdb
from mask import Mask

class Board(object):
    def __init__(self,rows=3, columns=3):
        self._rows = rows
        self._columns = columns


    def display(self, players):
        # FIXME: construct board of correct dimensions.
        board = [
            [ None, None, None ],
            [ None, None, None ],
            [ None, None, None ],
        ]
        for player in players:
            moves = player.moves.to_list
            for i in range(0,len(moves)):
                if moves[i] == '0': continue
                column = i % self._columns
                row = i / self._rows
                board[row][column] = player.token

        print board

    def mask(self, players):
        # high bits are taken squares
        m = 0
        for player in players:
            m |= player.moves.to_int
        return Mask(m)
