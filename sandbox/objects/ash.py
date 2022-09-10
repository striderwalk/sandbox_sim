from .particle import Particle
from .smoke import Smoke
from .solid import Solid


class Ash(Particle, Solid):
    """
    a Particle that will fall
     - down
    """

    colour = (54, 69, 79)
    temp = 115

    ### rules ###
    max_temp = 230
    min_temp = 0 

    def __init__(self, x, y):
        super().__init__(x, y, mass=20)
        Solid.__init__(self)
        self.update_colour()
        self.temp = Ash.temp


    def to_liquid(self):
        ### go to smoke for now ###
        return Smoke

    def update(self, board):
        if res := self.check():
            return res
        self.update_temp(board)
        # check if update needed
        if self.check_self(board):
            return

        # if on top of wood turn to smoke
        if self.y < len(board) - 1 and board[self.y + 1][self.x].flamable:
            return Smoke
        # time since created
        self.life_len += 1

        # check not at bottom of board
        if self.y == len(board) - 1:
            return

        # update pos
        if board[self.y + 1, self.x].mass < self.mass:
            self.moveTo(board, self.x, self.y + 1)

        return self.check_temp()
