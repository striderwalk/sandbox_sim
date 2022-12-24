import pygame

from buttons import Slots, make_menu_buttons
from conts import FPS, WHITE
from end import end
from sandbox_game import Background
from slots import get_empty, get_saved, save_slot

"""
GUI for saving board

"""


def save_exit(*args):
    save_slot(*args)
    end()


def run(win, board, img):
    # pygame setup
    clock = pygame.time.Clock()
    # slots
    index = get_empty()
    slots = Slots(get_saved())

    menu_buttons = make_menu_buttons(
        [
            ("save board", save_slot),
            ("don't save", lambda x, y, z: None),
            ("save and exit", save_exit),
        ]
    )

    background = Background()

    while True:
        win.fill(WHITE)
        background.update(win)
        for i, button in enumerate(menu_buttons):
            button.draw(win)
            # handle clicks
            if res := button.check_click():
                return index, res(board, index, img)

        index = slots.update(win, index)

        # draw cursor
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 0, 255), pos, 5)

        pygame.display.flip()
        clock.tick(FPS)
