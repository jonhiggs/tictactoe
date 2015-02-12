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

    @property
    def won(self):
        winning_positions = [
            "0b111000000",
            "0b000111000",
            "0b000000111",
            "0b100100100",
            "0b010010010",
            "0b001001001",
            "0b100010001",
            "0b001010100",
        ]
        for position in winning_positions:
            if self.moves.bits_set(Mask(position, 'bin')):
                return True
        return False

