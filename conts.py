import objects
from inspect import getmembers, isclass

particles = [i[1] for i in getmembers(objects, isclass)]
particles.remove(objects.Particle)
# swap air, acid
particles[0], particles[1] = particles[1], particles[0]


# all constants
WIDTH, HEIGHT = 775,700
LOWER_BOARDER = 75
CELL_WIDTH, CELL_HEIGHT = 5,5
COLS = WIDTH//CELL_WIDTH
ROWS = (HEIGHT-LOWER_BOARDER)//CELL_HEIGHT
