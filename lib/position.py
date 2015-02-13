class Position(object):
    def __init__(self, position, path):
        self._position = position
        self._path = path
        self._player = path._player
        # TODO: raise error if position isn't part of the path.

    @property
    def vacant(self):
        return self._player.board.vacant(self)

    def winning_paths(self):
        """ return the number of potential willing paths that can be formed
        with this position. """

        for p in self._player.paths:
            self._player.paths[p].mask
        return 0

