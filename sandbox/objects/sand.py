from .particle import Particle
from .properties import sand_vals
from .solid import Solid


class Sand(Particle, Solid):
    """
    a Particle that will fall
     - down
     - I don't like sand - Anakin Skywalker 32 BBY
    """

    colour = (222, 207, 111)

    temp = sand_vals["start_temp"]

    ### rules ###
    max_temp = sand_vals["max_temp"]
    min_temp = sand_vals["min_temp"]
    conduct = sand_vals["conduct"]
    mass = sand_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Sand.mass)
        Solid.__init__(self)
        self.temp = temp

    def to_liquid(self):
        from .lava import Lava

        return Lava

    def update(self, board):
        res = self.check()
        if res:
            return res

        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)

        # time since created
        self.life_len += 1

        # check not at bottom of board
        if self.y == len(board) - 1:
            return

        # update pos
        if board[self.y + 1, self.x].mass < self.mass:
            self.moveTo(board, self.x, self.y + 1)

        return self.check_temp()
