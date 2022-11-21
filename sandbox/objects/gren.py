from .particle import Particle
from .solid import Solid
from .properties import gren_vals


class Gren(Particle, Solid):
    """
    gren is life

    """

    colour = (22, 166, 24)

    temp = gren_vals["start_temp"]

    ### rules ###
    max_temp = gren_vals["max_temp"]
    min_temp = gren_vals["min_temp"]
    conduct = gren_vals["conduct"]
    mass = gren_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Gren.mass, static=True)
        Solid.__init__(self)
        self.temp = temp

    def update(self, board):
        if res := self.check():
            return res

        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)
