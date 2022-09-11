from .particle import Particle
from .steam import Steam
from .stone import Stone
from .lava import Lava
from .properties import water_vals
from .liquid import Liquid

class Water(Particle, Liquid):
    """
    a Particle that will fall
     - down
     - down to the left
     - down to the left
    will pool
     - when only above water
    changed by lava
     - if above Lava turn to steam
     - if next to Lava turn to stone

    """

    colour = (64, 154, 245)
    
    temp = water_vals["start_temp"]

    ### rules ###
    max_temp = water_vals["max_temp"]
    min_temp = water_vals["min_temp"]
    density = water_vals["density"]

    def __init__(self, x, y, temp=temp):
        # make_steam stop water condense duplicating
        super().__init__(x, y, mass=1)
        Liquid.__init__(self)

        self.update_colour()
        self.wetness = 10
        self.temp = temp

    def to_gas(self):
        return Steam

    def to_solid(self):
        return None

    def update(self, board):
        if self.check_self(board):
            return

        # update temp
        self.update_temp(board)

        # time since created
        self.life_len += 1

        # check not at bottom of board
        if self.y == len(board) - 1:
            return
        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        return self.check_temp()
