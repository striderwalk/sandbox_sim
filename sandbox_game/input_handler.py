import pygame
import logging
from sandbox.objects.fountain import Fountain
from sandbox import particles

result_map = {
pygame.K_LSHIFT:  {"type" : "toggle_play"},
pygame.K_ESCAPE:  {"type" : "menu"},
pygame.K_RETURN:  {"type" : "update"},
pygame.K_t:  {"type" : "temp"},
pygame.K_r:  {"type" : "reset"},
}


def process_events(events, mouse, index):
    result = None

    for event in events:
        #################
        # refactor this #
        #################
        if event.type == pygame.QUIT:
             result =  {"type" : "end"}

        if event.type == pygame.KEYDOWN:
            # select next item
            if event.key == pygame.K_TAB:
                index = (index + 1) % len(particles)
            # select prior item
            elif event.key == pygame.K_LCTRL:
                index = (index - 1) % len(particles)
            
            elif event.key == pygame.K_SPACE:
                result = {"type" : "rain", "value" : particles[index]}

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
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            mouse.heat_cells(board.board, x, y, 100)
    if keys[pygame.K_k]:
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            mouse.heat_cells(board.board, x, y, -100)

    # debugging tool
    if keys[pygame.K_q]:
        # ensure all particle know their pos
        board.fix()
        # show type of particle clicked
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            logging.info(f"{board.board[y, x]} really at {x=}, {y=}")

    if keys[pygame.K_e]:
        # place fountain
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            clicks.append({"type" : "press", "value" : (mouse.size, x, y, Fountain,False, particles[index])})

    result, index = process_events(pygame.event.get(), mouse, index)

    

    return index, clicks, result
