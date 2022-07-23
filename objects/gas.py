from .air import Air
from random import choice, random, shuffle


class Gas():
    """
    a base class for all gasses
     - handle flowing
    """

    def move(self, board):
        """
        - first move down
        - move down left/ right
        - move left/ right
        """

        # check not at top
        if self.y <= 0: return

        moves = []


        # check move down
        if board[self.y-1][self.x].mass > self.mass:
            moves.append((self.x, self.y-1))
        # check move down right
        if self.x < len(board[self.y])-1 and board[self.y-1][self.x+1].mass > self.mass:
            if type(board[self.y][self.x+1]) == Air:
                moves.append((self.x+1, self.y-1))
        # check move down left
        if self.x > 0 and board[self.y-1][self.x-1].mass > self.mass:
            if type(board[self.y][self.x-1]) == Air:
                moves.append((self.x-1, self.y-1))
        # check move right
        if self.x < len(board[self.y])-1 and board[self.y][self.x+1].mass > self.mass:
            moves.append((self.x+1, self.y))
        # check move left
        if self.x > 0 and board[self.y][self.x-1].mass > self.mass:
            moves.append((self.x-1, self.y))

        # choose move
        if len(moves) > 0: 
            shuffle(moves)
            return moves[-1]


