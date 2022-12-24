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
        draw_board(win, self.board.board, show_fountain=False)
