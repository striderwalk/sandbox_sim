from .particle import Particle
from .air import Air
from .ash import Ash
from .water import Water
from .lava import Lava
from .fire import Fire
from random import randint, random


class Wood(Particle):
    """
    a Partical never moves
    
    but if on fire BURN!!!
     - when done turn to ash

    """

    colour = (90, 50, 6)

    def __init__(self, x,y):
        super().__init__(x, y, mass=1000, static=True)

        self.update_colour()
        self.fire_count = -1


    def rot(self, board):
        # if neighbour is water start to rot
        for _, other in self.get_neighbours(board, 2):
            if type(other) == Water:
                self.colour = (self.colour[0], self.colour[1] + 2, self.colour[2])

    def check_lava(self, board):
        if self.fire_count > 0:
            return
            
        for _, other in self.get_neighbours(board, 2):
            if type(other) == Lava:
                self.fire_count += 2
            elif self.fire_count > 0 and type(other) == Wood:
                other.fire_count += 0.3
        
    def update(self, board):
        # age
        self.life_len += 1
        # check if upade needed
        if self.check_self(board):
            return

        # check for rot level
        if self.colour[1] > 100:
            return "dies"
        # check if BURN
        elif self.colour[0] < 10 or self.colour[1] < 10:
            self.fire_count = 0

        # rot self
        if self.life_len % 10 == 1:
            self.rot(board)

       # burning
        if self.fire_count != 0:
            self.check_lava(board)

        if self.fire_count > 0:
            self.check_lava(board)
            for _, other in self.get_neighbours(board, 2):
                if type(other) == Air:
                    board[other.y, other.x] = Fire(other.x, other.y)
                    self.fire_count -= 1
                    self.colour = (self.colour[0] -1 , self.colour[1] -1, self.colour[2])
                    break

        elif self.fire_count == 0:
            if random() > 0.4:
                return Ash 
            else:
                return "dies"



