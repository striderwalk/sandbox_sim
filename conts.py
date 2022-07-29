import objects
from inspect import getmembers, isclass


def sort_by_state(particles: list) -> list:
    # objects.Particle not type
    # objects.Air essentially empty
    types = [i for i in particles if len(i.__bases__) == 1 and i != objects.Particle and i != objects.Air]

    sorted_types = {}
    for i in types: sorted_types[i] = []
    for i in particles:
        # make sure not base type or Air
        if i in types or i == objects.Air or i == objects.Particle:
            continue
        try:
            sorted_types[i.__bases__[1]].append(i)
        except Exception as e:
            print(i)
            raise e

    particles = []
    for i in sorted_types:
        # turn to alphabetical order
        sorted_particles = sorted_types[i]
        sorted_particles.sort(key=lambda x: ord(x.__name__[0]))
        particles.extend(sorted_particles)
    particles.insert(0, objects.Air)
    return particles

_particles = [i[1] for i in getmembers(objects, isclass)]
particles = sort_by_state(_particles)


# all constants
WIDTH, HEIGHT = 775,700
LOWER_BOARDER = 75
CELL_WIDTH, CELL_HEIGHT = 5,5
COLS = WIDTH//CELL_WIDTH
ROWS = (HEIGHT-LOWER_BOARDER)//CELL_HEIGHT
