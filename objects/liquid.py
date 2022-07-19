from .air import Air
import numpy as np
from random import choice


class Liquid():
    """
    a base class for all liquids
     - handle flowing
    """

    def _check_pos(self, board, x, y):
        # check if move is possible

        if type(board[y, x]) == Air:
            return True

        return False

    def flow(self, board):
        # if similer particle not on top return or on top of similer particle

        left = (self.direct == -1) and (self.x > 0) and (type(board[self.y, self.x-1]) in [type(self), Air])
        right = (self.direct == 1) and (self.x < len(board[self.y])-1) and (type(board[self.y, self.x+1]) in [type(self), Air])

        moves = []
        for i in range(1, self.wetness):
            # check for stone
            left = left and self.x > i and type(board[self.y, self.x-i]) in [type(self), Air]
            right = right and self.x < len(board[self.y])-i and type(board[self.y, self.x+i]) in [type(self), Air]

            # check right
            if right and self._check_pos(board,self.x+i,self.y):
                    moves.append((self.x+i,self.y))
            
            # check left
            if left and self._check_pos(board,self.x-i,self.y):
                    moves.append((self.x-i,self.y))


            if len(moves) > 0:
                return moves[0]

        return False


    def move(self, board):
        moves = []
        if board[self.y+1, self.x].mass < self.mass: # down
            if self._check_pos(board, self.x, self.y+1):
                moves.append((self.x,self.y+1))

        elif self.x > 0 and board[self.y+1, self.x-1].mass < self.mass: # left
            if self._check_pos(board, self.x-1, self.y+1):
                moves.append((self.x-1,self.y+1))

        elif self.x < len(board[self.y])-1 and board[self.y+1, self.x+1].mass < self.mass: # right
            if self._check_pos(board, self.x+1, self.y+1):
                moves.append((self.x+1,self.y+1))
        
        if len(moves) != 0: # pick random move
            return choice(moves)

        return False