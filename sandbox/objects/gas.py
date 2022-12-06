from .air import Air
from random import random, choice, randint


class Gas:
    """
    a base class for all gasses
     - flowing
     - cloning
    """

    def __init__(self):
        self.type = "gas"

    def copy(self, board):
        if self.thickness <= 1:
            return
        split_ratio = random()
        # check 3 rand pos
        for _ in range(3):
            xoff = randint(-2, 3)
            yoff = randint(-2, 3)
            # so if pos out of board no
            y_axis = 0 <= self.y + yoff < len(board)
            x_axis = 0 <= self.x + xoff < len(board[0])
            if y_axis and x_axis:

                if type(board[self.y + yoff, self.x + xoff]) == Air:

                    x = self.x + xoff
                    y = self.y + yoff
                    thick = self.thickness * split_ratio
                    temp = self.next_temp

                    board[self.y + yoff, self.x + xoff] = type(self)(
                        x, y, thick=thick, temp=temp
                    )

                self.thickness *= 1 - split_ratio
                return

    def move(self, board):
        left = self.x > 0
        right = self.x < len(board[self.y]) - 1
        up = self.y > 0

        others = []
        if up:
            others.append(board[self.y - 1][self.x])

        if left and up:
            others.append(board[self.y - 1][self.x - 1])

        if right and up:
            others.append(board[self.y - 1][self.x + 1])

        moves = [(i.x, i.y) for i in others if i.mass < self.mass or isinstance(i, Air)]

        if len(moves) != 0:
            return choice(moves)

    def check_temp(self):
        # if cold go to solid
        is_min_temp = type(self).min_temp is not None
        if is_min_temp and self.temp < type(self).min_temp:
            return {"type": self.to_liquid()}
