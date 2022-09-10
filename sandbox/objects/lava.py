from .particle import Particle
from .liquid import Liquid
from .steam import Steam
from .stone import Stone


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
    temp = 255
 
    def __init__(self, x, y):
        super().__init__(x, y, mass=1, is_flame=True)
        Liquid.__init__(self)

        self.update_colour()
        self.wetness = 3

        self.temp = Lava.temp

    def check_water(self, board):
        from .water import Water

        up = self.y != 0
        down = self.y < len(board)-1
        left = self.x != len(board[0]) - 1 
        right = self.x != 0

        if (
            up and type(board[self.y - 1, self.x]) == Water
        ):  # check above if not on top
            board[self.y - 1, self.x] = Steam(self.x, self.y - 1)
            return "dies"

        if down and type(board[self.y + 1, self.x]) == Water:  # check below
            board[self.y + 1, self.x] = Stone(self.x, self.y - 1)
            return Stone
        if (
            right and type(board[self.y, self.x - 1]) == Water
        ):  # check right if not on edge
            board[self.y, self.x - 1] = Stone(self.x - 1, self.y)
            return Stone
        if (
            left and type(board[self.y, self.x + 1]) == Water
        ):  # check left if not on edge
            board[self.y, self.x + 1] = Stone(self.x + 1, self.y)
            return Stone

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

        # check for water
        if res := self.check_water(board):
            return res

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)


        return self.check_temp()
