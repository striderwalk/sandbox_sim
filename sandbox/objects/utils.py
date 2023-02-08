from random import randint


cbase = "#fc9803"
try:
    from colour import Color

    # heatmap
    HEAT_MAP = list(Color("#0000ff").range_to(Color("#ff0000"), 501))
    HEAT_MAP = [[i * 255 for i in colour.rgb] for colour in HEAT_MAP]

    # fire stuff
    base = Color(cbase)
    FIRE_COLOURS = base.range_to(Color("#fc0b03"), 5)
    FIRE_COLOURS = list(FIRE_COLOURS)
    FIRE_COLOURS = [[i * 255 for i in colour.rgb] for colour in FIRE_COLOURS]
except ModuleNotFoundError:  # probaly dont need this module
    HEAT_MAP = [(255, 255, 0) for i in range(600)]
    FIRE_COLOURS = [(255, 0, 0)]


def update_colour(colour):
    """randomly change rbg colour values (only when asked)"""
    colour = tuple(colour)
    r = (colour[0] + randint(-5, 5)) % 255
    g = (colour[1] + randint(-5, 5)) % 255
    b = (colour[2] + randint(-5, 5)) % 255
    return r, g, b


def find_heatmap_colour(temperature):
    return HEAT_MAP[int(min(500, temperature + 100))]
