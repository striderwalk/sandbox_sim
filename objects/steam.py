from .particle import Particle
from .gas import Gas
from .air import Air
from random import random, randint


class Steam(Particle, Gas):
    """
    a Particle that will rise randomly
     - up
     - up to the left
     - up to the left

    has a random chance of splitting
     - lowers thickness of self
     - copy self to random free tile in 3x3 square

    condense self
     - turn to Water
    """

    colour = (167, 203, 204)

    def __init__(self, x, y, thick=50):
        super().__init__(x, y, mass=-5)
        self.thickness = thick
        self.update_colour()
        self.wetness = 5
        self.life_lim = randint(90, 110)

    def update(self, board):
        # check if update needed
        if self.check_self(board):
            return

        # time since created
        self.life_len += 1

        # import here to avoid circular import
        from .water import Water

        # condense
        if self.life_len > self.life_lim:
            # bring neighbour with
            for other in self.get_neighbours(board, 2):
                if type(other) == Steam:
                    board[other.y, other.x] = Air(other.x, other.y)
            if random() > 0.95:
                if self.y < len(board) - 1:
                    board[self.y + 1, self.x] = Water(
                        self.x, self.y + 1, make_steam=False
                    )
            return "dies"

        # check not at top of board
        if self.y == 0:
            return

        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        # spread
        if random() > 0.5:
            if (result := self.copy(board)) and random() > self.thickness / 50:
                return result
