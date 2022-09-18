from .particle import Particle
from .liquid import Liquid
from .smoke import Smoke
from .air import Air
from random import random, randint, choice
from colour import Color
from .properties import fire_vals


class Fire(Particle, Liquid):
    """
    move
     - random up left or right
     - else down

    burning stuff
     - wood

    on death
    - turn to smoke

    """

    base_colour = "#fc9803"
    colour = (252, 152, 3)
    colours = list(Color(base_colour).range_to(Color("#fc0b03"), 5))
    colours = [[i * 255 for i in colour.rgb] for colour in colours]
    temp = fire_vals["start_temp"]

    ### rules ###
    max_temp = fire_vals["max_temp"]
    min_temp = fire_vals["min_temp"]
    htrans_num = fire_vals["htrans_num"]

    def __init__(self, x, y, player_made=True, temp=temp):
        super().__init__(x, y, mass=-1, static=False, is_flame=True)
        self.life_lim = randint(15, 36)
        self.colour = choice(self.colours)
        self.colours = Fire.colours
        self.player_made = player_made
        self.temp = temp

    def to_solid(self):
        return "dies"

    # make sure water steams
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
                    other.fire_count += 0.2

    def update_colour(self, board):
        index = randint(0, len(self.colours) - 1)
        self.colour = self.colours[index]

    def move(self, board):
        if self.y <= 0:
            return
        moves = []
        if self.x > 0 and type(board[self.y - 1, self.x - 1]) == Air:
            moves.append((self.x - 1, self.y - 1))
        if (
            self.x < len(board[self.y]) - 1
            and type(board[self.y - 1, self.x + 1]) == Air
        ):
            moves.append((self.x + 1, self.y - 1))
        if len(moves) != 0:
            self.moveTo(board, *choice(moves))

    def update(self, board):
        # update temp
        self.update_temp(board)
        # check for wood to BURN!!
        self.check_wood(board)
        # if val := self.check_water(board):
        #     return val
        # time since created
        self.life_len += 1

        if self.life_len > self.life_lim:
            if random() > 0.9:
                return {"type": Smoke}
            else:
                return {"type": Air}

        self.update_colour(board)
        self.move(board)

        # if on celling DIE
        if self.y == 0:
            return {"type": "dies"}

        return self.check_temp()
