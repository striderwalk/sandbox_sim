import pygame
from conts import *
pygame.font.init()
font = pygame.font.SysFont(None, 24)

class Button:
    """
    a class to represent buttons
     - handle drawing
     - handle
    """

    def __init__(self, x, y, size, text, colour):
        self.rect = pygame.Rect((x,y), (size, size))
        self.rect.topleft = (x, y)
        self.size = size
        self.x = x
        self.y = y
        self.colour = colour
        self.text = text
        self.clicked = False

    def draw(self, win):
        # draw button on screen
        pygame.draw.rect(win, self.colour, self.rect, border_radius =3)
        if self.clicked:
            img = font.render(self.text, True, (245,10,10))
        else:
            img = font.render(self.text, True, (0,0,0))

        win.blit(img, (self.rect.centerx-img.get_size()[0]/2, self.rect.centery-img.get_size()[1]/2))


    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                action = True

        return action
    def move(self, new_x, new_y):
        # move by a given amount
        self.x += new_x
        self.y += new_y
        self.rect = pygame.Rect((self.x,self.y), (self.size, self.size))
        self.rect.topleft = (self.x, self.y)

    def move_to(self, new_x, new_y):
        # move to somewhere
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect((self.x,self.y), (self.size, self.size))
        self.rect.topleft = (self.x, self.y)

    def up(self):
        # unclick
        self.clicked = False

    def down(self):
        # click
        self.clicked = True
