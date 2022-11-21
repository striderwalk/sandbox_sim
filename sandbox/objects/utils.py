from random import randint


def update_colour(colour):
    """ randomly change rbg colour values (only when asked)"""
    colour = tuple(colour)
    r = (colour[0] + randint(-5, 5)) % 255
    g = (colour[1] + randint(-5, 5)) % 255
    b = (colour[2] + randint(-5, 5)) % 255
    return r, g, b
