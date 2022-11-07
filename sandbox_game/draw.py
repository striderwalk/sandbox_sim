import pygame
from conts import CELL_WIDTH, CELL_HEIGHT
from sandbox.objects import Air
from sandbox.objects.fountain import Fountain


def draw_board(surf, board, show_temp=False, show_fountain=True):
    # draw all particles
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            # if air don't draw to save time
            if type(val) == Air and not show_temp:
                continue

            if show_temp:
                colour = val.temp_colour
            elif type(val) == Fountain and not show_fountain:
                colour = val.obj.colour
            else:
                colour = val.colour

            pygame.draw.rect(
                surf,
                colour,
                [j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT],
            )

    return surf
