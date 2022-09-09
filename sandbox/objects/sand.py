from .particle import Particle
from .solid import Solid


class Sand(Particle, Solid):
    """
    a Particle that will fall
     - down
    """

    colour = (222, 207, 111)

    def __init__(self, x, y):
        super().__init__(x, y, mass=20)
        Solid.__init__(self)
        self.update_colour()
        self.temp = 0

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
        # check not at bottom of board
        if self.y == len(board) - 1:
            return
