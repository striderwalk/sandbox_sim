import pygame
import itertools

from conts import WIDTH, HEIGHT, LOWER_BOARDER
from slots import load_path 
from .selection import Selection
from .sandbox import Box
from .get_particles import particles, objects


class Background:

    def __init__(self):
        self.board = Box(load_path("./assets/menu_board.pickle"))
        self.fnum = -1

    def draw_background(self, win):
        self.fnum += 1
        self.board.update(win, self.fnum, False,  show_fountain=False)

