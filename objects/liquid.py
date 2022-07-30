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

    def move(self, board):
        """
        - first move down
        - move down left/ down right
        - move left/ right
        """

        down = self.y < len(board) - 1
        left = self.x > 0
        right = self.x < len(board[self.y]) - 1

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

        for i in range(1, self.wetness):
            left = left and self.x > i and board[self.y][self.x - i].type != "solid"
            right = right and self.x < len(board[self.y]) - i and board[self.y][self.x + i].type != "solid"
            # check move left
            if left and board[self.y][self.x - i].mass < self.mass:
                if type(board[self.y][self.x - i]) == Air:
                    moves.append((self.x - i, self.y))
            # check move right
            if right and board[self.y][self.x + i].mass < self.mass:
                if type(board[self.y][self.x + i]) == Air:
                    moves.append((self.x + i, self.y))

            # choose move
            if len(moves) > 0:
                shuffle(moves)
                return moves[-1]
