from .particle import Particle

class Air(Particle):
    """
    a not acting partical 
    'ensuring' correct behavior of 
    all others   

    """


    colour = (255,255,255)
    def __init__(self, x,y):
        super().__init__(x, y, mass=-1)
        self.colour = tuple(Air.colour)
        


    def update(self,board):
        return
