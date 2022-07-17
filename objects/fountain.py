from .particle import Particle
from .air import Air

class Fountain(Particle):
    """
    spawns particel of given type

    """
    
    colour = (247, 227, 45)

    def __init__(self, x,y, obj):
        super().__init__(x, y, mass=1000, static=True)
        self.obj = obj


    def update(self,board):
        for _, other in self.get_neighbours(board, 3):
            if type(other) == Air:
                board[other.y, other.x] = self.obj(other.x, other.y)
