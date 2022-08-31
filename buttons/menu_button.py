import pygame
from random import random
from conts import WIDTH, HEIGHT

pygame.font.init()


class Button:
    """
    a class to represent buttons
     - handle drawing
     - check for clicks
    """

    font = pygame.font.SysFont(None, 64)

    def __init__(self, x, y, xsize, ysize, text, func):
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.text = text
        self.func = func
        self.xsize, self.ysize = xsize, ysize

    def draw(self, win):
        # draw button on screen
        pos = pygame.mouse.get_pos()
        # set colour based on mouse pos
        if self.rect.collidepoint(pos):
            rect_colour = (20, 20, 25)
            text_colour = (235, 235, 235)
        else:
            rect_colour = (235, 235, 235)
            text_colour = (20, 20, 25)

        # draw box
        pygame.draw.rect(win, rect_colour, self.rect, border_radius=3)

        # draw text
        img = Button.font.render(self.text, True, text_colour)
        win.blit(
            img,
            (
                self.rect.centerx - img.get_size()[0] / 2,
                self.rect.centery - img.get_size()[1] / 2,
            ),
        )

    def check_click(self):
        # check if clicked
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                return self.func