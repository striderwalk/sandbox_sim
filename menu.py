import pygame
from menu_button import Slot_Button, Button
from conts import *
from get_slot import get_saved, load_slot
from slot_selection import Slots


def run(win):
    # pygame setup
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    # save slots
    index = 0
    slots = Slots()
    # make menu buttons
    buttons = [Button(WIDTH / 2 - 60, HEIGHT / 2 - 30, 120, 60, "play", load_slot)]
    while True:
        # clear screen
        win.fill((255, 255, 255))
        # mouse
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 0, 255), pos, 5)

        # check menu buttons
        for i, button in enumerate(buttons):
            button.draw(win)
            if res := button.check_click(index):
                return index, res

        index = slots.update(win, index)

        pygame.display.flip()
        clock.tick(60)
