from .air import Air
from random import random, shuffle, randint


class Gas:
    """
    a base class for all gasses
     - handle flowing
     - spreading
    """

    def copy(self, board):
        if self.thickness <= 1:
            return
        split_ratio = random()
        # check 3 rand pos
        for _ in range(3):
            xoff = randint(-2, 3)
            yoff = randint(-2, 3)
            # so if pos out of board no
            if 0 <= self.y + yoff < len(board) and 0 <= self.x + xoff < len(board[0]):

                if type(board[self.y + yoff, self.x + xoff]) == Air:
                    board[self.y + yoff, self.x + xoff] = type(self)(
                        self.x + xoff, self.y + yoff, self.thickness * split_ratio
                    )
                self.thickness *= 1 - split_ratio
                return

    def move(self, board):
        if self.y <= 0:
            return
        moves = []
        if self.x > 0 and board[self.y - 1, self.x - 1].mass < self.y:
            moves.append((self.x - 1, self.y - 1))
        if (
            self.x < len(board[self.y]) - 1
            and board[self.y - 1, self.x + 1].mass < self.y
        ):
            moves.append((self.x + 1, self.y - 1))
        if len(moves) != 0:
            shuffle(moves)
            return moves[0]

    def check_temp(self):
        # if cold go to solid
        is_min_temp = type(self).min_temp is not None
        if is_min_temp and self.temp < type(self).min_temp:
            return {"type": self.to_liquid(), "temp": self.temp} 
