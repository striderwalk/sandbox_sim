from .particle import Particle
from .liquid import Liquid
from .air import Air
from .fume import Fume
from .properties import acid_vals
from random import randint, random


class Acid(Particle, Liquid):
    """
    a Particle never moves

    """

    colour = (62, 243, 65)
    temp = acid_vals["start_temp"]

    ### rules ###
    max_temp = acid_vals["max_temp"]
    min_temp = acid_vals["min_temp"]
    conduct = acid_vals["conduct"]
    mass = acid_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Acid.mass)
        Liquid.__init__(self)
        self.wetness = 10
        self.strength = randint(15, 17)
        self.temp = temp

    def to_gas(self):
        return Fume

    def to_solid(self):
        return None

    def check_other(self, others):
        # check below
        action = False
        for other in others:
            if other.type == "solid":
                other.health -= self.strength
                action = True

    def update(self, board):
        self.life_len += 1
        others = self.get_others(board)
        self.update_temp(others)

        self.check_other(others)

        up = isinstance(board[self.y - 1, self.x], Air)
        if random() > 0.85 + (self.life_len / 1000) and up:

            new = Fume(self.x, self.y - 1, self.next_temp)
            board[self.y - 1, self.x] = new

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        return self.check_temp()
