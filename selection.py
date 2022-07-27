import pygame
from conts import *
from button import Button


class Selection:
    def __init__(self, index=0):
        self.buttons = []
        self.index = index

        size = LOWER_BOARDER-5
        for i, obj in enumerate(particles):

            x = size*i
            y = HEIGHT-LOWER_BOARDER+5
            self.buttons.append(Button(x,y,size, obj.__name__, obj.colour))

        self.buttons[self.index].down()
        # to prevent selection changing when wraping
        self.draw_buttons =self.buttons
        


    def shift(self, num):
        moved_buttons = []
        for button in self.draw_buttons:
            button.move(num, 0)
            moved_buttons.append(button)

        for button in moved_buttons:
            if button.x+button.size < 0:
                moved_buttons.remove(button)
                button.move_to(moved_buttons[-1].x+moved_buttons[-1].size, moved_buttons[-1].y)
                moved_buttons.append(button)
            if button.x > WIDTH:
                moved_buttons.remove(button)
                button.move_to(moved_buttons[0].x-button.size, moved_buttons[0].y)
                moved_buttons.insert(0, button)
        self.draw_buttons = moved_buttons


    def update(self, win, index):#
        pygame.draw.rect(win, (0,0,0), (0, HEIGHT-LOWER_BOARDER, WIDTH, LOWER_BOARDER))
        self.index = index

        # draw buttons
        for i, button in enumerate(self.draw_buttons): button.draw(win)

        res = []
        for i, button in enumerate(self.buttons): 
            if click := button.check_click():
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

            


