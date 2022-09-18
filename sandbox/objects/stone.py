import logging

from .particle import Particle
from .solid import Solid
from .properties import stone_vals


class Stone(Particle, Solid):
    """
    a Particle never moves

    """

    colour = (117, 127, 128)

    temp = stone_vals["start_temp"]

    ### rules ###
    max_temp = stone_vals["max_temp"]
    min_temp = stone_vals["min_temp"]
    htrans_num = stone_vals["htrans_num"]

    def __init__(self, x, y, health=100, temp=temp):
        super().__init__(x, y, mass=1000, static=True, health=health)
        Solid.__init__(self)
        self.update_colour()
        # if temp == Stone.temp:
        #     logging.info(f"{temp}, {x}, {y}")
        self.temp = temp

    def to_liquid(self):
        from .lava import Lava

        logging.debug(f"Stone of temp {self.temp} went to heaven")
        return Lava

    def update(self, board):
        self.update_temp(board)

        if res := self.check():
            return res

        return self.check_temp()
