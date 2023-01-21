from .liquid import Liquid
from .particle import Particle
from .properties import lava_vals
from .stone import Stone


class Lava(Particle, Liquid):
    """
    hot wetness
    """

    colour = (245, 134, 70)

    temp = lava_vals["start_temp"]

    ### rules ###
    max_temp = lava_vals["max_temp"]
    min_temp = lava_vals["min_temp"]
    conduct = lava_vals["conduct"]
    mass = lava_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Lava.mass, is_flame=True)
        Liquid.__init__(self)

        self.wetness = 3

        self.temp = temp

    def to_gas(self):
        return None

    def to_solid(self):

        return Stone

    def update(self, board):

        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)

        # time since created
        self.life_len += 1

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        return self.check_temp()
