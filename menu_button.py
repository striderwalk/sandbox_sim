import pygame
from conts import WIDTH, HEIGHT
from random import random

pygame.font.init()
font = pygame.font.SysFont(None, 24)


class Button:
    """
    a class to represent buttons
     - handle drawing
     - handle
    """

    def __init__(self, x, y, xsize, ysize, text, mode):
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.text = text
        self.mode = mode
        self.xsize, self.ysize = xsize, ysize
        self.clicked = False

    def draw(self, win):
        # draw button on screen
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(win, (0,0,0), self.rect, border_radius=3)
            img = font.render(self.text, True, (235, 235, 235))
        else:
            pygame.draw.rect(win, (255, 255, 255), self.rect, border_radius=3)
            pygame.draw.rect(win,(0, 0, 0), self.rect, width=2)
            img = font.render(self.text, True, (0,0,0))

        if self.clicked:
            img = font.render(self.text, True, (255,0,0))
            pygame.draw.rect(win,(255, 0, 0), self.rect, width=2)

        win.blit(
            img,
            (
                self.rect.centerx - img.get_size()[0] / 2,
                self.rect.centery - img.get_size()[1] / 2,
            ),
        )

    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action = True
        if action:
            return self.mode

    def up(self):
        self.clicked = True
    def down(self):
        self.clicked = False
    