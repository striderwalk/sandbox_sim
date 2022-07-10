from .air import Air
from random import choice


class Gas():
    """
    a base class for all gasses
     - handle flowing
    """

    def _check_pos(self, board, x, y):
        # check if move is possible

        if type(board[y][x]) == Air:
            return True

        return False

    def flow(self, board):
        # if similer particle not on top return or on top of similer particle
        if self.y > 0  and type(board[self.y-1][self.x]) == type(self):
            if self.y < len(board)-1 and type(board[self.y+1][self.x]) != Air:
                return
        elif type(board[self.y+1][self.x]) != type(self):
            return


        left = True
        right = True

        moves = []
        for i in range(self.wetness):
            # check for stone
            left = left and self.x > i-1 and type(board[self.y][self.x-i]) in [type(self), Air]
            right = right and self.x < len(board[self.y])-i and type(board[self.y][self.x+i]) in [type(self), Air]


            # check left
            if left and self.x > i-1:
                if self._check_pos(board,self.x-i,self.y):
                    moves.append((self.x-i,self.y))


            # check right
            if right and self.x < len(board[self.y])-i:
                if self._check_pos(board,self.x+i,self.y):
                    moves.append((self.x+i,self.y))

            if len(moves) > 0:
                break
        if len(moves) > 0:
            self.moveTo(board, *choice(moves))
            return True

        return False
