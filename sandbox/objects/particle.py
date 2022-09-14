from random import randint
import numpy as np
from colour import Color
import logging

HEAT_MAP = list(Color("#0000ff").range_to(Color("#ff0000"), 501))
HEAT_MAP = [[i * 255 for i in colour.rgb] for colour in HEAT_MAP]

    

class Particle:
    """
    base class for all particles
     - stores pos
     - allows movement
     - find colour
     - find neighbours
    """

    def __init__(self, x, y, mass=0, static=False, flamable=False, is_flame=False, health=100, obj=None):
        self.x = x
        self.y = y
        self.mass = mass
        self.static = static
        self.flamable = flamable
        # is_flame can be property
        if "is_flame" not in dir(self):
            self.is_flame = is_flame
        self.health = health
        if not hasattr(self, "type"):
            self.type = "None"

        self.load = None
        self.count = 0
        self.life_len = 0
        if obj is not None:
             self.next_temp = obj.temp
        else:
            self.next_temp = type(self).temp

    @property
    def temp_colour(self):
        try:
            colour = HEAT_MAP[int(min(500, self.temp+100))]
        except IndexError as e:
            logging.critical(f"{type(self).__name__} at temp of {self.temp}")
            raise e

        return colour

    def choice(self, options):
        probs = [1 / len(options) for _ in options]
        x = np.random.rand()
        cum = 0
        for i, p in enumerate(probs):
            cum += p
            if x < cum:
                break
        return options[i]


    def update_temp(self, board):
        if self.is_flame:
            self.next_temp = 0# self.temp * 0.7
        else:
            self.next_temp = 0
        # find neigbours 
        others = [] # include self in avage
        total = 1
        if self.y > 0: # above
            other = board[self.y-1][self.x]
            others.append(other)

        if self.y < len(board)-1: # below
            other = board[self.y+1][self.x]
            others.append(other)

        if self.x >= 0: # left 
            other = board[self.y][self.x-1]
            others.append(other)

        if self.x < len(board[self.y])-1: # right
            other = board[self.y][self.x+1]
            others.append(other)

        temp = 0
        for other in others:
            if type(other).__name__ != "Fountain":
                htrans_num = type(other).htrans_num**2
            else:
                htrans_num = other.obj.htrans_num**2

            temp += other.temp*htrans_num
            total += htrans_num

        temp += self.temp
        total += 1/4

        self.next_temp += temp / total


    def update_colour(self):
        # randomly change rbg colour values
        self.colour = tuple(type(self).colour)
        r = (self.colour[0] + randint(-5, 5)) % 255

        g = (self.colour[1] + randint(-5, 5)) % 255
        b = (self.colour[2] + randint(-5, 5)) % 255
        self.colour = (r, g, b)

    def get_neighbours(self, board, dis) -> list:
        # THIS IS SLOW DO NOT USE IN UPDATES
        # find all neighbours in box(dis, dis) -> [others]
        # both ranges are ± from self.pos
        # fast but not circle :(

        # find box x
        minx = max(0, self.x - dis + 1)
        miny = max(0, self.y - dis + 1)

        # find box y
        maxx = min(len(board[0]), self.x + dis)
        maxy = min(len(board), self.y + dis)

        others = []
        # go though le box
        for y in range(miny, maxy):
            for x in range(minx, maxx):
                others.append(((x, y), board[y, x]))

        return others

    def moveTo(self, board, x, y):
        self.load = x, y

    def load_move(self, board):
        self.temp = self.next_temp
        if not self.load:
            return
        x, y = self.load

        # update others pos
        board[y, x].x = self.x
        board[y, x].y = self.y
        # swap pos
        board[self.y, self.x], board[y, x] = board[y, x], board[self.y, self.x]
        # set self pos
        self.x = x
        self.y = y
        self.load = None

    def check_self(self, board):
        if self.y > 0 and type(board[self.y - 1, self.x]) != type(self):
            return False
        if self.x > 0 and type(board[self.y, self.x - 1]) != type(self):
            return False
        if self.y < len(board) - 1 and type(board[self.y + 1, self.x]) != type(self):
            return False
        if self.x < len(board[self.y]) - 1 and type(board[self.y, self.x + 1]) != type(
            self
        ):
            return False

    def __repr__(self):
        return f"{type(self).__name__} of mass {self.mass} and temp {self.temp} at {self.x}, {self.y}"
