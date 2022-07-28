from .particle import Particle
from .soild import Soild

class Gren(Particle, Soild):
    """
    gren is good

    """
    
    colour = (22, 166, 24)

    def __init__(self, x,y):
        super().__init__(x, y, mass=1000, static=True)
        self.update_colour()


    def update(self,board): 
        if (res := self.check()):
            return res
