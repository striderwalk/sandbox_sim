import pygame
from sandbox.objects.fountain import Fountain
from sandbox.objects import Air
from sandbox import particles
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



    def heat_cells(self, board, x, y, temp):
        for _, other in board[y][x].get_neighbours(board, self.size):
            other.temp += temp

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
        clicks = []
        # check for input
        # unsafe placement
        if pygame.mouse.get_pressed()[0]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                clicks.append({"type": "press", "value" : (self.size, *pos[1:], particles[index], False, None)})

        if pygame.mouse.get_pressed()[1]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                x, y = pos[1:]
                try:
                    return particles.index(type(board[y, x]))
                except ValueError:  # Fountain not pick-able
                    if type(board[y, x]) == Fountain:
                        return particles.index(board[y, x].obj)
                        
        # safe placements
        if pygame.mouse.get_pressed()[2]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                 clicks.append({"type": "press", "value" : (self.size, *pos[1:], particles[index], True, None)})

        return clicks
