from .particle import Particle
from .solid import Solid


class Gren(Particle, Solid):
    """
    gren is good

    """

    colour = (22, 166, 24)
    temp = 100

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=1000, static=True)
        Solid.__init__(self)
        self.update_colour()
        self.temp = temp

    def update(self, board):
        if res := self.check():
            return res

        # update temp
        self.update_temp(board)
