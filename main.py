import objects
from mouse import Mouse
from selection import Selection
import itertools
import pygame
from pygame.locals import *
from inspect import getmembers, isclass
from random import randint
from sandbox import Box

        

from conts import *

particles = [i[1] for i in getmembers(objects, isclass)]
particles.remove(objects.Particle)

def main(RAIN=True, index=0, size=3, timeing=False):



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
    if RAIN:
        for _ in range(1500):            
            y,x = randint(0,ROWS-1),randint(0,COLS-1) 
            board.add_particle(x,y, objects.Water)
                

    # main loop 
    counter = itertools.count()
    for fnum in counter:
        # print(board.debug())

        index = selection.update(win, index)
        board.update(win, fnum)
        mouse.update(win, board, index)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                if timeing: 
                    return 
                else:
                    return exit()

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
                    val = mouse.get_pos()
                    if val[0] == "BOX":
                        x, y = val[1:]
                        print(board.board[y, x], (x,y))
                    
                        
                # select next item
                if event.key == pygame.K_TAB:
                    index = (index + 1) % len(particles)
                # select proir item
                if event.key == pygame.K_LCTRL:
                    index = (index - 1) % len(particles)


            #scrolling
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
       
