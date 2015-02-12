import pdb
from mask import Mask

class Board(object):
    def __init__(self, rows=3, columns=3):
        self._rows = rows
        self._columns = columns
        self._positions = rows * columns
        self._players = []
        self._board = [
            [ None, None, None ],
            [ None, None, None ],
            [ None, None, None ],
        ]


    @property
    def rows(self): return self._rows

    @property
    def columns(self): return self._columns

    def add_player(self, player):
        if player.token == None: return False
        for p in self._players:
            if p.token == player.token: return False

        if self._players.append(player):
            return False
        else:
            player._board = self
            return True

    def display(self):
        for player in self._players:
            for i in range(0, (self._positions-1) ):
                column = i % self._columns
                row = i / self._rows
                value = self._board[row][column]

                row_end = (i % self._columns) == (self._columns-1)

                if value == None: value = ""
                print str(value).center(8),
                if not row_end:
                    print "|",
                else:
                    print "\n",
                    print "-" * 8 * (self._columns+1)

    @property
    def state(self):
        state = list("_________")
        for player in self._players:
            for position in range(0,9):
                if player.moves.bit(position) == 1:
                    state[position] = player.token

        return "".join(state)


    def vacant(self, position):
        moves = 0
        for player in self._players:
            moves |= player.moves.to_int
        moves = Mask(moves, 'int')
        return moves.notted

    def move_to(self, position, player):
        column = position % self._columns
        row = position / self._rows
        if self._board[row][column] == None:
            self._board[row][column] = player.token
            return True
        else:
            return False
