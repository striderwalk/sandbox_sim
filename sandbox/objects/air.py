from .particle import Particle


class Air(Particle):
    """
    DOCUMENTATION NEEDED
    """

    colour = (255, 255, 255)

    def __init__(self, x, y):
        super().__init__(x, y, mass=0)
        self.colour = tuple(Air.colour)

    def update(self, board):
        return
