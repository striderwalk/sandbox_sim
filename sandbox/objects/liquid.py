from .air import Air
from random import shuffle
import logging


class Liquid:
    """
    a base class for all liquids
     - handle flowing
     - moving
    """

    def __init__(self):
        self.type = "liquid"
        self.has_moved = 0

    def check_temp(self):
        is_max_temp = self.__class__.max_temp is not None
        if is_max_temp and self.temp > self.__class__.max_temp:
            return {"type": self.to_gas()}

        is_min_temp = self.__class__.min_temp is not None
        if is_min_temp and self.temp < self.__class__.min_temp:
            return {"type": self.to_solid()}

    def check_air(self, board):
        """
        check for contact with air
        """
        for i in self.get_others(board):
            if isinstance(i, Air):
                return True

        return False

    def move(self, board):
        """
        - first move down
        - move down left/ down right
        - move left/ right
        """
        if self.y >= len(board) - 1:
            return
        if self.has_moved != 0:

            self.has_moved -= 1
            if self.check_air(board):
                self.has_moved = 0

            return

        cols = len(board[self.y])

        down = self.y < len(board) - 1
        left = self.x > 0
        right = self.x < cols - 1

        # check move down

        if down and board[self.y + 1][self.x].mass < self.mass:
            return (self.x, self.y + 1)

        moves = []
        if down and left and board[self.y + 1][self.x - 1].mass < self.mass:
            moves.append((self.x - 1, self.y + 1))

        if down and right and board[self.y + 1][self.x + 1].mass < self.mass:
            moves.append((self.x + 1, self.y + 1))

        if moves:  # can be ased to import random.choice
            shuffle(moves)
            return moves[-1]

        max_x = cols - 1
        for i in range(1, self.wetness):
            left, right = self.check_move(board, left, right, moves, max_x, i)

        # choose move
        if moves:
            shuffle(moves)
            return moves[-1]
        else:
            # don't move for 3 times cus speed
            self.has_moved += 3

    def check_move(self, board, left, right, moves, max_x, i):
        left = left and self.x > i
        right = right and self.x < max_x

        left = self._check_item(board, moves, left, -1) if left else left
        right = self._check_item(board, moves, left, +1) if right else right

        return left, right

    def _check_item(self, board, moves, dir_bool, adder):
        other_item = board[self.y, self.x + adder]
        if isinstance(other_item, Air):
            moves.append(other_item.pos)
            dir_bool = False

        elif not isinstance(other_item, self.__class__):
            dir_bool = False
        return dir_bool
