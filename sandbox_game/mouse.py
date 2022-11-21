import pygame
import logging
from sandbox.objects.fountain import Fountain
from sandbox.objects import Air
from conts import (
    CELL_WIDTH,
    CELL_HEIGHT,
    ROWS,
    WIDTH,
    HEIGHT,
    LOWER_BOARDER,
    UPPER_BOARDER,
    MOUSE_YELLOW,
)
import settings

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

    def get_pos(self):
        x, y = pygame.mouse.get_pos()
        # return y of COLS*CELL_HEIGHT+10 to avoid boarder bugs
        upper_boarder = UPPER_BOARDER if settings.showmenu.value else 0
        if y > LOWER_BOARDER - 3 or y < upper_boarder:
            # i think this is meant to make sure clicks happen, but could be a bug??
            return ("CORD", x, y)

        box_x = x // CELL_WIDTH
        box_y = y // CELL_HEIGHT

        return ("BOX", box_x, box_y)

    def _get_box_cords(self, x: float, y: float) -> tuple[float]:
        upper_boarder = UPPER_BOARDER if settings.showmenu.value else 0
        size_width = (self.size) * CELL_WIDTH * 2 - CELL_WIDTH
        size_height = (self.size) * CELL_HEIGHT * 2 - CELL_HEIGHT
        # find topleft
        topleft_x = (x - self.size) * CELL_WIDTH + CELL_WIDTH
        topleft_y = (y - self.size) * CELL_HEIGHT + CELL_HEIGHT

        if topleft_y + size_height > LOWER_BOARDER - 3:
            size_height = LOWER_BOARDER - 3 - topleft_y

        if topleft_x + size_width > WIDTH - 1:
            size_width = WIDTH - topleft_x - 2

        if topleft_x < 0:
            diff = abs(topleft_x)
            size_width -= diff
            topleft_x = 2

        if topleft_y < upper_boarder:
            diff = 0 - topleft_y
            size_height -= diff
            topleft_y = 2

        box_cords = (topleft_x, topleft_y, size_width + 1, size_height + 1)
        return box_cords

    def draw_mouse(self, win, obj, shown):
        # hide mouse
        pygame.mouse.set_visible(False)

        state, x, y = self.get_pos()
        if state == "CORD":
            print(x, y)
            rect = (x - CELL_WIDTH, y - CELL_HEIGHT,
                    CELL_WIDTH * 2, CELL_HEIGHT * 2)
            pygame.draw.rect(win, MOUSE_YELLOW, rect, border_radius=3)
            return

        # draw centre
        rx, ry = pygame.mouse.get_pos()
        rx %= CELL_WIDTH
        ry %= CELL_HEIGHT

        center_x = (x - 0.5) * CELL_WIDTH
        center_y = (y - 0.5) * CELL_HEIGHT
        rect = (center_x + rx, center_y + ry, CELL_WIDTH * 2, CELL_HEIGHT * 2)
        pygame.draw.rect(win, MOUSE_YELLOW, rect, border_radius=3)

        # check if out seaction is needed

        # find rim colour
        if obj == Air:
            colour = (0, 0, 0)
        else:
            colour = obj.colour
        # draw outer section

        box_cords = self._get_box_cords(x, y)
        pygame.draw.rect(win, colour, box_cords, width=1)

    def update(self, win, board, obj, shown_menu):
        self.draw_mouse(win, obj, shown_menu)
        events = []
        # check for input
        # unsafe placement
        if pygame.mouse.get_pressed()[0]:
            pos = self.get_pos()
            if pos[0] == "BOX":
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
                obj = type(board[y, x])
                if isinstance(obj, Fountain):
                    obj = obj.obj

                events.append(
                    {"handler": "selection", "type": "press", "value": obj})

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
