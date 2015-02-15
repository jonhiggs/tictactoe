import pdb
import player

class Human(player.Player):
    def __init__(self):
        self._board = None
        self._token = None

    def move(self):
        moved = False
        while not moved:
            position = int(raw_input("Where do you want to move? "))
            moved = self.move_to(position)
        return moved
