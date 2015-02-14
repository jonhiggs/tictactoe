import pdb

class Position(object):
    def __init__(self, mask):
        self._mask = mask
        self._owner = None
        # TODO: raise error if position isn't part of the path.

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def vacant(self):
        if self.owner == None:
            return True

    #@property
    #def paths(self):
    #    """ array of paths that this position is a member of """
    #    return None

    #@property
    #def number(self):
    #    pdb.set_trace()
    #    return self._number

    #def winning_paths(self):
    #    """ return the number of potential willing paths that can be formed
    #    with this position. """

    #    for p in self._player.paths:
    #        self._player.paths[p].mask
    #    return 0

