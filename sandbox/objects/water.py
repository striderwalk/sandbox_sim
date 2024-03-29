from .particle import Particle
from .steam import Steam
from .properties import water_vals
from .liquid import Liquid
from .ice import Ice


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
    conduct = water_vals["conduct"]
    mass = water_vals["mass"]

    def __init__(self, x, y, temp=temp):
        # make_steam stop water condense duplicating
        super().__init__(x, y, mass=Water.mass)
        Liquid.__init__(self)

        self.wetness = 15
        self.temp = temp

    def to_gas(self):
        return Steam

    def to_solid(self):
        return Ice

    def update(self, board):

        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)

        # time since created
        self.life_len += 1

        # update position

        if pos := self.move(board):
            self.moveTo(board, *pos)

        return self.check_temp()
