import pygame
import logging
import errors
from conts import RED, TEXT_COLOUR, BG_COLOUR, WIDTH
import fonts
"""
 deal with options menu stuff
  - toggle heat map
  - paused


"""


font = fonts.get_font(10)


class Button():

    def __init__(self, text, alt_text, hook, pos, size) -> None:
        # text
        self.text = text
        self.alt_text = alt_text
        # clicks
        self.hook = hook
        self.rect = pygame.Rect(pos, size)
        self.clicked = False
        self.timeout = 0
        # drawing
        self.pos = pos
        self.image = pygame.Surface(size)
        self.image.fill(BG_COLOUR)

    def _is_clicked(self) -> bool:

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return pygame.mouse.get_pressed()[0]

    def check_clicked(self):
        if self.timeout > 0:
            self.timeout -= 1
            return

        if self._is_clicked():
            self.hook()
            self.clicked = not self.clicked

    def click(self):
        # allow other thing eg keyboard input
        # to not desync
        self.clicked = not self.clicked

    def draw(self, win):
        self.check_clicked()

        if self.clicked:
            text = font.render(self.alt_text, False, RED)

        else:
            text = font.render(self.text, False, TEXT_COLOUR)

        image = self.image.copy()
        x = (image.get_width() - text.get_width()) / 2
        y = (image.get_height() - text.get_height()) / 2
        image.blit(text, (x, y))
        win.blit(image, self.pos)


class Menu():
    pos = (0, 0)
    size = (WIDTH, 30)

    def __init__(self):
        self.image = pygame.Surface(Menu.size, pygame.SRCALPHA)
        self.image.fill((*BG_COLOUR, 100))
        self.buttons = {}
        self.bx, self.by = 20, 5
        self.bdx, self.bdy = 80, 0
        self.bsize = (70, 20)

    def toggle(self, name):
        self.buttons[name].click()

    def make_button(self, text, alt_text, hook):
        x, y = self.bx, self.by
        self.bx += self.bdx
        self.by += self.bdy
        return Button(text, alt_text, hook, (x, y), self.bsize)

    def add_button(self, name, dat):
        if name in self.buttons:
            raise errors.NameAlreadyExists(name)

        b = self.make_button(*dat)
        self.buttons[name] = b

    def draw(self, win):
        img = self.image.copy()

        for i in self.buttons.values():
            i.draw(img)

        win.blit(img, Menu.pos)
