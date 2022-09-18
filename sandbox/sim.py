import pygame
import itertools
import logging

from .sandbox import Box
from .objects import Stone, Air
from .objects.fountain import Fountain
from .get_particles import particles, objects





def update_sim(board, fnum, events):
    board.update(fnum)

    for event in events:
        if event["type"] == "press":
            board.press(*event["value"])
        elif event["type"] == "rain":
            board.rain_type(event["value"])

    return board




