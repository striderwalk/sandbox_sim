from .air import Air
from random import choice


class Gas():
    """
    a base class for all gasses
     - handle flowing
    """

    def flow(self, board):
        # right
        moves = []
        if self.x < len(board[self.y])-1 and type(board[self.y][self.x+1]) == Air:
            moves.append((self.x+1, self.y))
        # left
        if self.x > 0 and type(board[self.y][self.x-1]) == Air:
            moves.append((self.x-1, self.y))

        if len(moves) > 0:
            return choice(moves)

    def move(self, board):
        moves = []
        if board[self.y-1, self.x].mass > self.mass: # up
            moves.append((self.x,self.y-1))

        else:
            if self.x > 0 and board[self.y-1, self.x-1].mass > self.mass: # left
                moves.append((self.x-1,self.y-1))


            if self.x < len(board[self.y])-1 and board[self.y-1, self.x+1].mass > self.mass: # right
                moves.append((self.x+1,self.y-1))

        
        if len(moves) > 0: # pick random move
            return choice(moves)

        return False
           

