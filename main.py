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

    
def main(RAIN=True, index=0, size=30, timeing=False, pause = False):

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
        for i in range(len(board.board)):
            for j in range(len(board.board)+23):
                index_d = (j // step)
                if j % step == 0:
                    board.add_particle(j, i, objects.Stone, health=1000000)
                    continue
                try:
                    board.add_particle(j, i, particles[index_d])
                except IndexError:
                    pass



    pause_time = 0
    # main loop 
    counter = itertools.count()
    for fnum in counter:
        if timeing and fnum >= 400: return 
        fnum -= pause_time
        if pause:
            pause_time += 1
        # print(board.debug())

        board.update(win, fnum, pause)
        if type(val := mouse.update(win, board, index)) == int:
            index = val
        index = selection.update(win, index)
        if (res := handle_input(mouse,board,selection, index, pause)) == "end":
            if not timeing:
                main(RAIN=False, index=selection.index, size=mouse.size, pause=pause)
            else:
                return
        elif res == "dead":
            if not timeing: exit()
            else: return
        # play pause    
        elif res == "stop": pause = True

        elif res == "play": pause = False
        elif type(res) == int:
            index = res
        img = font.render(f"{fnum}, fps={round(clock.get_fps(), 3)}", True, (0, 0, 0))
        win.blit(img, (30, 30))
        if pause:
            img = font.render(f"paused", True, (255, 0, 0))
            win.blit(img, (WIDTH-img.get_size()[0]-10, 30))


        pygame.display.flip()
        win.fill((255,255,255))
        if not pause: clock.tick(30)


if __name__ == '__main__':
    # this comment is not needed
    main()
       
