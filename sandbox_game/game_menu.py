import pygame

import errors
import fonts
import settings
from conts import BG_COLOUR, RED, TEXT_COLOUR, UPPER_BOARDER, WIDTH

"""
 deal with options menu stuff
  - toggle heat map
  - paused
"""


font = fonts.get_font(10)

Position = tuple[int]
Size = tuple[int]


def make_text(text, alt_text, text_colour=TEXT_COLOUR, alt_text_colour=RED):
    rtext = font.render(text, False, text_colour)
    ralt_text = font.render(alt_text, False, alt_text_colour)
    return rtext, ralt_text


class Button:
    # make button text obj refer to brain for reason
    def __init__(self, text, alt_text, pos: Position, size: Size, setting=None):
        # text
        self.text = text
        self.alt_text = alt_text
        # clicks
        self.setting = setting
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

    def __init__(self):
        self.image = pygame.Surface(Menu.size, pygame.SRCALPHA)
        self.image.fill((*BG_COLOUR, 100))
        rtext, ralt_text = make_text("=", "x")
        self.menu_button = Button(
            rtext, ralt_text, (10, 5), (20, 20), setting=settings.showmenu
        )
        self.buttons = {}
        self.bx, self.by = 40, 5
        self.bdx, self.bdy = 80, 0
        self.bsize = (70, 20)

    def toggle(self, name):
        self.buttons[name].click()

    def make_button(self, text, alt_text, setting):
        x, y = self.bx, self.by
        self.bx += self.bdx
        self.by += self.bdy

        rtext, ralt_text = make_text(text, alt_text)
        return Button(rtext, ralt_text, (x, y), self.bsize, setting=setting)

    def add_button(self, name, dat):
        if name in self.buttons:
            raise errors.NameAlreadyExists(name)
        b = self.make_button(*dat)
        self.buttons[name] = b

    def draw(self, win):
        # if not self.menu_button.clicked:
        if not self.menu_button.clicked:
            img = pygame.Surface(Menu.size, pygame.SRCALPHA)
            img.fill((0, 0, 0, 0))
        else:
            img = self.image.copy()
            draw = lambda x: x.draw(img)
            list(map(draw, self.buttons.values()))

        self.menu_button.draw(img)
        win.blit(img, Menu.pos)
