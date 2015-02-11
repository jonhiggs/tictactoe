from player import *

class Human(Player):

    def __init__(self, token):
        self._token = token
        self._moves = 0
        super(Player, self).__init__()

    def move(self, board_mask):
        position = int(raw_input("Where do you want to move"))
        self.move_to(position, board_mask)
