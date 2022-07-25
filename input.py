import pygame
from conts import *
from  objects.fountain import Fountain
from sandbox import Box
from random import randint
def handle_input(mouse,board,selection, index, pause):


    keys = pygame.key.get_pressed()
    # scroll options
    if keys[pygame.K_LEFT]:
        selection.shift(-3)
    if keys[pygame.K_RIGHT]:
        selection.shift(3)

    # reset 
    if keys[pygame.K_r]:
        board = Box()
        return "end"

    # debuging tool
    if keys[pygame.K_q]:
        # ensure all particle know their pos
        board.fix()
        # show type of particle clicked
        val = mouse.get_pos()
        if val[0] == "BOX":
            x, y = val[1:]
            print(board.board[y, x], (x,y))

    if keys[pygame.K_e]:
        val = mouse.get_pos()
        if val[0] == "BOX":
            x, y= val[1:]
            board.board[y][x] = Fountain(x, y, particles[index])
            # set neighbours
            for _, other in board.board[y][x].get_neighbours(board.board, mouse.size):
                board.board[other.y][other.x] = Fountain(other.x, other.y, particles[index])
        

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                for _ in range(1500):
                    y,x = randint(0,ROWS-1),randint(0,COLS-1) 
                    board.add_particle(x,y,objects.Water, strict=True)
            # select next item
            if event.key == pygame.K_TAB:
                index = (index + 1) % len(particles)
            # select proir item
            if event.key == pygame.K_LCTRL:
                index = (index - 1) % len(particles)

            if event.key == pygame.K_LSHIFT:
                if pause:
                    return "play"     
                else:
                    return "stop"


        if event.type == pygame.QUIT:
            pygame.quit()
            return "dead"
        # change press size
        if event.type == pygame.MOUSEBUTTONDOWN:
            # up 
            if event.button == 4:
                mouse.scale(1)
            if event.button == 5:
                mouse.scale(-1)

    return index