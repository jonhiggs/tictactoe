class Board(object):
    def __init__(self,rows=3, columns=3):
        self._moves = {}

    def position_available(self, position):
        # integer will be odd if the least significate bit is set.
        position = self.positions_taken() << position
        return position % 2 == 0

    def print_board(self):
        return "this should be a board"

    def positions_taken(self):
        p = 0
        for key in self._moves: p |= self.str2bin(self._moves[key])
        return p

    def player_positions(self, token):
        return self._moves.get(token, default=000)
        #if token in self._moves.keys():
        #    return self._moves[token]
        #else:
        #    return 000

    def str2bin(self, value):
        values = list(str(value))
        binary = 0
        for value in values:
            binary <<= 3
            binary |= int(value)

        return binary

    def move(self, token, position):
        self._moves[token] = "770"
        self._moves['d'] =   "005"
        print "position available %s" % self.position_available(0)
        return self.positions_taken()


#    def make_move(self, move, letter):
#         self.board[move] = letter
#         return self.board
#
#
#    def is_empty(self, index):
#        return self.board[index] == ' '
#
#
#    def is_full(self):
#        #make this function shorter
#        return ' ' not in self.board
#            
#    # this function will be redundant - we can make a new board object to try move
#    def get_copy_board(self):
#        return copy.deepcopy(self)
#
#    def row(self, n):
#        offset = (n*3)
#        r = []
#        for position in range(0,3):
#            r.append(self.board[offset+position])
#        return r
#
#    def matrix(self):
#        m = []
#        for r in range(0,3):
#            m.append(self.row(r))
#        return m
#
#    def win(self, player):
#        return ((self.board[0] == self.board[1] == self.board[2] == player) or
#                (self.board[3] == self.board[4] == self.board[5] == player) or
#                (self.board[6] == self.board[7] == self.board[8] == player) or
#                (self.board[0] == self.board[3] == self.board[6] == player) or
#                (self.board[1] == self.board[4] == self.board[7] == player) or
#                (self.board[2] == self.board[5] == self.board[8] == player) or
#                (self.board[0] == self.board[4] == self.board[8] == player) or
#                (self.board[2] == self.board[4] == self.board[6] == player))
#
#    # put indexes in vars? row var/columnvar/diag var. Add corner var and side var
##    def row_win(self, player):
##        return ((self.board[0] == self.board[1] == self.board[2] == player) or
##                (self.board[3] == self.board[4] == self.board[5] == player) or
##                (self.board[6] == self.board[7] == self.board[8] == player))
##
##
##    def column_win(self, player):
##        return ((self.board[0] == self.board[3] == self.board[6] == player) or
##                (self.board[1] == self.board[4] == self.board[7] == player) or
##                (self.board[2] == self.board[5] == self.board[8] == player))
##
##
##    def diagonal_win(self, player):
##        return ((self.board[0] == self.board[4] == self.board[8] == player) or
##                (self.board[2] == self.board[4] == self.board[6] == player))
