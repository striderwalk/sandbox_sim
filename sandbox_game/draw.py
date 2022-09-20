import pygame
from conts import CELL_WIDTH, CELL_HEIGHT
from sandbox.objects import Air

def draw_board(win, board, show_temp=False, show_fountain=True):
    # draw all particles
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            # if air don't draw to save time
            if type(val) == Air and not show_temp:
                continue
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