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
        - move down left/ down right
        - move left/ right
        """

        up = self.y > 0 



        moves = []
        for i in range(1, self.wetness):
            left = self.x > i-1 
            right = self.x < len(board[self.y])-i
            # check move down left
            if up  and left and board[self.y-1][self.x-i].mass > self.mass:
                if type(board[self.y][self.x-i]) == Air:
                    moves.append((self.x-i, self.y-1))
            # check move down right
            if up and right and board[self.y-1][self.x+i].mass > self.mass:
                if type(board[self.y][self.x+i]) == Air:
                    moves.append((self.x+i, self.y-1))
            # check move left
            if left and board[self.y][self.x-i].mass > self.mass:
                moves.append((self.x-i, self.y))

            # check move right
            if right and board[self.y][self.x+i].mass > self.mass:
                moves.append((self.x+i, self.y))
                
            # choose move 
            if len(moves) > 0: 
                shuffle(moves)
                return moves[-1]


