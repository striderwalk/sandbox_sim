import pygame
import errors
from typing import Callable
from conts import RED, TEXT_COLOUR, BG_COLOUR, WIDTH, UPPER_BOARDER
import fonts

"""
 deal with options menu stuff
  - toggle heat map
  - paused


"""


font = fonts.get_font(10)

Position = tuple[int]
Size = tuple[int]


# class Button


class Button:
    # make button text obj refer to brain for reason
    def __init__(self, text: str, alt_text: str, pos: Position, size: Size, hook: Callable = None):
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
            if self.hook:
                self.hook()
            else:
                self.click()
            self.timeout = 5

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


class Menu:
    pos = (0, 0)
    size = (WIDTH, UPPER_BOARDER)

    def __init__(self):
        self.image = pygame.Surface(Menu.size, pygame.SRCALPHA)
        self.image.fill((*BG_COLOUR, 100))
        self.menu_button = Button("≡", "x", (10, 5), (20, 20))
        self.buttons = {}
        self.bx, self.by = 40, 5
        self.bdx, self.bdy = 80, 0
        self.bsize = (70, 20)

    def toggle(self, name):
        self.buttons[name].click()

    def make_button(self, text, alt_text, hook):
        x, y = self.bx, self.by
        self.bx += self.bdx
        self.by += self.bdy
        return Button(text, alt_text, (x, y), self.bsize, hook=hook)

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

            for i in self.buttons.values():
                i.draw(img)

        self.menu_button.draw(img)
        win.blit(img, Menu.pos)
