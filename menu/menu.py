import pygame
from conts import *
from slots import get_saved, load_slot
from buttons import Slots
from end import end
from buttons import make_menu_buttons
from sandbox import Background


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
    slots = Slots(get_saved())
    # make menu buttons
    buttons = make_menu_buttons([("  start  ", load_slot), ("  exit  ", end)])
    background = Background()
    while True:
        # clear screen
        win.fill((255, 255, 255))
        background.draw_background(win)
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
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return index, buttons[0].click()(index)



