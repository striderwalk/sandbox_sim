from .particle import Particle
from .solid import Solid


class Stone(Particle, Solid):
    """
    a Particle never moves

    """

    colour = (117, 127, 128)
    temp = 0

    def __init__(self, x, y, health=100):
        super().__init__(x, y, mass=1000, static=True, health=health)
        Solid.__init__(self)
        self.update_colour()
        self.temp = Stone.temp

    def to_liquid(self):
        from .lava import Lava
        return Lava

    def update(self, board):
        if res := self.check():
            return res

        # update temp
        # print()
        # print(self.temp)
        self.update_temp(board)
        # print(self.temp)
        return self.check_temp()

