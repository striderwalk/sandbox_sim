from .utils import find_heatmap_colour, update_colour

THRESH_HOLD = 1


class Particle:
    """
    base class for all particles
     - does to much
    """

    # USE **KWARGS NOW
    def __init__(self, x, y, mass=0, static=False, flamable=False, is_flame=False, health=100, obj=None):  # USE **KWARGS
        # USE **KWARGS DO IT
        # MAYBE DON'T ITS KINNA HARD JUST GET RID OF KWARGS
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
            self.next_temp = self.__class__.temp

        self.colour = update_colour(self.__class__.colour)

    @property
    def pos(self):
        return self.x, self.y

    @property
    def temp_colour(self):
        if self.temp + 100 < 0:
            colour = (0, 0, 0)
        else:
            colour = find_heatmap_colour(self.temp)

        return colour

    def get_others(self, board):
        others = []
        if self.y > 0:  # above
            others.append(board[self.y - 1, self.x])

        if self.y < len(board) - 1:  # below
            others.append(board[self.y + 1, self.x])

        if self.x > 0:  # left
            others.append(board[self.y, self.x - 1])

        if self.x < len(board[self.y]) - 1:  # right
            others.append(board[self.y, self.x + 1])
        
        return others


    

    def update_temp(self, others):
        # profiler.start()
        # find neigbours
        # include self in average

        total = 0
        if all(abs(i.temp - self.temp) <= THRESH_HOLD for i in others):
            return

        temp = 0
        for other in others:
            # can't use isstance here because can't import fountain
            if other.__class__.__name__ == "Fountain":
                continue
            else:
                conduct = other.__class__.conduct * other.__class__.mass

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
        return f"{self.__class__.__name__} mass={self.mass} temp={self.temp} health={self.health} pos={self.x},{self.y}"
