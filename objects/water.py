from .particle import Particle
from .steam import Steam
from .stone import Stone
from .air import Air
from .liquid import Liquid

from random import random, randint, choice

class Water(Particle, Liquid):
    """
    a Partical that will fall
     - down 
     - down to the left
     - down to the left
    will pool
     - when only above water
    changed by lava
     - if above Lava turn to steam
     - if next to Lava turn to stone

    """

    colour = (64, 154, 245)

    def __init__(self, x,y):
        super().__init__(x, y, mass=1)
        self.update_colour()
        self.wetness = 6 

    def check_lava(self, board):
        # import here to avoid circular impor
        from .lava import Lava
        # check for lava
        if type(board[self.y+1][self.x]) == Lava: # check below 
            return Steam 
        if self.y > 0 and type(board[self.y-1][self.x]) == Lava: # check above if not on top
            board[self.y-1][self.x] = Stone(self.x,self.y-1)
            self_change = True
        if self.x > 0 and type(board[self.y][self.x-1]) == Lava: # check right if not on edge
            board[self.y][self.x-1] = Stone(self.x-1,self.y)
            self_change = True
        if self.x < len(board)-1 and type(board[self.y][self.x+1]) == Lava: # check left if not on edge
            board[self.y][self.x+1] = Stone(self.x+1,self.y)
            self_change = True
        if "self_change" in locals():
            return Stone
            

    def move(self, board):
        moves = []
        if board[self.y+1][self.x].mass < self.mass:
            moves.append((self.x,self.y+1))
        elif self.x !=0 and board[self.y+1][self.x-1].mass < self.mass:
            moves.append((self.x-1,self.y+1))
        elif self.x < len(board)-1 and board[self.y+1][self.x+1].mass < self.mass == None:
            moves.append((self.x+1,self.y+1))
        
        if len(moves) != 0:
            self.moveTo(board, *choice(moves))

    def update(self,board):
        # time since created
        self.life_len += 1
        
        # check not at bottom of board
        if self.y == len(board)-1: return
        # check for lava
        if res := self.check_lava(board):
            return res
        # update postion
        self.move(board)
        # flow
        self.flow(board)        
