from .particle import Particle

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
            
        # time since created
        self.life_len += 1
        
        # check not at bottom of board
        if self.y == len(board)-1: return

        # update pos
        if board[self.y+1, self.x].mass < self.mass: self.moveTo(board,self.x,self.y+1)
        # check not at bottom of board
        if self.y == len(board)-1: return


        
