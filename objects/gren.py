from .particle import Particle
from .solid import Solid


class Gren(Particle, Solid):
    """
    gren is good

    """

    colour = (22, 166, 24)

    def __init__(self, x, y):
        super().__init__(x, y, mass=1000, static=True)
        Solid.__init__(self)

        self.update_colour()

    def update(self, board):
        if res := self.check():
            return res
