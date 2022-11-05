import logging

from .particle import Particle
from .solid import Solid
from .properties import stone_vals


class Stone(Particle, Solid):
    """
    a Particle never moves

    """

    # colour = (117, 127, 128)
    colour = (105, 106, 106)
    temp = stone_vals["start_temp"]

    ### rules ###
    max_temp = stone_vals["max_temp"]
    min_temp = stone_vals["min_temp"]
    conduct = stone_vals["conduct"]
    mass = stone_vals["mass"]

    def __init__(self, x, y, health=100, temp=temp):
        super().__init__(x, y, mass=Stone.mass, static=True, health=health)
        Solid.__init__(self)
        # if temp == Stone.temp:
        # logging.info("LIFE HAS NOT GONE WELL")
        self.temp = temp

    def to_liquid(self):
        from .lava import Lava

        # logging.debug(f"Stone of temp {self.temp} went to heaven")
        return Lava

    def update(self, board):
        self.update_temp(board)

        if res := self.check():
            return res

        return self.check_temp()
