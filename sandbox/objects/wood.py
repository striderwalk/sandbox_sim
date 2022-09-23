from .particle import Particle
from .air import Air
from .ash import Ash
from .water import Water
from .fire import Fire
from .solid import Solid
from .properties import wood_vals
from random import random


class Wood(Particle, Solid):
    """
    a Particle never moves

    but if on fire BURN!!!
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

    def rot(self, board):
        # if neighbour is water start to rot
        rot = any([type(i) == Water for i in self.get_others(board)])

        if rot:
            if self.fire_count > 0:
                self.fire_count = -10
            else:
                self.fire_count -= 1

            self.colour = (self.colour[0], self.colour[1] + 2, self.colour[2])

    def check_lava(self, board):

        if self.fire_count > 0:
            return

        if self.y > 0:  # above
            if board[self.y - 1, self.x].is_flame:
                self.fire_count += 2
            elif self.fire_count > 0 and type(board[self.y - 1, self.x]) == Wood:
                board[self.y - 1, self.x].fire_count += 0.3

        if self.x > 0:  # left
            if board[self.y, self.x - 1].is_flame:
                self.fire_count += 2
            elif self.fire_count > 0 and type(board[self.y, self.x - 1]) == Wood:
                board[self.y, self.x - 1].fire_count += 0.3

        if self.y < len(board) - 1:  # below
            if board[self.y + 1, self.x].is_flame:
                self.fire_count += 2
            elif self.fire_count > 0 and type(board[self.y + 1, self.x]) == Wood:
                board[self.y + 1, self.x].fire_count += 0.3

        if self.x < len(board[self.y]) - 1:  # right
            if board[self.y, self.x + 1].is_flame:
                self.fire_count += 2
            elif self.fire_count > 0 and type(board[self.y, self.x + 1]) == Wood:
                board[self.y, self.x + 1].fire_count += 0.3

    def update(self, board):
        if res := self.check():
            return res

        # update temp
        self.update_temp(board)

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
            self.rot(board)

        # burning
        if self.fire_count != 0:
            self.check_lava(board)

        if self.fire_count > 0:
            self.check_lava(board)
            for _, other in self.get_neighbours(board, 2):
                if type(other) == Air:
                    board[other.y, other.x] = Fire(other.x, other.y)
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
