import logging
from random import randint

import numpy as np

import errors
from conts import COLS, ROWS

from .get_particles import particles
from .objects import Air, Stone
from .objects.barrier import Barrier
from .objects.fountain import Fountain


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
        if type(board_data) != str:  # loaded board from file
            self.board = board_data
            if len(self.board) != ROWS or len(self.board[0]) != COLS:
                logging.warning("board sized incorrectly resizing")
                self.scale_board()
        elif board_data == "empty":  # no board
            self.board = make_empty()
            logging.info("created empty board")

        elif board_data == "profiling":  # setup for profiling

            self.set_profiling_board()
            logging.info("profile board made")
        else:
            raise errors.InvalidBoard(board_data)

    def scale_board(self):
        """resize saved board to fit board size"""

        # check if board is to small
        row_len = len(self.board)
        col_len = len(self.board[0])

        if row_len < ROWS:
            diff = ROWS - row_len
            adder = [[Air(0, 0) for i in range(col_len)] for _ in range(diff)]
            self.board = np.append(self.board, adder, 0)

        elif row_len > ROWS:
            self.board = self.board[:ROWS, :]

        if col_len < COLS:
            diff = COLS - col_len
            adder = [[Air(0, 0) for i in range(diff)] for _ in range(ROWS)]
            self.board = np.append(self.board, adder, 1)

        elif col_len > COLS:
            self.board = self.board[:COLS, :]

        logging.info(f"resized board of size {row_len}x{col_len} to {ROWS}x{COLS}")
        self.fix(talk=False)

    def set_profiling_board(self):
        # i don't like this code but done care enough to fix it
        self.board = np.array([[Air(x, y) for x in range(COLS)] for y in range(ROWS)])
        step = COLS // len(particles)
        index_d = 0
        for i in range(ROWS):
            index_d = self.set_profiling_row(step, i, index_d)

    def set_profiling_row(self, step, i, index_d):
        for j in range(COLS):
            index_d = j // step
            if j % step < 2:
                self.add_particle(j, i, Barrier)
                continue
            if index_d < len(particles) and index_d > 0:
                self.add_particle(j, i, particles[index_d])

        return index_d

    def add_particle(self, x, y, obj, *, strict=False, place_obj=None, health=10):
        """
        add a particle a point (x,y)
        - strict means only replace Air
        - I don't know what the rest do
        """

        if obj not in particles and obj not in [Fountain, Barrier]:
            raise errors.InvalidParticle(obj)

        # add particle to board
        # strict means only resplace Air
        if strict and type(self.board[y, x]) != Air:
            return

        if obj == Fountain:
            self.board[y, x] = obj(x, y, place_obj)
        elif obj == Stone:
            self.board[y, x] = obj(x, y, health)

        else:
            self.board[y, x] = obj(x, y)

    def press(self, size, x, y, obj, keep=False, place_obj=None):
        """
        handle mouse press
        - keep means only replace Air
        """

        # set mouse pos to obj
        if obj == Fountain:
            self.add_particle(x, y, obj, strict=keep, place_obj=place_obj)
        else:
            self.add_particle(x, y, obj, strict=keep)

        # set neighbours
        cell = self.board[y, x]
        for _, other in cell.get_neighbours(self.board, size):
            pos = (other.x, other.y)
            if obj == Fountain:
                self.add_particle(*pos, obj, strict=keep, place_obj=place_obj)
            else:
                self.add_particle(*pos, obj, strict=keep)

    def update_row(self, row, types: tuple[str]) -> None:
        """
        update a single row in 2 passes to prevent some movement bias
        """
        for item in row:
            # check if type can be updated
            if item.type not in types:
                continue

            # update item
            if (result := item.update(self.board)) is None:
                continue
            # check for death in particle
            elif result["type"] == "dies":
                item.load_move(self.board)
                self.board[item.y, item.x] = Air(item.x, item.y, temp=item.next_temp)
            # if particle wants to go though a major change
            elif result["type"] is not None:
                obj = result["type"]
                self.board[item.y, item.x] = obj(item.x, item.y, temp=item.next_temp)

        # move items
        for item in row[::2]:
            item.load_move(self.board)
        # move items
        for item in row[1::2]:
            item.load_move(self.board)

    def update(self):
        """
        upadate board in 2 passes to prevent spredding
        """
        # update board
        for row in self.board[::-1]:
            self.update_row(row, ["solid", "liquid"])

        for row in self.board:
            self.update_row(row, ["gas"])

    def debug(self) -> list:
        """get list of particle counts"""

        vals = {}
        for i in particles:
            vals[i.__name__] = 0

        for row in self.board:
            for thing in row:
                vals[type(thing).__name__] = vals[type(thing).__name__] + 1

        return vals

    def fix(self, talk=True) -> None:
        """fix a load of stupid bugs"""
        logging.warning("there is a stuid bug")
        # tell each particle where there areq
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if type(item) == Air:
                    continue
                if item.y != y or item.x != x and talk:
                    logging.warning(f"{item=} pos needed fixing to {x=}, {y=}")
                item.x = x
                item.y = y
                item.load = None

    def heat_cells(self, mouse_pos, change_temp, size):
        # check for invaild pos
        if not mouse_pos:
            return None
        x, y = mouse_pos
        if 0 > y or y > ROWS or 0 > x or x > COLS:
            logging.warning(f"box cords {x=},{y=} from mouse not vaild")
            return

        for _, other in self.board[y][x].get_neighbours(self.board, size):
            if isinstance(other, Fountain):
                continue

            # check for correct temp range
            cool = other.temp < type(other).max_temp
            warm = other.temp > type(other).min_temp
            if cool and warm:
                other.temp += change_temp

    def rain_type(self, obj, num=1500) -> None:
        for _ in range(num):
            y, x = randint(0, ROWS - 1), randint(0, COLS - 1)
            self.add_particle(x, y, obj)

    def reset(self):
        """does this need a docstring?"""
        logging.info("reseting board")
        self.board = np.array([[Air(x, y) for x in range(COLS)] for y in range(ROWS)])


def make_empty():
    return np.array([[Air(x, y) for x in range(COLS)] for y in range(ROWS)])
