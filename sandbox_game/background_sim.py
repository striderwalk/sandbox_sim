import pygame
from conts import CELL_HEIGHT, CELL_WIDTH, COLS, ROWS, YOFFSET
from sandbox import Box, update_sim
from slots import load_path

from .draw import draw_board

#############
## save me ##
#############


class Background:
    def __init__(self):
        self.board = Box(load_path("./assets/menu_board.json"))
        self.fnum = -1

    def update(self, win):
        self.fnum += 1
        update_sim(self.board)

        surf = pygame.Surface((COLS * CELL_WIDTH, ROWS * CELL_HEIGHT))
        draw_board(surf, self.board.board, show_fountain=False)
        win.blit(surf, (0, YOFFSET))
