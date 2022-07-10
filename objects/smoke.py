from .particle import Particle
from .gas import Gas
from .air import Air
from random import random, randint, choice

class Smoke(Particle, Gas):
    """
    a Partical that will rise
     - up
     - up to the left
     - up to the left 
    will pool
     - when only above water
    
    has a random chance of spliting
     - lowers thickness of self
     - copy self to random free tile in 3x3 square 

    """
    colour = (7, 53, 54)

    def __init__(self, x,y, thick=1):
        super().__init__(x, y, mass=-4)
        self.thickness = thick
        self.update_colour()
        self.wetness = 15
        self.timeout = randint(90,110)
    

    def move(self, board):
        if self.y <= 0:
            return
        moves = []
        if self.x > 0:
            moves.append((self.x-1, self.y-1))      
        if self.x < len(board[self.y])-1:
            moves.append((self.x+1, self.y-1))
        if len(moves) != 0:
            self.moveTo(board, *choice(moves))

    def copy(self,board):
        if self.thickness <=1: return
        split_ratio = random()
        # check 3 rand pos
        for _ in range(3):
            xoff = randint(-2,3)
            yoff = randint(-2,3)
            # so if pos out of board no
            if 0 <= self.y+yoff < len(board) and 0 <= self.x+xoff < len(board[0]):

                if type(board[self.y+yoff][self.x+xoff]) == Air:
                    board[self.y+yoff][self.x+xoff] = Smoke(self.x+xoff,self.y+yoff,self.thickness*split_ratio)
                self.thickness *= 1-split_ratio
                return

    def update(self,board):
        # time since created
        self.life_len += 1

        # check for timeout
        # timeout = 100 ± 10
        if self.life_len > self.timeout:
            return "dies"

        # check not at top of board
        if self.y == 0: return

         # update postion
        self.move(board)
        # spread
        if random() > 0.5:
            self.copy(board)
        # flow
        self.flow(board)
