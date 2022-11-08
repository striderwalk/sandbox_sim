from .particle import Particle
from .solid import Solid
from .properties import ice_vals


class Ice(Particle, Solid):
    """
    a solid water
    """

    colour = (63, 208, 212)

    temp = ice_vals["start_temp"]

    ### rules ###
    max_temp = ice_vals["max_temp"]
    min_temp = ice_vals["min_temp"]
    conduct = ice_vals["conduct"]
    mass = ice_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Ice.mass, static=True)
        Solid.__init__(self)
        self.temp = temp

    def to_liquid(self):
        from .water import Water

        return Water

    def update(self, board):
        if res := self.check():
            return res

        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)

        return self.check_temp()
