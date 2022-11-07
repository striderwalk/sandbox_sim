from .particle import Particle
from .properties import air_vals


class Air(Particle):
    """
    DOCUMENTATION NEEDED
    """

    colour = (255, 255, 255)
    temp = air_vals["start_temp"]

    ### rules ###
    max_temp = air_vals["max_temp"]
    min_temp = air_vals["min_temp"]
    conduct = air_vals["conduct"]
    mass = air_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Air.mass)
        self.type = "gas"
        self.colour = tuple(Air.colour)
        self.temp = temp

    def to_liquid(self):
        self.temp = Air.min_temp

    def update(self, board):

        others = list(self.get_others(board))

        self.update_temp(self.get_others(board))

        # room temp
        self.next_temp += (Air.temp - self.next_temp) * 0.1
