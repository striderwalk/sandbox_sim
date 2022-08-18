from .particle import Particle
from .liquid import Liquid
from .air import Air
from .fume import Fume
from random import randint, random


class Acid(Particle, Liquid):
    """
    a Particle never moves

    """

    colour = (62, 243, 65)

    def __init__(self, x, y):
        super().__init__(x, y, mass=0.9)
        Liquid.__init__(self)
        self.update_colour()
        self.wetness = 7
        self.strength = randint(15, 17)

    def check_other(self, board):
        # check below
        if self.y < len(board) - 1 and board[self.y + 1, self.x].type == "solid":
            # kill other
            board[self.y + 1, self.x].health -= self.strength

        # check above
        if self.y > 0 and board[self.y - 1, self.x].type == "solid":
            # kill other
            board[self.y - 1, self.x].health -= self.strength
        # check left
        if self.x < len(board) - 1 and board[self.y, self.x + 1].type == "solid":
            # kill other
            board[self.y, self.x + 1].health -= self.strength

        # check right
        if self.x != 0 and board[self.y, self.x - 1].type == "solid":
            # kill other
            board[self.y, self.x - 1].health -= self.strength

    def update(self, board):

        self.check_other(board)

        if random() > 0.85 and type(board[self.y - 1, self.x]) == Air:
            board[self.y - 1, self.x] = Fume(self.x, self.y - 1)

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)