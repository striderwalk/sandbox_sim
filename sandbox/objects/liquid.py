from .air import Air
from random import shuffle


class Liquid:
    """
    a base class for all liquids
     - handle flowing
     - moving
    """

    def __init__(self):
        self.type = "liquid"

    def check_temp(self):
        is_max_temp = type(self).max_temp is not None
        if is_max_temp and self.temp > type(self).max_temp:
            return {"type": self.to_gas()}

        is_min_temp = type(self).min_temp is not None
        if is_min_temp and self.temp < type(self).min_temp:
            return {"type": self.to_solid()}

    def move(self, board):
        """
        - first move down
        - move down left/ down right
        - move left/ right
        """
        cols = len(board[self.y])

        down = self.y < len(board) - 1
        left = self.x > 0
        right = self.x < cols - 1

        # check move down
        if down and board[self.y + 1][self.x].mass < self.mass:
            return (self.x, self.y + 1)

        moves = []
        # check move left
        if down and left and board[self.y + 1][self.x - 1].mass < self.mass:
            moves.append((self.x - 1, self.y + 1))

        # check move right
        if down and right and board[self.y + 1][self.x + 1].mass < self.mass:
            moves.append((self.x + 1, self.y + 1))

        # choose move
        if len(moves) > 0:
            shuffle(moves)
            return moves[-1]

        self_type = type(self)
        max_x = cols - 1
        for i in range(1, self.wetness):
            left = left and self.x > i

            right = right and self.x < max_x

            if left:
                left_item = board[self.y, self.x - 1]
                if isinstance(left_item, Air):
                    moves.append(left_item.pos)
                elif not isinstance(left_item, self_type) or isinstance(left_item, Air):
                    left = False

            if right:
                right_item = board[self.y, self.x + 1]
                if isinstance(right_item, Air):
                    moves.append(right_item.pos)
                elif not isinstance(right_item, self_type):
                    right = False

            # choose move
            if len(moves) > 0:
                shuffle(moves)
                return moves[-1]
