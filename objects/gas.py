from .air import Air
from random import choice, random, shuffle, randint


class Gas():
    """
    a base class for all gasses
     - handle flowing
     - spreding
    """
    def copy(self,board):
        if self.thickness <=1: return
        split_ratio = random()
        # check 3 rand pos
        for _ in range(3):
            xoff = randint(-2,3)
            yoff = randint(-2,3)
            # so if pos out of board no
            if 0 <= self.y+yoff < len(board) and 0 <= self.x+xoff < len(board[0]):

                if type(board[self.y+yoff, self.x+xoff]) == Air:
                    board[self.y+yoff, self.x+xoff] = type(self)(self.x+xoff,self.y+yoff,self.thickness*split_ratio)
                self.thickness *= 1-split_ratio
                return


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


