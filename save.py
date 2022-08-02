from slot_selection import Slots
from menu_button import Button
from conts import WIDTH, HEIGHT
from get_slot import save_slot
import pygame
"""
GUI for saving board

"""



def run(win, board, img):
    # pygame setup
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    # slots
    index = 0
    slots = Slots()

    menu_buttons = [Button(WIDTH / 2 - 150, HEIGHT / 2 - 62, 300, 60, "save board", save_slot),
                    Button(WIDTH / 2 - 150, HEIGHT / 2 +  1, 300, 60, "don't save", lambda x,y,z:None)]
    while True:
        win.fill((255,255,255))
        for i, button in enumerate(menu_buttons):
            button.draw(win)
            if res := button.check_click():
                return index, res(board, index, img)

        index = slots.update(win, index)

        # mouse
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 0, 255), pos, 5)


        pygame.display.flip()
        clock.tick(60)