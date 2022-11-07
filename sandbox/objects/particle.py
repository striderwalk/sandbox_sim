import numpy as np
from colour import Color
from .utils import update_colour

HEAT_MAP = list(Color("#0000ff").range_to(Color("#ff0000"), 501))
HEAT_MAP = [[i * 255 for i in colour.rgb] for colour in HEAT_MAP]
THRESH_HOLD = 1


class Particle:
    """
    base class for all particles
     - stores pos
     - allows movement
    """

    # USE **KWARGS NOW
    def __init__(
        self,
        x,
        y,
        mass=0,
        static=False,
        flamable=False,
        is_flame=False,
        health=100,
        obj=None,
    ):  # USE **KWARGS
        # USE **KWARGS DO IT
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

        self.colour = update_colour(type(self).colour)

    @property
    def pos(self):
        return self.x, self.y

    @property
    def temp_colour(self):
        if self.temp + 100 < 0:
            colour = (0, 0, 0)
        else:
            colour = HEAT_MAP[int(min(500, self.temp + 100))]

        return colour

    def get_others(self, board):
        if self.y > 0:  # above
            yield board[self.y - 1, self.x]
            # others.append(other)

        if self.y < len(board) - 1:  # below
            yield board[self.y + 1, self.x]
            # others.append(other)

        if self.x > 0:  # left
            yield board[self.y, self.x - 1]
            # others.append(other)

        if self.x < len(board[self.y]) - 1:  # right
            yield board[self.y, self.x + 1]
            # others.append(other)

    def update_temp(self, board):
        # profiler.start()
        # find neigbours
        # include self in average
        others = list(self.get_others(board))
        total = 0

        if all(abs(i.temp - self.temp) <= THRESH_HOLD for i in others):
            return

        temp = 0
        for other in others:
            if type(other).__name__ == "Fountain":
                continue
            # elif other.type == "solid" and type(self) == type(other):
            #     conduct = 1
            # elif abs(self.temp - other.temp) > 20 and type(other).conduct < 1:
            #     conduct = 1
            else:
                conduct = type(other).conduct * type(other).mass

            temp += other.temp * conduct
            total += conduct

        temp += self.temp
        total += 1

        self.next_temp = temp / total

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
        if not board[y][x].static:
            self.load = x, y

    def load_move(self, board):
        # set current temp to next
        self.temp = self.next_temp

        # check for a move
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

    def __repr__(self):
        return f"{type(self).__name__} mass={self.mass} temp={self.temp} health={self.health} pos={self.x},{self.y}"
