from conts import *
import objects
import pygame
import numpy as np
from random import randint

class Box:
    """
    a container for all particles
    use for
    - updating
    - moving
    - drawing
    - adding new particles
    """

    def __init__(self):
        # setup board
        self.board = np.array([[objects.Air(x,y) for x in range(COLS)] for y in range(ROWS)])


    def draw_particles(self, win):
        # draw all particles
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                # if air not dawn to save time
                pygame.draw.rect(win, val.colour, [j*CELL_WIDTH,i*CELL_HEIGHT,CELL_WIDTH,CELL_HEIGHT])
                # if type(val) != objects.Air:

                
                
    def add_particle(self, x, y, obj, strict=False, **kwargs) -> None:
        if obj not in particles:
            raise TypeError(f"add_particle ask to place invalid particle {obj}")
        # add particle to board
        # strict mean not replace non air
        if strict and type(self.board[y, x]) != objects.Air:
            return

        if kwargs:
            self.board[y, x] = obj(x,y, **kwargs)
        else:
            self.board[y, x] = obj(x,y)


    def update(self, win : pygame.surface, fnum : int, pause : bool) -> None:
        # DRAW THINGS!!!!
        self.draw_particles(win)
        if pause: return

        # update board for heavy things
        for row in self.board[::-1]:
            for item in row:
                if item.count != fnum and item.mass > 0: # if fnum same already updated
                  
                    # check for death in particle
                    if (result := item.update(self.board)) == "dies":
                        self.board[item.y, item.x] = objects.Air(item.x, item.y)
                    # if particle wants to go though a major change of behaviour
                    elif result:
                        self.board[item.y, item.x] = result(item.x, item.y)

                    # update count
                    self.board[item.y, item.x].count = fnum
            for item in row:
                item.load_move(self.board)

        # update board for other things
        for row in self.board:
            for item in row[::-1]:
                if item.count != fnum and item.mass < 0: # if fnum same already updated
                  
                    # check for death in particle
                    if (result := item.update(self.board)) == "dies":
                        item.load_move(self.board)
                        self.board[item.y, item.x] = objects.Air(item.x, item.y)
                    # if particle wants to go though a major change
                    elif result:
                        self.board[item.y, item.x] = result(item.x, item.y)

                    # update count
                    self.board[item.y, item.x].count = fnum

            # move items
            for item in row:
                item.load_move(self.board)



    def debug(self) -> list:
        # return No. of particles
        vals = {}
        for i in particles:
            vals[i.__name__] = 0

        for row in self.board:
            for thing in row:
                vals[type(thing).__name__] = vals[type(thing).__name__] + 1


        return vals


    def fix(self) -> None:
        # tell each particle where there are
        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if item.y != y or item.x != x: 
                    print(f"WARNING: {item=} pos needed fixing to {x=}, {y=}")
                item.x = x
                item.y = x

    def rain_type(self, obj, num=1500) -> None:
        for _ in range(num):            
            y,x = randint(0,ROWS-1),randint(0,COLS-1) 
            self.add_particle(x,y, obj)
