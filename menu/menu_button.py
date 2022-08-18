import pygame
from conts import WIDTH, HEIGHT
from random import random

pygame.font.init()


class Slot_Button:
    """
    a class to handle buttons used for selection
     - handle drawing
     - checking for clicks
    """

    font = pygame.font.SysFont(None, 24)

    def __init__(self, x, y, xsize, ysize, name, img, mode):
        self.rect = pygame.Rect(x, y, xsize, ysize)
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.name = name
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (xsize, ysize))
        self.mode = mode
        self.xsize, self.ysize = xsize, ysize
        self.clicked = False

    def draw(self, win):
        # draw button on screen

        if self.clicked:
            colour = (255, 0, 0)
        else:
            colour = (0, 0, 0)

        name = Slot_Button.font.render(self.name, True, colour)
        # draw text
        win.blit(name, (self.x + name.get_size()[0] / 8, self.y - 15))
        # draw image (either picture of save of cross)
        win.blit(
            self.img,
            (self.rect.topleft[0], self.rect.topleft[1]),
        )

        # draw box around image
        pygame.draw.rect(
            win,
            colour,
            (self.x - 1, self.y - 1, self.xsize + 2, self.ysize + 2),
            width=2,
            border_radius=3,
        )

    def check_click(self):
        # check for click
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                return self.mode

    def up(self):
        self.clicked = True

    def down(self):
        self.clicked = False


class Button:
    """
    a class to represent buttons
     - handle drawing
     - handle
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
