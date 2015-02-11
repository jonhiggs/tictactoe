class Player(object):

    def __init__(self, token):
        self._token = token
        self._moves = 0

    @property
    def token(self):
        return self._token

    @property
    def moves(self):
        return self._moves

    def move(self, position, board_mask):
        if self.position_vacant(position, board_mask):
            print "taking position %s" % position
        else:
            print "postion %s is taken" % position
            return False


    def position_vacant(self, position, board_mask):
        return not bool(self.position_state(position, board_mask))


    def position_state(self, position, board_mask):
        # free: return 0
        # mine: return 1
        # used: return 2

        if ( self.mask2int(self._moves) << position ) % 2 != 0:
            return 1
        elif ( self.mask2int(board_mask) << position ) % 2 != 0:
            return 3
        else:
            return 0


    def mask2int(self, mask):
        # take a mask like 124 and convertes it into an integer for performing
        # bitwise operations.
        i = 0
        for value in list(str(mask)):
            i <<= 3
            i |= int(value)
        return i
