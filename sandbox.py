from conts import *
import objects
import pygame
# import pygame.gfxdraw
import numpy as np


class Box:
    """
    a container for all particles
    - handle upading pos
    - drawing
    - adding new particles
    """

    def __init__(self):

        # setup board
        self.board = np.array([[objects.Air(x,y) for x in range(COLS)] for y in range(ROWS)])


    def draw_particals(self, win):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                pygame.draw.rect(win, val.colour, [j*CELL_WIDTH,i*CELL_HEIGHT,CELL_WIDTH,CELL_HEIGHT])
                # pygame.gfxdraw.box(win,[j*CELL_WIDTH,i*CELL_HEIGHT,CELL_WIDTH,CELL_HEIGHT], val.colour)

                
                
    def add_particle(self, x, y, obj, strict=False):
        # add particle to board
        if strict and type(self.board[y, x]) != objects.Air:
            return

        self.board[y, x] = obj(x,y)


    def update(self, win, fnum):
        # update board
        # heavy thingz
        for row in self.board[::-1]:
            for item in row:
                if item.count != fnum and item.mass > 0: # fnum same mean allready updated
                    # check for death in particle
                    if (result := item.update(self.board)) == "dies":
                        self.board[item.y, item.x] = objects.Air(item.x, item.y)
                    # if partcle wants to go thourgh a major change
                    elif result:
                        self.board[item.y, item.x] = result(item.x, item.y)

                    # update count
                    self.board[item.y, item.x].count = fnum
        # gasses
        for row in self.board:
            for item in row:
                if item.count < fnum and item.mass < 0:  # fnum same mean allready updated
                     # check for death in particle
                    if (result := item.update(self.board)) == "dies":
                        self.board[item.y, item.x] = objects.Air(item.x, item.y)
                    # if partcle wants to go thourgh a major change
                    elif result:
                        self.board[item.y, item.x] = result(item.x, item.y)

                    # update count
                    self.board[item.y, item.x].count = fnum 

        # DRAW THINGS!!!!
        self.draw_particals(win)

    def debug(self) -> list:
        vals = {}
        for i in particles:
            vals[i.__name__] = 0

        for row in self.board:
            for thing in row:
                vals[type(thing).__name__] = vals[type(thing).__name__] + 1


        return vals


