from .particle import Particle
from .air import Air
from .water import Water
from .smoke import Smoke
from .steam import Steam
from random import random, randint, choice
from colour import Color


class Fire(Particle):
    """
    move
     - random up left or right
     - else down

    buring stuff
     - wood
    
    dieding
    - turn to smoke

    """


    base_colour = "#fc9803"
    colour = (252, 152, 3)
    colours = list(Color(base_colour).range_to(Color("#fc0b03"), 5))
    colours = [[i*255 for i in colour.rgb] for colour in colours]

    def __init__(self, x,y, player_made=True):
        super().__init__(x, y, mass=-1, static=False, flamable=True)
        self.life_lim = randint(15,36)
        self.colour = choice(self.colours)
        self.colours = Fire.colours
        self.player_made = player_made

    def check_water(self, board):
        # check for water
        if self.y < len(board)-1 and type(board[self.y+1][self.x]) == Water: # check below 
            return Steam 
        if type(board[self.y-1][self.x]) == Water: # check above if not on top
            return Steam 
        if self.x !=0 and type(board[self.y][self.x-1]) == Water: # check right if not on edge
            return Steam 
        if self.x < len(board)-1 and type(board[self.y][self.x+1]) == Water: # check left if not on edge
            return Steam


    def check_wood(self, board):
        # import here to stop circular import
        from .wood import Wood

        for _, other in self.get_neighbours(board, 2):
            if type(other) == Wood:
                if other.fire_count > 0:
                    break
                elif self.player_made:
                    other.fire_count += 2
                else:
                    other.fire_count += .2

        
    def update_colour(self, board):
        index = randint(0, len(self.colours)-1)
        self.colour = self.colours[index]
        


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


    def update(self,board):
        # check for wood to BURN!!
        self.check_wood(board)
        if (val := self.check_water(board)):
            return val
        # time since created
        self.life_len += 1

        if self.life_len > self.life_lim:
            if random() > 0.5: return Smoke
            else: return "dies"

        self.update_colour(board)
        self.move(board)


        # if on celling DIE
        if self.y == 0:
            if random() > 0.7:
                return Smoke
            else:
                return "dies"        



        