import pdb
from mask import Mask

class Board(object):
    def __init__(self, rows=3, columns=3):
        self._rows = rows
        self._columns = columns
        self._players = []
        self._positions = []
        for i in (self.rows * self.columns):
            self._positions.append(Position(Mask(i, 'int')))

    @property
    def rows(self): return self._rows

    @property
    def positions(self): return self._positions

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

    @property
    def display(self):
        b = "\n\n"
        i = 1
        for position in self.positions:
            if position.owner == None:
                b += " ".center(8)
            else:
                b += position.owner.token.center(8)

            if (i % self.rows):
                b += " | "
            elif (i == self.rows * self.columns):
                b += "\n"
            else:
                b += "\n"
                b += "-" * ((8 * self.rows) + 5)
                b += "\n"
            i += 1

        return b
