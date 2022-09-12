import pygame
import logging
import numpy as np
from random import randint
from .objects import Stone, Air
from .objects.fountain import Fountain
from conts import ROWS, COLS, CELL_WIDTH, CELL_HEIGHT
from .get_particles import particles


def get_profiling_board():
    # i don't like this code but done care enough to fix it
    np.array([[Air(x, y) for x in range(COLS)] for y in range(ROWS)])
    step = COLS // len(particles)
    index_d = 0
    for i in range(ROWS):
        for j in range(COLS):
            index_d = j // step
            if j % step < 2:
                self.add_particle(j, i, Stone, health=100000)
                continue
            try:
                self.add_particle(j, i, particles[index_d])
            except IndexError:
                pass
    #######################################################


class Box:
    """
    a container for all particles
    use for
    - updating
    - moving
    - drawing
    - adding new particles
    """

    def __init__(self, board_data):
        # setup board
        if type(board_data) != str: # loaded board from file
            self.board = board_data
            if not np.array_equal(self.board,self.board[:ROWS, :COLS]):
                logging.warning("board sized incorrectly resizing")
                self.board = self.board[:ROWS, :COLS]
        elif board_data == "empty": # no board
            self.board = np.array(
                [[Air(x, y) for x in range(COLS)] for y in range(ROWS)]
            )
            logging.info("created empty board")

        elif board_data == "profiling": # setup for profiling
            self.board = get_profiling_board()
            logging.info("profile board made")



    def draw_particles(self, win, show_temp=False, show_fountain=True):
        # draw all particles
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                # if air not dawn to save time
                if not show_temp:
                    options = [Fountain, Air]
                else:
                    options = [Fountain]
                if type(val) not in options:
                    if show_temp:
                        colour = val.temp_colour
                    else:
                        colour = val.colour 
                    try:
                        pygame.draw.rect(
                            win,
                            colour,
                            [j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT],
                        )
                    except ValueError as e:
                        print(val)
                        raise e
                elif type(val) == Fountain:
                    if show_fountain:
                        colour = val.colour
                    else:
                        colour = val.obj.colour

                    pygame.draw.rect(
                        win,
                        colour,
                        [j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT],
                    )

    def add_particle(
        self, x, y, obj, *, strict=False, place_obj=None, health=10
    ) -> None:
        if obj not in particles and obj != Fountain:
            raise TypeError(f"add_particle ask to place invalid particle {obj}")

        # add particle to board
        # strict mean not replace non air
        if strict and type(self.board[y, x]) != Air:
            return

        if obj == Fountain:
            self.board[y, x] = obj(x, y, place_obj)
        elif obj == Stone:
            self.board[y, x] = obj(x, y, health)

        else:
            self.board[y, x] = obj(x, y)

    def update(self, win, fnum, pause, show_temp, show_fountain=True ):
        # DRAW THINGS!!!!
        self.draw_particles(win, show_temp, show_fountain)
        if pause:
            return

        # update board for heavy things
        for row in self.board[::-1]:
            for item in row:
                if item.count != fnum and item.mass > 0:  # if fnum same already updated

                     # check for death in particle
                    if (result := item.update(self.board)) is None:
                        pass
                    elif result["type"] == "dies":
                        item.load_move(self.board)
                        self.board[item.y, item.x] = Air(item.x, item.y)
                    # if particle wants to go though a major change
                    elif result["type"] is not None:
                        self.board[item.y, item.x] = result["type"](item.x, item.y, temp=result["temp"]) 
                    # update count
                    self.board[item.y, item.x].count = fnum
            # move items
            for item in row[::2]:
                item.load_move(self.board)
            # move items
            for item in row[1::2]:
                item.load_move(self.board)

        # update board for other things
        for row in self.board:
            for item in row:
                if item.count != fnum and item.mass <= 0:  # if fnum same already updated

                    # check for death in particle
                    if (result := item.update(self.board)) is None:
                        pass
                    elif result["type"] == "dies":
                        item.load_move(self.board)
                        self.board[item.y, item.x] = Air(item.x, item.y)
                    # if particle wants to go though a major change
                    elif result:
                        self.board[item.y, item.x] = result["type"](item.x, item.y, temp=result["temp"])

                    # update count
                    self.board[item.y, item.x].count = fnum

            # move items
            for item in row[::2]:
                item.load_move(self.board)
            # move items
            for item in row[1::2]:
                item.load_move(self.board)

        # self.fix()

    def debug(self) -> list:
        # return No. of particles
        vals = {}
        for i in particles:
            vals[i.__name__] = 0

        for row in self.board:
            for thing in row:
                vals[type(thing).__name__] = vals[type(thing).__name__] + 1

        return vals

    def fix(self) -> None:
        # tell each particle where there are
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if type(item) == Air:
                    continue
                if item.y != y or item.x != x:
                    logging.warning(f"{item=} pos needed fixing to {x=}, {y=}")
                item.x = x
                item.y = y
                item.load = None

    def rain_type(self, obj, num=1500) -> None:
        for _ in range(num):
            y, x = randint(0, ROWS - 1), randint(0, COLS - 1)
            self.add_particle(x, y, obj)

    def reset(self):
        logging.info("reseting board")
        self.board = np.array([[Air(x, y) for x in range(COLS)] for y in range(ROWS)])
