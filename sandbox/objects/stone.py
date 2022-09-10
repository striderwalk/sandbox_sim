from .particle import Particle
from .solid import Solid


class Stone(Particle, Solid):
    """
    a Particle never moves

    """

    colour = (117, 127, 128)
    temp = 100


    ### rules ###
    max_temp = 150
    min_temp = 0

    def __init__(self, x, y, health=100, temp=temp):
        super().__init__(x, y, mass=1000, static=True, health=health)
        Solid.__init__(self)
        self.update_colour()
        self.temp = temp

    def to_liquid(self):
        from .lava import Lava
        return Lava

    def update(self, board):
        self.update_temp(board)

        if res := self.check():
            return res

        return self.check_temp()

