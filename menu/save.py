import pygame
from .slot_selection import Slots
from .menu_button import Button
from .conts import WIDTH, HEIGHT
from .get_slot import save_slot
from .end import end
from .make_buttons import make_menu_buttons

"""
GUI for saving board

"""


def save_exit(*args):
    save_slot(*args)
    end()


def run(win, board, img):
    # pygame setup
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    # slots
    index = 0
    slots = Slots()

    # this should be dinamic
    # i can't be ask tho
    menu_buttons = make_menu_buttons(
        [
            ("save board", save_slot),
            ("don't save", lambda x, y, z: None),
            ("save and exit", save_exit),
        ]
    )

    while True:
        win.fill((255, 255, 255))
        for i, button in enumerate(menu_buttons):
            button.draw(win)
            if res := button.check_click():
                return index, res(board, index, img)

        index = slots.update(win, index)

        # mouse
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 0, 255), pos, 5)

        pygame.display.flip()
        clock.tick(120)
