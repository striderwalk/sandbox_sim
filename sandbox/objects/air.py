from .particle import Particle


class Air(Particle):
    """
    DOCUMENTATION NEEDED
    """

    colour = (255, 255, 255)
    temp = 6
    
    def __init__(self, x, y):
        super().__init__(x, y, mass=0)
        self.colour = tuple(Air.colour)
        self.temp = Air.temp

    def to_liquid(self):
        ...

    def update(self, board):
        self.update_temp(board)
