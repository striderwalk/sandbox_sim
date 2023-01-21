import pygame

import settings
from conts import CELL_HEIGHT, CELL_WIDTH
from sandbox.objects import Air
from sandbox.objects.fountain import Fountain

flame_glow = pygame.Surface((CELL_WIDTH * 2, CELL_HEIGHT * 2), pygame.SRCALPHA)


def draw_row(surf, i, row, showtemp, show_fountain):
    for j, item in enumerate(row):
        # if air don't draw to save time
        if isinstance(item, Air) and not showtemp:
            continue

        if showtemp:
            colour = item.temp_colour
        elif isinstance(item, Fountain) and not show_fountain:
            colour = item.obj.colour
        else:
            colour = item.colour

        rect = j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT
        pygame.draw.rect(surf, colour, rect)


def draw_board(surf, board, show_fountain=True):

    # draw all particles
    showtemp = settings.showtemp.value
    for i, row in enumerate(board):
        draw_row(surf, i, row, showtemp, show_fountain)

    # idk about thids
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item.is_flame:
                x, y = (j - 0.5) * CELL_WIDTH, (i - 0.5) * CELL_HEIGHT
                glow = flame_glow.copy()
                glow.fill((*item.colour, 10))
                surf.blit(glow, (x, y), special_flags=pygame.BLEND_ALPHA_SDL2)
    return surf
