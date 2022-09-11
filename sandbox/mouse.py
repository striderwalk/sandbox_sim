import pygame
from .objects.fountain import Fountain
from .objects import Air
from .get_particles import particles
from conts import (
    CELL_WIDTH,
    CELL_HEIGHT,
    ROWS,
    HEIGHT,
    LOWER_BOARDER,
)

MAX_SIZE = 20


class Mouse:
    """
    handle cursor
     - clicks
     - drawing
    """

    def __init__(self, size=3):
        self.size = size

    def scale(self, num):
        # find new size
        new = self.size + num

        if new > 0 and new < MAX_SIZE:
            self.size = new

    def press(self, board, x, y, obj, *, keep=False, place_obj=None):
        # if keep only replace Air
        # set mouse pos to obj

        if obj == Fountain:
            board.add_particle(x, y, obj, strict=keep, place_obj=place_obj)
        else:
            board.add_particle(x, y, obj, strict=keep)

        # set neighbours
        for _, other in board.board[y][x].get_neighbours(board.board, self.size):
            if obj == Fountain:
                board.add_particle(
                    other.x, other.y, obj, strict=keep, place_obj=place_obj
                )
            else:
                board.add_particle(other.x, other.y, obj, strict=keep)

    def get_pos(self):
        x, y = pygame.mouse.get_pos()
        # return y of COLS*CELL_HEIGHT+10 to avoid boarder bugs
        if y > ROWS * CELL_HEIGHT - 3:
            return ["CORD", x, ROWS * CELL_HEIGHT + 10]
        box_x = x // CELL_WIDTH
        box_y = y // CELL_HEIGHT
        return ["BOX", box_x, box_y]

    def draw_mouse(self, win, obj):
        # find rim colour
        if obj == Air:
            colour = (0, 0, 0)
        else:
            colour = obj.colour
        # hide mouse
        pygame.mouse.set_visible(False)
        # if in main area
        state, x, y = self.get_pos()
        if state == "CORD":
            pygame.mouse.set_visible(True)
            return
        # draw centre
        pygame.draw.rect(
            win,
            (226, 233, 16),
            [
                (x - 0.5) * CELL_WIDTH,
                (y - 0.5) * CELL_HEIGHT,
                CELL_WIDTH * 2,
                CELL_HEIGHT * 2,
            ],
        )
        # draw outer section
        pygame.draw.rect(
            win,
            colour,
            [
                CELL_WIDTH * x - (self.size - 1) * CELL_WIDTH,
                CELL_HEIGHT * y - (self.size - 1) * CELL_HEIGHT,
                ((self.size * 2 - 1) * CELL_WIDTH),
                min((self.size * 2 - 1) * CELL_HEIGHT, HEIGHT - LOWER_BOARDER),
            ],
            width=1,
        )

    def update(self, win, board, index):
        self.draw_mouse(win, particles[index])

        # check for input
        # unsafe placement
        if pygame.mouse.get_pressed()[0]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                self.press(board, *pos[1:], particles[index])

        if pygame.mouse.get_pressed()[1]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                x, y = pos[1:]
                try:
                    return particles.index(type(board.board[y, x]))
                except ValueError:  # Fountain not pick-able
                    if type(board.board[y, x]) == Fountain:
                        return particles.index(board.board[y, x].obj)

        # safe placements
        if pygame.mouse.get_pressed()[2]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                board = self.press(board, *pos[1:], particles[index], keep=True)
