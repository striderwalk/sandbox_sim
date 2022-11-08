import pygame
from conts import RED, TEXT_COLOUR, BG_COLOUR
import fonts
"""
 deal with options menu stuff
  - toggle heat map
  - paused


"""

# NOT TO BE USED YET 
font = fonts.get_font(10)


class Button():

    def __init__(self, text, pos, size) -> None:
        self.text = text
        self.pos = pos
        self.rect = rect
        self.image = pygame.Surface(size)
        self.image.fill(BG_COLOUR)

        self.click = False

    def is_clicked(self) -> bool:

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return pygame.mouse.get_pressed()[0]

    def draw(self, win) -> None:
        if self.clicked:
            text_colour = RED
        else:
            text_colour = TEXT_COLOUR

        text = font.render(self.text, False, text_color)
        image = self.image.copy()
        x = (image.get_width() - text.get_width()) / 2
        y = (image.get_height() - text.get_height()) / 2
        image.blit(text, (x, y))
        win.blit(image, self.pos)


class Menu():

    def __init__(self):
        pass
