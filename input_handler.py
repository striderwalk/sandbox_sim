import pygame
from conts import *
from  objects.fountain import Fountain
from sandbox import Box
from random import randint
def handle(mouse,board,selection, index, pause):


    keys = pygame.key.get_pressed()
    # scroll options
    if keys[pygame.K_LEFT]:
        selection.shift(-3)
    if keys[pygame.K_RIGHT]:
        selection.shift(3)

    # reset 
    if keys[pygame.K_r]:
        board = Box()
        return "reset"

    # debugging tool
    if keys[pygame.K_q]:
        # ensure all particle know their pos
        board.fix()
        # show type of particle clicked
        val = mouse.get_pos()
        if val[0] == "BOX":
            x, y = val[1:]
            print(board.board[y, x], f" really at {x=}, {y=}")

    if keys[pygame.K_e]:
        val = mouse.get_pos()
        if val[0] == "BOX":
            x, y= val[1:]
            board.board[y][x] = Fountain(x, y, particles[index])
            # end neighbours
            for _, other in board.board[y][x].get_neighbours(board.board, mouse.size):
                board.board[other.y][other.x] = Fountain(other.x, other.y, particles[index])
        

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

            if event.key == pygame.K_LSHIFT:
                if pause:
                    return "play"     
                else:
                    return "stop"


        if event.type == pygame.QUIT:
            pygame.quit()
            return "end"
            
        # change press size
        if event.type == pygame.MOUSEBUTTONDOWN:
            # up 
            if event.button == 4:
                mouse.scale(1)
            if event.button == 5:
                mouse.scale(-1)

    return index