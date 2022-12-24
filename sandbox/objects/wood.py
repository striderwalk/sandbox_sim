from random import random

from .air import Air
from .ash import Ash
from .fire import Fire
from .particle import Particle
from .properties import wood_vals
from .smoke import Smoke
from .solid import Solid
from .water import Water


class Wood(Particle, Solid):
    """
    a Particle never moves

    but if on fire will BURN!!
     - when done turn to ash

    """

    colour = (90, 50, 6)

    temp = wood_vals["start_temp"]

    ### rules ###
    max_temp = wood_vals["max_temp"]
    min_temp = wood_vals["min_temp"]
    conduct = wood_vals["conduct"]
    mass = wood_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Wood.mass, static=True, is_flame=False)
        Solid.__init__(self)

        self.fire_count = -1
        self.temp = temp

    def to_liquid(self):
        self.fire_count += 3

    @property
    def is_flame(self):
        return self.fire_count > 0

    def rot(self, others):
        # if neighbour is water start to rot
        rot = any([type(i) == Water for i in others])

        if rot:
            if self.fire_count > 0:
                self.fire_count = -10
            else:
                self.fire_count -= 1

            self.colour = (self.colour[0], self.colour[1] + 2, self.colour[2])

    def check_extinguish(self, others):

        for other in others:
            if type(other) == Air:
                break
            elif other.type == "liquid":
                self.fire_count = -1
                return
        else:
            self.fire_count = -1
            return

    def update(self, board):
        if res := self.check():
            return res

        others = list(self.get_others(board))

        # update temp
        self.update_temp(others)

        # age
        self.life_len += 1

        # check for rot level
        if self.colour[1] > 100:
            return {"type": "dies"}

        # check if BURN
        elif self.colour[0] < 10 or self.colour[1] < 10:
            self.fire_count = 0

        # rot self
        if self.life_len % 10 == 1:
            self.rot(others)

        if self.fire_count > 0:
            self.check_extinguish(others)

        if self.fire_count > 0:
            for other in others:
                if isinstance(other, Air):
                    if random() > 0.5:
                        board[other.y, other.x] = Fire(other.x, other.y)
                    else:
                        board[other.y, other.x] = Smoke(other.x, other.y)

                    self.fire_count -= 1
                    self.colour = (
                        self.colour[0] - 1,
                        self.colour[1] - 1,
                        self.colour[2],
                    )
                    break

        elif self.fire_count == 0:
            if random() > 0.4:
                return {"type": Ash}
            else:
                return {"type": "dies"}

        return self.check_temp()
