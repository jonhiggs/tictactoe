import pdb
from mask import Mask

class Player(object):

    def __init__(self, token):
        self._token = token
        self._moves = 0

    @property
    def token(self):
        return self._token

    @property
    def moves(self):
        return Mask(self._moves)

    def move_to(self, position, board_mask):
        if self.position_vacant(position, board_mask):
            self._moves ^= (( Mask(position, "dec").to_int ))
        else:
            return False


    def position_vacant(self, position, board_mask):
        return not bool(self.position_state(position, board_mask))


    def position_state(self, position, board_mask):
        # free: return 0
        # mine: return 1
        # used: return 2

        position -= 1
        m = 2 ** position
        # FIXME: no boardmask...
        mask = Mask(m)

        if ( self.moves.to_int >> position ) % 2 != 0:
            return 1
        elif ( mask.to_int >> position ) % 2 != 0:
            return 3
        else:
            return 0

