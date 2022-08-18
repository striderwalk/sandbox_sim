import pygame
from .menu_button import Slot_Button, Button
from .conts import *
from .get_slot import get_saved, load_slot
from .slot_selection import Slots
from .end import end
from .make_buttons import make_menu_buttons

"""
 menu for start of game loop
 allow user:
    to select save
    start game
    end game
    ???clear save slot???

"""


def run(win):
    # pygame setup
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    # save slots
    index = 0
    slots = Slots()
    # make menu buttons
    buttons = make_menu_buttons([("  play  ", load_slot), ("  exit  ", end)])
    while True:
        # clear screen
        win.fill((255, 255, 255))

        # check menu buttons
        for i, button in enumerate(buttons):
            button.draw(win)
            if res := button.check_click():
                return index, res(index)

        index = slots.update(win, index)

        # mouse
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 0, 255), pos, 5)

        pygame.display.flip()
        clock.tick(60)
