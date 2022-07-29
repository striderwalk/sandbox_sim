from .particle import Particle
from .gas import Gas
from random import random, randint


class Fume(Particle, Gas):
    """
    a Particle that will rise randomly
     - up
     - up to the left
     - up to the left

    has a random chance of splitting
     - lowers thickness of self
     - copy self to random free tile in 3x3 square

    """

    colour = (214, 245, 167)

    def __init__(self, x, y, thick=1):
        super().__init__(x, y, mass=-4)
        self.thickness = thick
        self.update_colour()
        self.wetness = 15
        self.timeout = randint(20, 35)

    def update(self, board):
        # check if update needed
        if self.check_self(board):
            return

        # time since created
        self.life_len += 1

        # check for timeout
        # timeout = 100 ± 10
        if self.life_len > self.timeout:
            return "dies"

        # check not at top of board
        if self.y == 0:
            return

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        # spread
        if random() > 0.5:
            self.copy(board)
