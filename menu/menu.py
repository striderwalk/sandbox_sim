import pygame

import fonts
from buttons import Slots, make_menu_buttons
from conts import FPS, WHITE
from end import end
from sandbox_game import Background
from slots import get_saved, load_slot

"""
 menu for start of game loop
 allow user:
    to select save
    start game
    end game
    ???clear save slot???

"""

font = fonts.get_font(24)


def run(win):
    # pygame setup
    clock = pygame.time.Clock()
    # save slots
    index = 0
    slots = Slots(get_saved())
    # make menu buttons
    buttons = make_menu_buttons([("  start  ", load_slot), ("  exit  ", end)])
    background = Background()
    while True:
        # clear screen
        win.fill(WHITE)
        background.update(win)
        # check menu buttons
        for button in buttons:
            button.draw(win)
            if res := button.check_click():
                return index, res(index)

        index = slots.update(win, index)

        # mouse
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 0, 255), pos, 5)

        clock.tick(FPS)
        # text = f"fps={round(clock.get_fps(), 3)}"
        pygame.display.flip()

        for event in pygame.event.get():
            if val := process_event(event, index, buttons):
                return val


def process_event(event, index, buttons):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        return index, buttons[0].click()(index)
