import logging
from .particle import Particle
from .properties import stone_vals


class Barrier(Particle):
    """
    i can not be harmed by words or guns

    """

    colour = (255, 0, 0)
    temp = 22
    conduct = 0

    def __init__(self, x, y):
        super().__init__(x, y, mass=1000, static=True)
        self.temp = 22
        self.type = "debug"

    def update(self, board):
        ...
