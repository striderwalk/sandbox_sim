from .particle import Particle

class Gren(Particle):
    """
    a Partical never moves

    """
    
    colour = (10,150,10)

    def __init__(self, x,y):
        super().__init__(x, y, mass=1000, static=True)
        self.update_colour()


    def update(self,board): return 
