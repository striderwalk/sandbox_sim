import logging
import pygame
import sys


def end(*args):
    logging.info("exiting, bye!")
    pygame.quit()
    sys.exit()
