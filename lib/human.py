import game

class Human(game.Game):

    def __init__(self):
        # create a list like this ' ' * 9
        self._token = None
        self._moves = '0b000000000'

    @property
    def token(self):
        return self._token
