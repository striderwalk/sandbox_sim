from .particle import Particle
from .smoke import Smoke
from .solid import Solid
from .properties import ash_vals


class Ash(Particle, Solid):
    """
    movent
    - goes down
    """

    colour = (54, 69, 79)
    temp = ash_vals["start_temp"]

    max_temp = ash_vals["max_temp"]
    min_temp = ash_vals["min_temp"]
    conduct = ash_vals["conduct"]
    mass = ash_vals["mass"]

    def __init__(self, x, y, temp=temp):
        super().__init__(x, y, mass=Ash.mass)
        Solid.__init__(self)
        self.temp = temp

    def to_liquid(self):
        ### go to smoke for now ###
        return Smoke

    def update(self, board):
        if res := self.check():
            return res

        others = list(self.get_others(board))
        self.update_temp(others)

        # if on top of wood turn to smoke
        if self.y < len(board) - 1 and board[self.y + 1][self.x].flamable:
            return {"type": Smoke}
        # time since created
        self.life_len += 1

        # check not at bottom of board
        if self.y == len(board) - 1:
            return

        # update pos
        if board[self.y + 1, self.x].mass < self.mass:
            self.moveTo(board, self.x, self.y + 1)

        return self.check_temp()
