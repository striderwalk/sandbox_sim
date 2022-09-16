import pygame
import logging
from .objects.fountain import Fountain
from .sandbox import Box
from .get_particles import particles


def input_handle(mouse, board, selection, index):
    mouse_val = mouse.get_pos()
    keys = pygame.key.get_pressed()
    # scroll options
    if keys[pygame.K_LEFT]:
        selection.shift(-3)
    if keys[pygame.K_RIGHT]:
        selection.shift(3)

    if keys[pygame.K_j]:
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            for _, other in board.board[y][x].get_neighbours(board.board, mouse.size):
                other.temp += 30
    if keys[pygame.K_k]:
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            for _, other in board.board[y][x].get_neighbours(board.board, mouse.size):
                other.temp -= 30
      
    # reset
    if keys[pygame.K_r]:
        board = Box("empty")
        return "reset"

    # debugging tool
    if keys[pygame.K_q]:
        # ensure all particle know their pos
        board.fix()
        # show type of particle clicked
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            logging.info(f"{board.board[y, x]} really at {x=}, {y=}")

    if keys[pygame.K_e]:
        if mouse_val[0] == "BOX":
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
                return "toggle_play"
            if event.key == pygame.K_ESCAPE:
                return "menu"

            if event.key == pygame.K_RETURN:
                return "update"

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
