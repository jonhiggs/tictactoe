from random import randint, shuffle

from board import *

class Game(object):

    def __init__(self):
        self._players = []
        rows = 3
        columns = 3

        self._tokens = []

        #for player in range(0,players):
        #    human = raw_input('Player %s, Are you human? (y/n): ' % (player+1))
        #    if human in ['y']: self._players.append(super(Human, self))
        #    else: self._players[player] = AI()

        #self._board = Board(players, rows, columns)

    def add_player(self, player):
        if player.token not in self._tokens:
            try:
                self._tokens.append(player.token)
                self._players.append(player)
                shuffle(self._players)
            except:
                print "That token has already been taken"


    @property
    def players(self):
        return len(self._players)

    @property
    def next_player(self):
        player = self._players.pop(0)
        self._players.append(player)
        return player

    @property
    def won(self):
        return False
