import pdb
from mask import Mask

class Board(object):
    def __init__(self, rows=3, columns=3):
        self._rows = rows
        self._columns = columns
        self._players = []

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

    @property
    def display(self):
        b = "\n\n"
        i = 1
        for position in list(self.state):
            if position == "_":
                b += " ".center(8)
            else:
                b += position.center(8)

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

    @property
    def state(self):
        state = list("_________")
        for player in self._players:
            for position in range(0,9):
                if player.moves.bit(position) == 1:
                    state[position] = str(player.token)

        return "".join(state)


    def vacant(self, position):
        return list(self.state)[position] == "_"
