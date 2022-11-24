import logging
import pygame
import sys


# handle exiting
def end(*args, **kwargs):
    logging.info("exiting, bye!")
    pygame.quit()
    sys.exit()
