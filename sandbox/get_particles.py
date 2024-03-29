from inspect import getmembers, isclass

import sandbox.objects as objects


def sort_by_state(particles: list) -> list:
    # objects.Particle not type
    # objects.Air essentially empty
    types = [
        i
        for i in particles
        if len(i.__bases__) == 1 and i != objects.Particle and i != objects.Air
    ]

    sorted_types = {}
    for i in types:
        sorted_types[i] = []
    for i in particles:
        # make sure not base type or Air
        if i in types or i == objects.Air or i == objects.Particle:
            continue
        sorted_types[i.__bases__[1]].append(i)

    particles = []
    for i in sorted_types:
        # turn to alphabetical order
        sorted_particles = sorted_types[i]
        sorted_particles.sort(key=lambda x: ord(x.__name__[0]))
        particles.extend(sorted_particles)
    particles.insert(0, objects.Air)
    return particles


_particles = [i[1] for i in getmembers(objects, isclass)]


#### import this ####
particles = sort_by_state(_particles)
#####################
ext_particles = particles + [objects.fountain.Fountain]
