import pygame
from buttons import Slots
from conts import WIDTH, HEIGHT
from slots import save_slot, get_saved
from end import end
from buttons import make_menu_buttons
from sandbox import Background
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
        win.fill((255, 255, 255))
        background.draw_background(win)
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
        clock.tick(120)
