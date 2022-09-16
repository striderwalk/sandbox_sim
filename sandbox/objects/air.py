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
    htrans_num = air_vals["htrans_num"]
    
    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=0)
        self.colour = tuple(Air.colour)
        self.temp = temp

    def to_liquid(self):
        self.temp = Air.min_temp

    def update(self, board):
        self.update_temp(board)

        # if abs(self.temp - Air.temp) > 500:
        #     print(self)

        self.next_temp += (Air.temp-self.next_temp)*0.5
            