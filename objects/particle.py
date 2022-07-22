from random import randint
import numpy as np

class Particle:
    """
    base class for all particles
     - stores pos
     - allows movement
     - find colour
     - find neigbours
    """

    i_d = 0
    def __init__(self, x,y, mass = 0, static=False, flamable=False):
        self.x = x
        self.y = y
        self.count = 0
        self.mass = mass
        self.life_len = 0
        self.static = static
        self.flamable = flamable
        self.i_d = Particle.i_d
        Particle.i_d += 1

    def choice(self, options):
        probs = [1/len(options) for _ in options]
        x = np.random.rand()
        cum = 0
        for i,p in enumerate(probs):
            cum += p
            if x < cum:
                break
        return options[i]
        
    def update_colour(self):
        self.colour = tuple(type(self).colour)
        r = (self.colour[0] + randint(-5, 5)) % 255

        g = (self.colour[1] + randint(-5, 5)) % 255
        b = (self.colour[2] + randint(-5, 5)) % 255
        self.colour = (r, g, b)
    
       
    

    def get_neighbours(self, board, dis) -> list:
        # find all neigbours in box(dis, dis) -> [vals]
        # both ranges are ± from self.pos 
        # fast but not circle :(

        # find box x
        minx = max(0, self.x-dis+1)
        miny = max(0, self.y-dis+1)
        
        # find box y
        maxx = min(len(board[0]), self.x+dis)
        maxy = min(len(board), self.y+dis)

        others = []
        # go though le box
        for y in range(miny, maxy):
            for x in range(minx, maxx):
                others.append(((x,y), board[y, x]))

        return others
                
    def moveTo(self, board, x,y):
        # to not move stone/wood
        if board[y, x].static == True: return
        # update others pos
        board[y, x].x = self.x
        board[y, x].y = self.y
        # swap pos
        board[self.y, self.x], board[y, x] = board[y, x], board[self.y, self.x]
        # set self pos
        self.x = x
        self.y = y


    def check_self(self,board):
        if self.y > 0 and type(board[self.y-1, self.x]) != type(self):
            return False
        if self.x > 0 and type(board[self.y, self.x-1]) != type(self):
            return False
        if self.y < len(board)-1 and type(board[self.y+1, self.x]) != type(self):
            return False
        if self.x < len(board[self.y])-1  and type(board[self.y, self.x+1]) != type(self):
            return False



    def __repr__(self): return f"{type(self).__name__}{self.i_d} at {self.x}, {self.y}"# with mass of {self.mass}"
    
