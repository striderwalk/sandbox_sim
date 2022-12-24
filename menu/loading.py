import math

import pygame

import fonts
from conts import FPS, HEIGHT, WHITE, WIDTH

"""
 loading screen for transitions
 not needed for ascetics
"""


def run(win, time=100000, slot_text=None):
    # init pygame stuff
    font = fonts.get_font(50)

    clock = pygame.time.Clock()

    # if slot info
    if slot_text is not None:
        slot_text = font.render(slot_text, False, (0, 0, 0))
        slot_size = slot_text.get_size()

    # render loading text
    loading_text = font.render("LOADING ", False, (160, 0, 0))
    size = loading_text.get_size()

    # angle between loading dot circle thing
    theata = 0
    dtheata = math.pi / 10

    # find run time
    # can be specified but look bad if to lower than 15
    run_time = min(15, time)
    for i in range(run_time):
        win.fill(WHITE)
        # draw loading circle dots thing
        # colour used to fade dots
        colour = 150
        raidus = 15
        for i in range(8):
            # find pos of dot
            angle = theata - i * dtheata
            x = raidus * math.cos(angle) + ((WIDTH + size[0]) / 2) + 20
            y = raidus * math.sin(angle) + ((HEIGHT) / 2)
            pygame.draw.circle(win, (colour, colour, colour), (x, y), 4)
            colour += 10
            # radius change -> it looks better
            raidus += 0.5
        theata += dtheata
        # draw text
        win.blit(loading_text, ((WIDTH - size[0]) / 2, (HEIGHT - size[1]) / 2))
        if slot_text is not None:
            _x = (WIDTH - slot_size[0]) / 2
            _y = (HEIGHT - slot_size[1]) / 2 + size[1] * 1.4
            win.blit(slot_text, (_x, _y))

        # update screen
        pygame.display.flip()
        clock.tick(FPS)

        # handle exiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
