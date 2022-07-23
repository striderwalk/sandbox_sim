from .particle import Particle
from .liquid import Liquid 
from .air import Air

class Acid(Particle, Liquid):
    """
    a Partical never moves

    """
    
    colour = (132, 217, 30)

    def __init__(self, x,y):
        super().__init__(x, y, mass=1)
        self.wetness = 1



    def check_other(self, board):
        # check for lava
        if self.y < len(board)-1 and board[self.y+1][self.x].static: # check below 
            # kill other and move
            board[self.y+1][self.x].health -= 10

        if self.y > 0 and board[self.y-1][self.x].static: # check above if not on top
            # kill other and move
            board[self.y-1][self.x].health -= 10

        if self.x < len(board)-1 and board[self.y][self.x+1].static: # check left if not on edge
            # kill other and move
            board[self.y][self.x+1].health -= 10
                
        if self.x !=0 and board[self.y][self.x-1].static: # check right if not on edge
            # kill other and move
            board[self.y][self.x-1].health -= 10

    def update(self,board):

        self.check_other(board)

        # update postion
        if (pos := self.move(board)):
            self.moveTo(board, *pos)    
