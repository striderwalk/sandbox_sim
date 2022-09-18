from slots import load_path
from .sandbox import Box



class Background:
    def __init__(self):
        self.board = Box(load_path("./assets/menu_board.json"))
        self.fnum = -1

    def draw_background(self, win):
        self.fnum += 1
        self.board.update(win, self.fnum, False, False, show_fountain=False)
