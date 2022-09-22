import pygame
import logging
from sandbox.objects.fountain import Fountain
from sandbox import particles

result_map ={
    pygame.K_LSHIFT: {
        "handler": "main",
        "type": "toggle_play"
    },
    pygame.K_ESCAPE: {
        "handler": "main",
        "type": "menu"
    },
    pygame.K_RETURN: {
        "handler": "main",
        "type": "update"
    },
    pygame.K_t: {
        "handler": "main",
        "type": "temp"
    },
    pygame.K_r: {
        "handler": "main",
        "type": "reset"
    },

    pygame.K_q: {
        "handler": "sim",
        "type": "fix"
    },
}


def process_events(events, mouse, index):
    result = None

    for event in events:
        #################
        # refactor this #
        #################
        if event.type == pygame.QUIT:
             result =  {"handler": "main", "type" : "end"}

        if event.type == pygame.KEYDOWN:
            # select next item
            if event.key == pygame.K_TAB:
                index = (index + 1) % len(particles)
            # select prior item
            elif event.key == pygame.K_LCTRL:
                index = (index - 1) % len(particles)
            
            elif event.key == pygame.K_SPACE:
                result = {"handler": "sim", "type" : "rain", "value" : particles[index]}

            elif event.key in result_map:
                # get rid of endless elif
                result = result_map[event.key]

        # change press size
        if event.type == pygame.MOUSEBUTTONDOWN:
            # up
            if event.button == 4:
                mouse.scale(1)
            if event.button == 5:
                mouse.scale(-1)

    return result, index

def input_handle(mouse, board, selection, index):
    mouse_val = mouse.get_pos()
    keys = pygame.key.get_pressed()
    clicks = []
    # scroll options
    if keys[pygame.K_LEFT]:
        selection.shift(-3)
    if keys[pygame.K_RIGHT]:
        selection.shift(3)

    if keys[pygame.K_j]:
        clicks.append({"handler": "sim", "type" : "heat", "value" : [ 50, mouse.size]})

    if keys[pygame.K_k]:
        clicks.append({"handler": "sim", "type" : "heat", "value" : [-50, mouse.size]})



    if keys[pygame.K_e]:
        # place fountain
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            clicks.append({"handler": "sim", "type" : "press", "value" : (mouse.size, x, y, Fountain,False, particles[index])})

    result, index = process_events(pygame.event.get(), mouse, index)

    

    return index, clicks, result
