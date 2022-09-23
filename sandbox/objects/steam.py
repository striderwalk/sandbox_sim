from .particle import Particle
from .gas import Gas
from .properties import steam_vals
from random import random, randint


class Steam(Particle, Gas):
    """
    a Particle that will rise randomly
     - up
     - up to the left
     - up to the left

    has a random chance of splitting
     - lowers thickness of self
     - copy self to random free tile in 3x3 square

    condense self
     - turn to Water
    """

    colour = (167, 203, 204)

    temp = steam_vals["start_temp"]

    ### rules ###
    max_temp = steam_vals["max_temp"]
    min_temp = steam_vals["min_temp"]
    conduct = steam_vals["conduct"]
    mass = steam_vals["mass"]

    def __init__(self, x, y, thick=50, temp=temp):
        super().__init__(x, y, mass=Steam.mass)
        Gas.__init__(self)
        self.thickness = thick
        self.wetness = 5
        self.life_lim = randint(90, 110)
        self.temp = temp

    def to_liquid(self):
        from .water import Water

        return Water

    def update(self, board):

        # update temp
        self.update_temp(board)

        # time since created
        self.life_len += 1

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        # spread
        if random() > 0.5 and random() > self.thickness / 50:
            self.copy(board)

        return self.check_temp()
