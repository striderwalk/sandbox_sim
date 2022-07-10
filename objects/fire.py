from .particle import Particle
from .air import Air
from .smoke import Smoke
from random import random, randint, choice
from colour import Color


class Fire(Particle):
    """
    a not acting partical 
    'ensuring' correct behavior of 
    all others   

    """


    base_colour = "#fc9803"
    colour = (252, 152, 3)
    def __init__(self, x,y, player_made=True):
        super().__init__(x, y, mass=-1, static=False)
        self.life_lim = randint(15,36)
        self.colours = list(Color(Fire.base_colour).range_to(Color("#fc0b03"), 5))
        self.colour = [i*255 for i in self.colours[0].rgb]
        self.player_made = player_made

    def check_wood(self, board):
        # import here to stop circular import
        from .wood import Wood

        for other in self.get_neighbours(board, 2):
            if type(other) == Wood:
                if self.player_made:
                    other.fire_count += 2
                else:
                    other.fire_count += .2

        
    def update_colour(self, board):
        index = randint(0, len(self.colours)-1)
        self.colour =  [i*255 for i in self.colours[index].rgb]
        


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


        # time since created
        self.life_len += 1

        if self.life_len > self.life_lim:
            if random() > 0.5: return Smoke
            else: return "dies"


        self.update_colour(board)
        self.move(board)

        # if on celling DIE
        if self.y == 0:
            if random() > 0.5: return Smoke
            else: return "dies"        



        