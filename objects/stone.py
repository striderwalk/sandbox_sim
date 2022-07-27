from .particle import Particle
from .soild import Soild

class Stone(Particle, Soild):
    """
    a Partical never moves

    """
    
    colour = (117,127,128)

    def __init__(self, x,y, health=100):
        super().__init__(x, y, mass=1000, static=True,health=health)
        self.update_colour()


    def update(self,board): 
        if (res := self.check()):
            return res
