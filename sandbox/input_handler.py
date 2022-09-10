import pygame
import logging
from .objects.fountain import Fountain
from .sandbox import Box
from .get_particles import particles


def input_handle(mouse, board, selection, index, pause):
    keys = pygame.key.get_pressed()
    # scroll options
    if keys[pygame.K_LEFT]:
        selection.shift(-3)
    if keys[pygame.K_RIGHT]:
        selection.shift(3)

    # reset
    if keys[pygame.K_r]:
        board = Box("empty")
        return "reset"

    # debugging tool
    if keys[pygame.K_q]:
        # ensure all particle know their pos
        board.fix()
        # show type of particle clicked
        val = mouse.get_pos()
        if val[0] == "BOX":
            x, y = val[1:]
            logging.info(board.board[y, x], f" really at {x=}, {y=}")

    if keys[pygame.K_e]:
        val = mouse.get_pos()
        if val[0] == "BOX":
            x, y = val[1:]
            # end neighbours
            mouse.press(board, x, y, Fountain, place_obj=particles[index])

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                board.rain_type(particles[index])
            # select next item
            if event.key == pygame.K_TAB:
                index = (index + 1) % len(particles)
            # select prior item
            if event.key == pygame.K_LCTRL:
                index = (index - 1) % len(particles)

            if event.key == pygame.K_t:
                return "temp"

            if event.key == pygame.K_LSHIFT:
                if pause:
                    return "play"
                else:
                    return "stop"
            if event.key == pygame.K_ESCAPE:
                return "menu"

        if event.type == pygame.QUIT:
            return "end"

        # change press size
        if event.type == pygame.MOUSEBUTTONDOWN:
            # up
            if event.button == 4:
                mouse.scale(1)
            if event.button == 5:
                mouse.scale(-1)

    return index
