from random import randint, random

from .gas import Gas
from .particle import Particle
from .properties import fume_vals


class Fume(Particle, Gas):
    """
    a Particle that will rise randomly
     - up
     - up to the left
     - up to the left

    has a random chance of splitting
     - lowers thickness of self
     - copy self to random free tile in 3x3 squar

    small chance of choroding
    """

    colour = (214, 245, 167)
    temp = fume_vals["start_temp"]

    ### rules ###
    max_temp = fume_vals["max_temp"]
    min_temp = fume_vals["min_temp"]
    conduct = fume_vals["conduct"]
    mass = fume_vals["mass"]

    def __init__(self, x, y, thick=1, temp=temp):
        super().__init__(x, y, mass=Fume.mass)
        Gas.__init__(self)
        self.thickness = thick
        self.wetness = 15
        self.timeout = randint(20, 35)
        self.strength = 1
        self.temp = temp

    def check_other(self, board):
        # get them
        others = self.get_others(board)

        # punish them
        for other in others:
            if other.type == "solid":
                other.health -= self.strength

    def to_liquid(self):
        return "dies"

    def update(self, board):

        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)

        # time since created
        self.life_len += 1
        self.check_other(board)
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
