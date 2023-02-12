import logging

import pygame

import settings
from conts import (
    CELL_HEIGHT,
    CELL_WIDTH,
    LOWER_BOARDER,
    MOUSE_YELLOW,
    UPPER_BOARDER,
    WIDTH,
    YOFFSET,
)
from sandbox.objects import Air
from sandbox.objects.fountain import Fountain

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

    @property
    def colour(self):
        if any(pygame.mouse.get_pressed()):
            return (255, 0, 0)
        return MOUSE_YELLOW

    def get_pos(self):
        """
        get the position of the mouse -> tuple [state, x, y]
        - state is CORD or BOX
        - CORD is for menus
        - BOX is for game
        """

        x, y = pygame.mouse.get_pos()

        if LOWER_BOARDER < y or y < UPPER_BOARDER:  # in menu bar
            return ("CORD", x, y)

        box_x = x // CELL_WIDTH
        box_y = (y - YOFFSET) // CELL_HEIGHT

        return ("BOX", box_x, box_y)

    def _get_box_cords(self, x: float, y: float) -> tuple:

        size_width = (self.size) * CELL_WIDTH * 2 - CELL_WIDTH
        size_height = (self.size) * CELL_HEIGHT * 2 - CELL_HEIGHT
        # find topleft
        topleft_x = (x - self.size) * CELL_WIDTH + CELL_WIDTH
        topleft_y = (y - self.size) * CELL_HEIGHT + CELL_HEIGHT + YOFFSET

        if topleft_y + size_height > LOWER_BOARDER - 3:
            size_height = LOWER_BOARDER - 3 - topleft_y

        if topleft_x + size_width > WIDTH - 1:
            size_width = WIDTH - topleft_x - 2

        if topleft_x < 0:
            diff = abs(topleft_x)
            size_width -= diff
            topleft_x = 2

        if topleft_y < UPPER_BOARDER:
            diff = UPPER_BOARDER - topleft_y
            size_height -= diff
            topleft_y = UPPER_BOARDER + 2

        box_cords = (topleft_x, topleft_y, size_width + 1, size_height + 1)
        return box_cords

    def draw_mouse(self, win, obj):

        if not pygame.mouse.get_focused():
            return

        # hide mouse
        pygame.mouse.set_visible(settings.debug.value)

        state, x, y = self.get_pos()

        if state == "CORD":
            pygame.draw.circle(win, self.colour, (x, y), 6)
            return

        # draw centre

        rx, ry = pygame.mouse.get_pos()

        # snap to grid
        rx = rx - rx % CELL_WIDTH
        ry = ry - ry % CELL_HEIGHT
        size_mult = 1.75
        w, h = CELL_WIDTH * size_mult, CELL_HEIGHT * size_mult
        rect = (rx - (CELL_WIDTH) / 4, ry - (CELL_HEIGHT) / 4, w, h)

        pygame.draw.rect(win, self.colour, rect)

        # find rim colour
        if obj == Air:
            colour = (0, 0, 0)
        else:
            colour = obj.colour
        # draw outer section

        box_cords = self._get_box_cords(x, y)
        pygame.draw.rect(win, colour, box_cords, width=1)

    def update(self, win, board, obj):
        self.draw_mouse(win, obj)
        events = []
        # check for input
        # unsafe placement
        if pygame.mouse.get_pressed()[0]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                x, y = pos[1:]
                y += YOFFSET
                events.append(
                    {
                        "handler": "sim",
                        "type": "press",
                        "value": (self.size, *pos[1:], obj, False, None),
                    }
                )

        if pygame.mouse.get_pressed()[1]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                x, y = pos[1:]
                obj = board[y, x].__class__
                if isinstance(obj, Fountain):
                    obj = obj.obj

                events.append({"handler": "selection", "type": "press", "value": obj})

        # safe placements
        if pygame.mouse.get_pressed()[2]:
            pos = self.get_pos()
            if pos[0] == "BOX":
                events.append(
                    {
                        "handler": "sim",
                        "type": "press",
                        "value": (self.size, *pos[1:], obj, True, None),
                    }
                )

        return events
