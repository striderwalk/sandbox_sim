from .particle import Particle
from .gas import Gas
from .properties import smoke_vals
from random import random, randint


class Smoke(Particle, Gas):
    """
    a Particle that will rise randomly
     - up
     - up to the left
     - up to the left

    has a random chance of splitting
     - lowers thickness of self
     - copy self to random free tile in 3x3 square

    """

    colour = (7, 53, 54)

    temp = smoke_vals["start_temp"]

    ### rules ###
    max_temp = smoke_vals["max_temp"]
    min_temp = smoke_vals["min_temp"]
    conduct = smoke_vals["conduct"]
    mass = smoke_vals["mass"]

    def __init__(self, x, y, thick=1, temp=temp):
        super().__init__(x, y, mass=Smoke.mass)
        Gas.__init__(self)
        self.thickness = thick
        self.wetness = 5
        self.timeout = randint(60, 80)
        self.temp = temp

    def to_liquid(self):
        return "dies"

    def update(self, board):

        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)

        # time since created
        self.life_len += 1

        # check for timeout
        # timeout = 100 ± 10
        if self.life_len > self.timeout:
            return {"type": "dies"}

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        # spread
        if random() > 0.5:
            self.copy(board)

        return self.check_temp()
