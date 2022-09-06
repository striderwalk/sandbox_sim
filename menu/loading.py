import pygame
import math
from random import randint
from conts import WIDTH, HEIGHT

"""
 loading screen for transitions
 not needed for ascetics
"""


def run(win, time=100000, slot_text=None):
    # init pygame stuff
    font = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()

    # if slot info
    if slot_text is not None:
        slot_text = font.render(slot_text, True, (0, 0, 0))
        slot_size =  slot_text.get_size()

    # render loading text
    loading_text = font.render("LOADING ", True, (160, 0, 0))
    size = loading_text.get_size()

    # angle betwwen loading dot cirle thing
    theata = 0
    dtheata = math.pi / 10

    # find run time
    # can be specfied but look bad if to lower than 15
    run_time = min(15, time)
    for i in range(run_time):
        win.fill((255, 255, 255))
        # draw loading circle dots thing
        # colour used to fade dots
        colour = 150
        raidus = 15
        for i in range(8):
            # find pos of dot
            x = raidus * math.cos(theata - i * dtheata) + ((WIDTH + size[0]) / 2) + 20
            y = raidus * math.sin(theata - i * dtheata) + ((HEIGHT) / 2)
            pygame.draw.circle(win, (colour, colour, colour), (x, y), 4)
            colour += 10
            # raidus change cus it look better
            raidus += 0.5
        theata += dtheata
        # draw text
        win.blit(loading_text, ((WIDTH - size[0]) / 2, (HEIGHT - size[1]) / 2))
        if slot_text is not None:
            win.blit(slot_text, ((WIDTH - slot_size[0]) / 2, (HEIGHT - slot_size[1]) / 2 +  size[1]*1.4))
        # update screen
        pygame.display.flip()
        clock.tick(30)

        # handle exiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
