from .particle import Particle
from .steam import Steam
from .stone import Stone
from .air import Air
from .lava import Lava
from .liquid import Liquid
import time

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
    directer = 1

    def __init__(self, x,y):
        super().__init__(x, y, mass=1)
        self.update_colour()
        self.wetness = 6
        # if -1 move self if 1 move right
        self.direct = Water.directer
        Water.directer *= -1



    def check_lava(self, board):
        # check for lava
        if type(board[self.y+1][self.x]) == Lava: # check below 
            return Steam 
        if type(board[self.y-1][self.x])== Lava: # check above if not on top
            board[self.y-1][self.x] = Stone(self.x,self.y-1)
            return Stone 
        if self.x !=0 and type(board[self.y][self.x-1])== Lava: # check right if not on edge
            board[self.y][self.x-1] = Stone(self.x-1,self.y)
            return Stone 
        if self.x < len(board)-1 and type(board[self.y][self.x+1])== Lava: # check left if not on edge
            board[self.y][self.x+1] = Stone(self.x+1,self.y)
            return Stone         

    def update(self,board):
        # swich direction
        self.direct *= -1
        # time since created
        self.life_len += 1
        
        # check not at bottom of board
        if self.y == len(board)-1: return
        # check for lava
        if res := self.check_lava(board):
            return res
        # update postion
        if (pos := self.move(board)):
            print("move")
            self.moveTo(board, *pos)
        # flow
        elif (pos := self.flow(board)):
            print("flow")
            self.moveTo(board, *pos)      
