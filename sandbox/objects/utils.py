import json
from random import randint

with open("./assets/colour_data.json") as file:
    dat = json.load(file)

HEAT_MAP = dat["HEAT_MAP"]
FIRE_COLOURS = dat["FIRE_COLOURS"]


def update_colour(colour):
    """randomly change rbg colour values (only when asked)"""
    colour = tuple(colour)
    r = (colour[0] + randint(-5, 5)) % 255
    g = (colour[1] + randint(-5, 5)) % 255
    b = (colour[2] + randint(-5, 5)) % 255
    return r, g, b


def find_heatmap_colour(temperature):
    temperature += 25
    temperature = min(len(HEAT_MAP)-1, int(temperature))
    if temperature < 0:
        return (0, 0, 0)
    return HEAT_MAP[temperature]
