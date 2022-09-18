import logging
import pygame
import sys


# handle exiting
def end(*args):
    logging.info("exiting, bye!")
    pygame.quit()
    sys.exit()
