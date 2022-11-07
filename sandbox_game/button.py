import pygame
from conts import RED, BLACK
pygame.font.init()
font = pygame.font.Font("assets/fonts/joystix monospace.ttf", 10)


class Button:
    def __init__(self, x, y, size, name, colour):
        image = pygame.Surface((size, size))
        image.fill(colour)
        self.image = image
        self.text = name
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y, size, size))
        self.size = size
        self.clicked = False

    @ property
    def pos(self):
        return self.x, self.y

    def draw(self, win):
        if self.clicked:
            text_color = RED
        else:
            text_color = BLACK

        text = font.render(self.text, False, text_color)
        image = self.image.copy()
        x = (image.get_width() - text.get_width()) / 2
        y = (image.get_height() - text.get_height()) / 2
        image.blit(text, (x, y))
        win.blit(image, self.pos)

    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
        return action

    def move(self, new_x, new_y):
        # move by a given amount
        self.x += new_x
        self.y += new_y
        self.rect = pygame.Rect((self.x, self.y), (self.size, self.size))
        self.rect.topleft = (self.x, self.y)

    def move_to(self, new_x, new_y):
        # move to somewhere
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect((self.x, self.y), (self.size, self.size))
        self.rect.topleft = (self.x, self.y)

    def up(self):
        # unclick
        self.clicked = False

    def down(self):
        # click
        self.clicked = True
