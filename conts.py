import objects
from inspect import getmembers, isclass

particles = [i[1] for i in getmembers(objects, isclass)]
particles.remove(objects.Particle)

# all constants
WIDTH, HEIGHT = 700,700
LOWER_BOARDER = 75
CELL_WIDTH, CELL_HEIGHT = 5, 5
COLS = WIDTH//CELL_WIDTH
ROWS = (HEIGHT-LOWER_BOARDER)//CELL_HEIGHT
