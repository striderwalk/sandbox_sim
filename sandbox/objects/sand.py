from .particle import Particle
from .solid import Solid
from .properties import sand_vals

class Sand(Particle, Solid):
    """
    a Particle that will fall
     - down
    """

    colour = (222, 207, 111)
    
    temp = sand_vals["start_temp"]

    ### rules ###
    max_temp = sand_vals["max_temp"]
    min_temp = sand_vals["min_temp"]
    htrans_num = sand_vals["htrans_num"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=20)
        Solid.__init__(self)
        self.update_colour()
        self.temp = temp

    def to_liquid(self):
        from .lava import Lava
        return Lava

    def update(self, board):
        if res := self.check():
            return res

        # update temp
        self.update_temp(board)

        # time since created
        self.life_len += 1

        # check not at bottom of board
        if self.y == len(board) - 1:
            return

        # update pos
        if board[self.y + 1, self.x].mass < self.mass:
            self.moveTo(board, self.x, self.y + 1)


        return self.check_temp()