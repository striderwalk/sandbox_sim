from conts import *
import objects
import pygame
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
                if type(val) != objects.Air:
                    pygame.draw.rect(win, val.colour, [j*CELL_WIDTH,i*CELL_HEIGHT,CELL_WIDTH,CELL_HEIGHT])
                # pygame.gfxdraw.box(win,[j*CELL_WIDTH,i*CELL_HEIGHT,CELL_WIDTH,CELL_HEIGHT], val.colour)

                
                
    def add_particle(self, x, y, obj, strict=False, **kwargs):
        if obj not in particles:
            raise TypeError(f"add_particle ask to place invadlid particle {obj}")
        # add particle to board
        if strict and type(self.board[y, x]) != objects.Air:
            return
        try:
            if kwargs:
                self.board[y, x] = obj(x,y, **kwargs)
            else:
                self.board[y, x] = obj(x,y)
        except Exception as e:
            print(obj)
            raise e

    def update(self, win, fnum, pause):
        # DRAW THINGS!!!!
        self.draw_particals(win)
        if pause: return

        # update board for heavy things
        for row in self.board[::-1]:
            for item in row:
                if item.count != fnum and item.mass > 0: # if fnum same allready updated
                  
                    # check for death in particle
                    if (result := item.update(self.board)) == "dies":
                        self.board[item.y, item.x] = objects.Air(item.x, item.y)
                    # if partcle wants to go thourgh a major change
                    elif result:
                        self.board[item.y, item.x] = result(item.x, item.y)

                    # update count
                    self.board[item.y, item.x].count = fnum
            for item in row:
                if type(item) != objects.Air:
                    item.load_move(self.board)


        # update board for other things
        for row in self.board:
            for item in row[::-1]:
                if item.count != fnum and item.mass < 0: # if fnum same allready updated
                  
                    # check for death in particle
                    if (result := item.update(self.board)) == "dies":
                        self.board[item.y, item.x] = objects.Air(item.x, item.y)
                    # if partcle wants to go thourgh a major change
                    elif result:
                        self.board[item.y, item.x] = result(item.x, item.y)

                    # update count
                    self.board[item.y, item.x].count = fnum
            for item in row:
                if type(item) != objects.Air:
                    item.load_move(self.board)



    def debug(self) -> list:
        vals = {}
        for i in particles:
            vals[i.__name__] = 0

        for row in self.board:
            for thing in row:
                vals[type(thing).__name__] = vals[type(thing).__name__] + 1


        return vals


    def fix(self):
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                item.x = x
                item.y = y