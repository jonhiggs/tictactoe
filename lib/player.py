import pdb

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

    def move_to(self, position, board_mask):
        if self.position_vacant(position, board_mask):
            self._moves ^= (( self.mask2int(position) ))
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
        mask = self.int2mask(m)

        if ( self.mask2int(self._moves) >> position ) % 2 != 0:
            return 1
        elif ( self.mask2int(board_mask) >> position ) % 2 != 0:
            return 3
        else:
            return 0


    def mask2int(self, mask):
        # take a mask like 777 and convert it into an integer for performing
        # bitwise operations.
        i = 0
        for value in list(str(mask)):
            i <<= 3
            i |= int(value)
        return i

    def mask2bin(self, mask):
        # take 777 and convert it into '0b111111111'
        return format(self.mask2int(mask), '#011b')

    def bin2mask(self, bin):
        # take '0b111111111' and convert into 777

        bin = list(bin)[2:]     # drop off the 0b from the start
        mask = ''
        #pdb.set_trace()
        while len(bin) != 0:
            bits = "".join(bin[-3:])
            mask += str(int(bits, 2))
            bin = bin[:-3]
        return int(mask)

    def int2mask(self, i):
        # take an integer and turn it into a mask.
        # eg 511 == 777

        a = list(format(i, '#011b'))
        a.pop(0)
        a.pop(0)
        "".join(a)

        mask = "0b"
        for row in range(0, 3):
            v = str(a.pop(0) + a.pop(0) + a.pop(0))
            mask += v

        return mask


