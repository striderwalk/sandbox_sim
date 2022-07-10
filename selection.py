import pygame
from conts import *
from button import Button
from inspect import getmembers, isclass
import objects




class Selection:
    def __init__(self, index=0):
        self.buttons = []
        self.index = index

        size = LOWER_BOARDER-5
        for i, obj in enumerate(particles):

            x = size*i+size/2
            y = HEIGHT-LOWER_BOARDER+5
            self.buttons.append(Button(x,y,size, obj.__name__, obj.colour))

        self.buttons[self.index].down()



    def update(self, win, index):#
        pygame.draw.rect(win, (0,0,0), (0, HEIGHT-LOWER_BOARDER, WIDTH, LOWER_BOARDER))
        self.index = index
        res = []
        for i, button in enumerate(self.buttons):
            if click := button.draw(win):
                res.append(i)

        if len(res) == 0:
            res.append(index)

        for i, button in enumerate(self.buttons):
            if i != res[0]:
                button.up()

            else:
                button.down()

        self.index = res[0]

        return self.index

            


