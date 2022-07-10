from random import randint
from math import sqrt

class Particle:
    """
    base class for all particles
     - stores pos
     - allows movement
     - find colour
     - find neigbours
    """


    def __init__(self, x,y, mass = 0, static=False):
        self.x = x
        self.y = y
        self.count = 0
        self.mass = mass
        self.life_len = 0
        self.static = static

        
    def update_colour(self):
        self.colour = tuple(type(self).colour)
        r = (self.colour[0] + randint(-5, 5)) % 255

        g = (self.colour[1] + randint(-5, 5)) % 255
        b = (self.colour[2] + randint(-5, 5)) % 255
        self.colour = (r, g, b)
    
       
    

    def get_neighbours(self, board, xdis, ydis=-1) -> list:
        # find all neigbours in box(xrange, yrange) -> [vals]
        # both ranges are ± from self.pos 
        if ydis < 0: ydis = xdis
        # faster that get_neighbours but not circle :(
        neighbours = []
        for i in range(ydis+1):
            for j in range(xdis+1):
                # avoid self
                if i+j == 0:
                     continue
                # will check self gets removed later

                # all cases
                if self.y > i-1 and self.x > j: # up left
                    neighbours.append(board[self.y-i][self.x-j])
                if self.y > i-1 and self.x < len(board[self.y])-j: # up right
                    neighbours.append(board[self.y-i][self.x+j])
                if self.y < len(board)-i and self.x > j: # down left
                    neighbours.append(board[self.y+i][self.x-j])
                if self.y < len(board)-i  and self.x < len(board[self.y])-j:# down right
                    neighbours.append(board[self.y+i][self.x+j])
        return neighbours

   

    def moveTo(self, board, x,y):
        # to not move stone/wood
        if board[y][x].static == True: return
        # update others pos
        board[y][x].x = self.x
        board[y][x].y = self.y
        # swap pos
        board[self.y][self.x], board[y][x] = board[y][x], board[self.y][self.x]
        # set self pos
        self.x = x
        self.y = y

    def __repr__(self): return f"{type(self).__name__} at {self.x}, {self.y}"# with mass of {self.mass}"
    
