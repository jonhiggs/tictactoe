from player import *

class Human(Player):
    def __init__(self):
        self._board = None
        self._moves = Mask('000')
        self._token = None
        super(Player, self).__init__()

    def move(self):
        moved = False
        while not moved:
            position = int(raw_input("Where do you want to move? "))
            moved = self.move_to(position)
        return moved
