from  objects.fountain import Fountain
from mouse import Mouse
from selection import Selection
import itertools
import pygame
from pygame.locals import *
from random import randint
from sandbox import Box
from input import handle_input

        

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
        step = (len(board.board)+23)//len(particles)
        index_d = 0
        print(particles)
        for i in range(len(board.board)):
            for j in range(len(board.board)+23):
                index_d = (j // step) 
                try:
                    board.add_particle(j, i, particles[index_d])
                except IndexError:
                    pass


                
    # main loop 
    counter = itertools.count()
    for fnum in counter:
        # print(board.debug())

        board.update(win, fnum)
        if type(val := mouse.update(win, board, index)) == int:
            index = val
        index = selection.update(win, index)
        if (res := handle_input(mouse,board,selection, index)) == "end":
            if not timeing:
                main(RAIN=False, index=selection.index, size=mouse.size)
            else:
                return
        elif res == "dead":
            if not timeing:
                exit()
            else:
                return
        elif type(res) == int:
            index = res
        img = font.render(f"{fnum}, fps={round(clock.get_fps(), 3)}", True, (0, 0, 0))
        win.blit(img, (30, 30))


        pygame.display.flip()
        win.fill((255,255,255))
        clock.tick()


if __name__ == '__main__':
    # this comment is not needed
    main()
       
