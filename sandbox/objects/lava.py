from .particle import Particle
from .liquid import Liquid
from .steam import Steam
from .stone import Stone
from .properties import lava_vals

class Lava(Particle, Liquid):
    """
    a Particle that will fall
     - down
     - down to the left
     - down to the left

    will flow

    affects Water
     - if Below Water turn to it steam
     - if next to Water turn to it and self stone

    """

    colour = (245, 134, 70)
    
    temp = lava_vals["start_temp"]

    ### rules ###
    max_temp = lava_vals["max_temp"]
    min_temp = lava_vals["min_temp"]
    htrans_num = lava_vals["htrans_num"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=1, is_flame=True)
        Liquid.__init__(self)

        self.update_colour()
        self.wetness = 3

        self.temp = temp

    def to_gas(self):
        return None

    def to_solid(self):
        return Stone

    def update(self, board):
        # check if update needed
        if self.check_self(board):
            return

        # update temp
        self.update_temp(board)

        # time since created
        self.life_len += 1


        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)


        return self.check_temp()
