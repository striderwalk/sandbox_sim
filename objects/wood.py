from .particle import Particle

from .water import Water
from .lava import Lava
from .fire import Fire
from random import randint


class Wood(Particle):
    """
    a Partical never moves
    but fire is true

    """
    
    colour = (90, 50, 6)

    def __init__(self, x,y):
        super().__init__(x, y, mass=1000, static=True)

        self.update_colour()
        self.fire_count = -1


    def rot(self, board):
        # if neighbour is water start to rot
        for other in self.get_neighbours(board, 2):
            if type(other) == Water:
                self.colour = (self.colour[0], self.colour[1] + 2, self.colour[2])

    def check_lava(self, board):
        for other in self.get_neighbours(board, 2):
            if type(other) == Lava:
                self.fire_count += 3
            elif self.fire_count > 0 and type(other) == Wood:
                other.fire_count += 0.3
        
    def update(self, board):
        # check for rot level
        if self.colour[1] > 100:
            return "dies"

        # rot self
        self.rot(board)

       # burning
        self.check_lava(board)
        
    
        if self.fire_count > 0:
            for other in self.get_neighbours(board, 2):
                if type(other) == Air:
                    board[other.y][other.x] = Fire(other.x, other.y)
                    self.fire_count -= 1

        elif self.fire_count == 0:
            return "dies" # Ash 