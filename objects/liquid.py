from .air import Air
import numpy as np
from random import choice, shuffle, random


class Liquid():
    """
    a base class for all liquids
     - handle flowing
     - moving
    """

    def move(self, board):
        """
        - first move down
        - move down left/ right
        - move left/ right
        """

        down = self.y < len(board)-1 

        # check move down
        if down  and board[self.y+1][self.x].mass < self.mass:
            return (self.x, self.y+1)

        moves = []
        for i in range(1, self.wetness):
            left = self.x > i-1 
            right = self.x < len(board[self.y])-i
            # check move down left
            if down  and left and board[self.y+1][self.x-i].mass < self.mass:
                if type(board[self.y][self.x-i]) == Air:
                    moves.append((self.x-i, self.y+1))
            # check move down right
            if down and right and board[self.y+1][self.x+i].mass < self.mass:
                if type(board[self.y][self.x+i]) == Air:
                    moves.append((self.x+i, self.y+1))
            # check move left
            if left and board[self.y][self.x-i].mass < self.mass:
                moves.append((self.x-i, self.y))

            # check move right
            if right and board[self.y][self.x+i].mass < self.mass:
                moves.append((self.x+i, self.y))
                
            # choose move 
            if len(moves) > 0: 
                shuffle(moves)
                return moves[-1]