from .particle import Particle
from .liquid import Liquid
from .air import Air
from .steam import Steam
from .stone import Stone
from random import random, randint, choice

class Lava(Particle, Liquid):
    """
    a Partical that will fall
     - down 
     - down to the left
     - down to the left 

    will flow
    
    affects Water
     - if Below Water turn to it steam
     - if next to Water turn to it and self stone

    """

    colour = (245 , 134 , 70)
    directer = 2

    def __init__(self, x,y):
        super().__init__(x, y, mass=1)
        self.update_colour()
        self.wetness = 10

        # if -1 move self if 1 move right
        self.direct = Lava.directer
        Lava.directer *= -1

    def check_water(self, board):
        from .water import Water
        if type(board[self.y-1, self.x]) == Water and self.y != 0: # check above if not on top
            board[self.y-1, self.x] = Steam(self.x,self.y-1)
            return "dies"

        if type(board[self.y+1, self.x]) == Water: # check below 
            board[self.y+1, self.x] = Stone(self.x,self.y-1)
            return Stone
        if type(board[self.y, self.x-1]) == Water and self.x != 0: # check right if not on edge
            board[self.y, self.x-1] = Stone(self.x-1,self.y)
            return Stone
        if self.x != len(board[0])-1 and type(board[self.y, self.x+1]) == Water : # check left if not on edge
            board[self.y, self.x+1] = Stone(self.x+1,self.y)
            return Stone


    def update(self,board):
        # check if upade needed
        if self.check_self(board):
            return
            
        # flip side
        self.direct *= -1
        # time since created
        self.life_len += 1

        # check not at bottom of board
        if len(board)-1 == self.y: return

        # check for water
        if res := self.check_water(board):
            return res
        

         # update postion
        if pos := self.move(board):
            self.moveTo(board, *pos)
    






