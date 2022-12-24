from random import choice, randint, random

from .air import Air
from .gas import Gas
from .particle import Particle
from .properties import fire_vals
from .smoke import Smoke
from .utils import FIRE_COLOURS


class Fire(Particle, Gas):
    """
    move
     - random up left or right
     - else down

    burning stuff
     - wood

    on death
    - turn to smoke (if the code works properly)


    """

    base_colour = "#fc9803"
    colour = (252, 152, 3)
    colours = FIRE_COLOURS
    temp = fire_vals["start_temp"]

    ### rules ###
    max_temp = fire_vals["max_temp"]
    min_temp = fire_vals["min_temp"]
    conduct = fire_vals["conduct"]
    mass = fire_vals["mass"]

    def __init__(self, x, y, player_made=True, temp=temp):
        super().__init__(x, y, mass=Fire.mass, static=False, is_flame=True)
        Gas.__init__(self)
        self.life_lim = randint(15, 36)
        self.colour = choice(self.colours)
        self.colours = Fire.colours
        self.player_made = player_made
        self.temp = temp

    def to_liquid(self):
        return "dies"

    # make sure water steams
    def check_wood(self, others):
        # import here to stop circular import
        from .wood import Wood

        for other in others:
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

    def update(self, board):
        # update temp
        others = list(self.get_others(board))
        self.update_temp(others)
        # check for wood to BURN!!
        self.check_wood(others)
        # time since created
        self.life_len += 1

        if self.life_len > self.life_lim:
            if random() > 0.99:
                return {"type": Smoke}
            else:
                return {"type": Air}

        self.update_colour(board)
        # update position
        if pos := self.move(board):
            self.moveTo(board, *pos)

        # if on celling DIE
        if self.y == 0:
            return {"type": "dies"}

        return self.check_temp()
