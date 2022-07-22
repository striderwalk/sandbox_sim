from .air import Air
import numpy as np
from random import choice


class Liquid():
    """
    a base class for all liquids
     - handle flowing
     - moving
    """

    def flow(self, board):

        left = (self.x > 0) and type(board[self.y, self.x-1]) == Air
        right = (self.x < len(board[self.y])-1) and type(board[self.y, self.x+1]) == Air
        moves = []
        for i in range(1, self.wetness):
            # check for stone
            left = left and self.x > i and type(board[self.y, self.x-i]) == Air
            right = right and self.x < len(board[self.y])-i and type(board[self.y, self.x+i]) == Air

            # check left
            if left and type(board[self.y, self.x-i]) == Air:
                moves.append((self.x-i,self.y))
            
            # check right
            if right:
                moves.append((self.x+i,self.y))
            
            
            


            if len(moves) > 0:
                return moves[0]

        return False


    def move(self, board):
        moves = []
        if board[self.y+1, self.x].mass < self.mass: # down
            moves.append((self.x,self.y+1))

        elif self.x > 0 and board[self.y+1, self.x-1].mass < self.mass: # left
            moves.append((self.x-1,self.y+1))


        elif self.x < len(board[self.y])-1 and board[self.y+1, self.x+1].mass < self.mass: # right
            moves.append((self.x+1,self.y+1))

        
        if len(moves) != 0: # pick random move
            return choice(moves)

        return False