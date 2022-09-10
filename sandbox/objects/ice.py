from .particle import Particle
from .solid import Solid


class Ice(Particle, Solid):
    """
    a solid water
    """

    colour = (63,208,212)
    temp = 10


    ### rules ###
    max_temp = 20
    min_temp = 0

    def __init__(self, x, y, health=100):
        super().__init__(x, y, mass=1000, static=True, health=health)
        Solid.__init__(self)
        self.update_colour()
        self.temp = Ice.temp

    def to_liquid(self):
        from .water import Water
        return Water

    def update(self, board):
        if res := self.check():
            return res

        # update temp
        self.update_temp(board)
        return self.check_temp()

