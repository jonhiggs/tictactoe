from player import *
from random import randint, shuffle

class AI(Player):

    def __init__(self):
        self._board = None
        self._moves = Mask('000')
        self._token = None

    def move(self):
        position = randint(0,8)
        self.move_to(position, board_mask)

    def winning_path(self):
        scores = []
        for path in winning_positions:
            mask = Mask(winning_positions["path"], bin)


### 1. Check if computer can make winning move
##def win_move(board, letter):
##    print "win move"
##    for number in range(0, 9):
##        try_board = board.get_copy_board()
##        print try_board.board
##        if try_board.is_empty(number):
##            try_board.board[number] = letter
##            print try_board.board
##            if try_board.win(letter):
##                return number
##    else: 
##        return False
##
### 2. Check if computer can block player from winning
##def block_move(board, letter):
##    print "block move"
##    for number in range(0, 9):
##        try_board = board.get_copy_board()
##        if try_board.is_empty(number):
##            try_board.board[number] = letter
##            if try_board.win(letter):
##                return number
##    else: 
##        return False
##
### 3. Take a corner piece (first one computer finds)
##def move_corner(board):
##    print "corner move"
##    for number in [0, 2, 6, 8]:
##        if board.is_empty(number):
##            return number
##    else: 
##        return False
##
### 4. Take center
##def move_center(board):
##    print "center move"
##    if board.is_empty(5):
##        return 5
##    else: 
##        return False
##
### 5. Take side (first one computer finds)
##def move_side(board):
##    print "side move"
##    for number in [1, 3, 5, 7]:
##        if board.is_empty(number):
##            return number
##    else: 
##        return False
##
