from conts import *
import pygame
import objects


class Box:
    """
    a container for all particles
    - handle upading pos
    - drawing
    - adding new particles
    """

    def __init__(self):

        # setup board
        self.board = [[objects.Air(x,y) for x in range(COLS)] for y in range(ROWS)]


    def draw_particals(self, win):
        for i in range(ROWS):
            for j in range(COLS):
                pygame.draw.rect(win, self.board[i][j].colour,[j*CELL_WIDTH,i*CELL_HEIGHT,CELL_WIDTH,CELL_HEIGHT])
    def add_particle(self, x, y, obj, strict=False):
        # add particle to board
        if strict and type(self.board[y][x]) != objects.Air:
            return

        self.board[y][x] = obj(x,y)


    def update(self, win, fnum):
        # update board
        # others
        for row in self.board[::-1]:
            for item in row:
                if item.count < fnum and item.mass > 0:
                    if (result := item.update(self.board)) == "dies":
                        self.board[item.y][item.x] = objects.Air(item.x, item.y)
                    elif result:
                        self.board[item.y][item.x] = result(item.x, item.y)

                
                    item.count = fnum
        # gasses
        for row in self.board:
            for item in row:
                if item.count < fnum and item.mass < 0: 
                    if (result := item.update(self.board)) == "dies":
                        self.board[item.y][item.x] = objects.Air(item.x, item.y)
                    elif result:
                        self.board[item.y][item.x] = result(item.x, item.y)

                    item.count = fnum 


        # draw board
        self.draw_particals(win)

    def debug(self) -> list:
        vals = {}
        for i in particles:
            vals[i.__name__] = 0

        for row in self.board:
            for thing in row:
                vals[type(thing).__name__] = vals[type(thing).__name__] + 1


        return vals


