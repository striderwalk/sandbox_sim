from .air import Air
from random import choice


class Gas():
    """
    a base class for all gasses
     - handle flowing
    """

    def flow(self, board):
        # if similer particle not on top return or on top of similer particle
        if self.y > 0  and type(board[self.y-1, self.x]) == type(self):
            if self.y < len(board)-1 and type(board[self.y+1, self.x]) != Air:
                return
        elif self.y < len(board)-1 and  type(board[self.y+1, self.x]) != type(self):
            return


        left = True
        right = True

        moves = []
        for i in range(self.wetness):
            # check for stone
            left = left and self.x > i-1 and type(board[self.y, self.x-i]) in [type(self), Air]
            right = right and self.x < len(board[self.y])-i and type(board[self.y, self.x+i]) in [type(self), Air]


            # check left
            if left and self.x > i-1:
                if type(board[self.y, self.x-i]) == Air:
                    moves.append((self.x-i,self.y))


            # check right
            if right and self.x < len(board[self.y])-i:
                if type(board[self.y, self.x+i]) == Air:
                    moves.append((self.x+i,self.y))

            if len(moves) > 0:
                break

        if len(moves) > 0:
            self.moveTo(board, *choice(moves))
            return True

        return False


    def move(self, board):
        if self.y <= 0:
            return
        moves = []
        if self.x > 0:
            moves.append((self.x-1, self.y-1))      
        if self.x < len(board[self.y])-1:
            moves.append((self.x+1, self.y-1))
        if len(moves) != 0:
            self.moveTo(board, *choice(moves))

