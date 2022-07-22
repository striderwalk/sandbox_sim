from  objects.fountain import Fountain
from mouse import Mouse
from selection import Selection
import itertools
import pygame
from pygame.locals import *
from random import randint
from sandbox import Box

        

from conts import *

particles = [i[1] for i in getmembers(objects, isclass)]
particles.remove(objects.Particle)

def main(RAIN=True, index=0, size=30, timeing=False):



    # setup pygame
    pygame.init()
    clock = pygame.time.Clock()
    flags = DOUBLEBUF
    win = pygame.display.set_mode((WIDTH,HEIGHT), flags, 16)

    win.set_alpha(False)
    pygame.event.set_allowed([QUIT, KEYDOWN, MOUSEBUTTONDOWN])
    pygame.display.set_caption("SandBox")
    font = pygame.font.SysFont(None, 24)

    

    # setup board
    board = Box()
    mouse = Mouse(size)
    selection = Selection(index)

    # make it rain
    if RAIN and not timeing:
        for _ in range(1500):            
            y,x = randint(0,ROWS-1),randint(0,COLS-1) 
            board.add_particle(x,y, objects.Water)

    if timeing:
        step = len(board.board[0])//len(particles)
        index = 0
        for j in range(len(board.board[0])-15):
            for i in range(0, len(board.board)):
                board.add_particle(j, i, particles[index])

            if (j % step) == 0: index += 1 
                

    # main loop 
    counter = itertools.count()
    for fnum in counter:
        # print(board.debug())

        board.update(win, fnum)
        if type(val := mouse.update(win, board, index)) == int:
            index = val
        index = selection.update(win, index)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                if timeing: 
                    return 
                else:
                    exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    for _ in range(1500):
                        y,x = randint(0,ROWS-1),randint(0,COLS-1) 
                        board.add_particle(x,y,objects.Water, strict=True)

                # reset 
                if event.key == pygame.K_r:
                    board = Box()
                    main(RAIN=False, index=selection.index, size=mouse.size)


                # debuging tool
                if event.key == pygame.K_q:
                    # ensure all particle know their pos
                    board.fix()
                    # show type of particle clicked
                    val = mouse.get_pos()
                    if val[0] == "BOX":
                        x, y = val[1:]
                        print(board.board[y, x], (x,y))

                if event.key == pygame.K_e:
                    val = mouse.get_pos()
                    if val[0] == "BOX":
                        x, y= val[1:]
                        board.board[y][x] = Fountain(x, y, particles[index])
                        # set neighbours
                        for _, other in board.board[y][x].get_neighbours(board.board, mouse.size):
                            board.board[other.y][other.x] = Fountain(other.x, other.y, particles[index])
                    

                    
                # select next item
                if event.key == pygame.K_TAB:
                    index = (index + 1) % len(particles)
                # select proir item
                if event.key == pygame.K_LCTRL:
                    index = (index - 1) % len(particles)

            # change press size
            if event.type == pygame.MOUSEBUTTONDOWN:
                # up 
                if event.button == 4:
                    mouse.scale(1)
                if event.button == 5:
                    mouse.scale(-1)


        img = font.render(f"{fnum}, fps={round(clock.get_fps(), 3)}", True, (0, 0, 0))
        win.blit(img, (30, 30))


        pygame.display.flip()
        win.fill((255,255,255))
        clock.tick(30)


if __name__ == '__main__':
    main()
       
