from .particle import Particle
from .smoke import Smoke

class Ash(Particle):
    """
    a Partical that will fall
     - down
    """

    colour = (54,69,79)

    def __init__(self, x,y):
        super().__init__(x, y, mass=20)
        self.update_colour()


    def update(self,board):
        # check if upade needed
        if self.check_self(board):
            return
            
        # if on top of wood turn to smoke
        if self.y < len(board)-1 and board[self.y+1][self.x].flamable:
            return Smoke
        # time since created
        self.life_len += 1
        
        # check not at bottom of board
        if self.y == len(board)-1: return

        # update pos
        if board[self.y+1, self.x].mass < self.mass: self.moveTo(board,self.x,self.y+1)
        # check not at bottom of board
        if self.y == len(board)-1: return


        
