from .particle import Particle
from .air import Air


class Fountain(Particle):
    """
    spawns particles of given type

    """

    colour = (247, 227, 45)

    def __init__(self, x, y, obj):
        super().__init__(x, y, mass=1000, static=True, obj=obj)
        self.type = "solid"
        self.obj = obj
        self.colour = Fountain.colour
        self.temp = obj.temp
        self.conduct = obj.conduct

    def update(self, board):
        for _, other in self.get_neighbours(board, 3):
            if self.obj != Air:
                if isinstance(other, Air):
                    board[other.y, other.x] = self.obj(other.x, other.y)
            elif not isinstance(other, Fountain):
                board[other.y, other.x] = self.obj(other.x, other.y)

    def __repr__(self):
        return f"{self.__class__.__name__} of object {self.obj.__name__}"
