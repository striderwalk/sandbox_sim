import pygame
from pygame import Vector2

import errors
import fonts
import settings
from conts import (
    BG_COLOUR,
    CELL_HEIGHT,
    CELL_WIDTH,
    EMPTY_COLOUR,
    RED,
    TEXT_COLOUR,
    UPPER_BOARDER,
    WIDTH,
    YOFFSET,
)

"""
 deal with options menu stuff
  - toggle heat map
  - paused
"""


font = fonts.get_font(10)

Position = Vector2
Size = Vector2


def make_text(text, alt_text, text_colour=TEXT_COLOUR, alt_text_colour=RED):
    rtext = font.render(text, False, text_colour)
    ralt_text = font.render(alt_text, False, alt_text_colour)
    return rtext, ralt_text


class Button:
    # make button text obj refer to brain for reason
    def __init__(
        self, text, alt_text, pos: Position, size: Size, setting=None, default=False
    ):
        # text
        self.text = text
        self.alt_text = alt_text
        # clicks
        self.setting = setting
        self.rect = pygame.Rect(pos, size)
        self.clicked = default
        self.timeout = 0
        # drawing
        self.pos = pos
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill(EMPTY_COLOUR)
        pygame.draw.rect(self.image, BG_COLOUR, (0, 0, *size), border_radius=4)

    def _is_clicked(self) -> bool:
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return pygame.mouse.get_pressed()[0]
        return False

    def check_clicked(self):
        if self.timeout > 0:
            self.timeout -= 1
            return

        if self._is_clicked():
            if self.setting:
                self.setting.toggle()
            else:
                self.click()
            self.timeout = 5

    def click(self):
        # allow other thing eg keyboard input
        # to not desync
        self.clicked = not self.clicked

    def draw(self, win):
        self.check_clicked()
        if self.setting:
            self.clicked = self.setting.value

        if self.clicked:
            text = self.alt_text

        else:
            text = self.text

        image = self.image.copy()
        x = (image.get_width() - text.get_width()) / 2
        y = (image.get_height() - text.get_height()) / 2
        image.blit(text, (x, y))
        win.blit(image, self.pos)


class Menu:
    pos = (0, 0)
    size = (WIDTH, UPPER_BOARDER)
    image = pygame.Surface(size, pygame.SRCALPHA)
    image.fill(EMPTY_COLOUR)

    def __init__(self):
        self.image = pygame.Surface(Menu.size, pygame.SRCALPHA)
        self.image.fill(EMPTY_COLOUR)
        self.buttons = {}
        self.bx, self.by = CELL_WIDTH, YOFFSET / 4
        self.bheight = YOFFSET / 2
        self.bdx, self.bdy = CELL_WIDTH, 0

    def toggle(self, name):
        self.buttons[name].click()

    def make_button(self, text, alt_text, setting, default):

        x, y = self.bx, self.by
        colour = RED if not default else TEXT_COLOUR
        rtext, ralt_text = make_text(text, alt_text, alt_text_colour=colour)
        xsize = max((max(rtext.get_width(), ralt_text.get_width()) * 1.8), 30)
        self.bx += self.bdx + xsize
        self.by += self.bdy
        return Button(
            rtext,
            ralt_text,
            (x, y),
            (xsize, self.bheight),
            setting=setting,
            default=default,
        )

    def add_button(self, name, dat, default=False):
        if name in self.buttons:
            raise errors.NameAlreadyExists(name, self.buttons)
        self.buttons[name] = self.make_button(*dat, default)

    def draw(self, win):

        img = Menu.image.copy()
        img = self.image.copy()
        for i in self.buttons.values():
            i.draw(img)

        win.blit(img, Menu.pos)
