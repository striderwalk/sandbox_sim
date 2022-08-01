import pygame
from conts import WIDTH, HEIGHT
from random import random

pygame.font.init()
font = pygame.font.SysFont(None, 24)


class Slot_Button:
    """
    a class to represent buttons
     - handle drawing
     - handle
    """

    def __init__(self, x, y, xsize, ysize, name, state, mode):
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.name = name
        if state:
            self.img = pygame.image.load("./assets/check.png")
        else:
            self.img = pygame.image.load("./assets/cross.png")
        self.img = pygame.transform.scale(self.img, (xsize,ysize))
        self.mode = mode
        self.xsize, self.ysize = xsize, ysize
        self.clicked = False

    def draw(self, win):
        # draw button on screen

        if self.clicked:
            pygame.draw.rect(win, (255, 0, 0), (self.x-1, self.y-1, self.xsize+2, self.ysize+2), width=2)
            name = font.render(self.name, True, (255,0,0))

        else:
            pygame.draw.rect(win, (0, 0, 0), (self.x-1, self.y-1, self.xsize+2, self.ysize+2), width=2)
            name = font.render(self.name, True, (0,0,0))
        win.blit(name, (self.x+name.get_size()[0]/8, self.y-15))
        win.blit(self.img,(self.rect.topleft[0],self.rect.topleft[1]),)

    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
        if action:
            return self.mode

    def up(self):
        self.clicked = True
    def down(self):
        self.clicked = False
    