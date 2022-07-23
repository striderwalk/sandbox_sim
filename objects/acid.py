from .particle import Particle
from .liquid import Liquid 
from .air import Air
from random import randint

class Acid(Particle, Liquid):
    """
    a Partical never moves

    """
    
    colour = (132, 217, 30)

    def __init__(self, x,y):
        super().__init__(x, y, mass=1)
        self.wetness = 1
        self.strength = randint(15,17)



    def check_other(self, board):
        if self.strength <= 0:
            self.mass = 0.9
            return
        # check for lava
        if self.y < len(board)-1 and board[self.y+1][self.x].static: # check below 
            # kill other and move
            board[self.y+1][self.x].health -= self.strength
            self.strength -= 1

        if self.y > 0 and board[self.y-1][self.x].static: # check above if not on top
            # kill other and move
            board[self.y-1][self.x].health -= self.strength
            self.strength -= 1

        if self.x < len(board)-1 and board[self.y][self.x+1].static: # check left if not on edge
            # kill other and move
            board[self.y][self.x+1].health -= self.strength
            self.strength -= 1
                
        if self.x !=0 and board[self.y][self.x-1].static: # check right if not on edge
            # kill other and move
            board[self.y][self.x-1].health -= self.strength
            self.strength -= 1

    def update(self,board):

        self.check_other(board)

        # update postion
        if (pos := self.move(board)):
            self.moveTo(board, *pos)    
