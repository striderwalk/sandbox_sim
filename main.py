import itertools
import input_handler
from mouse import Mouse
from selection import Selection
from sandbox import Box
from conts import particles, WIDTH, HEIGHT, objects
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


def main(RAIN=True, index=0, size=30, profiling=False, pause=False):
    # setup pygame
    pygame.init()
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIDTH, HEIGHT), 16)
    pygame.display.set_caption("SandBox")
    font = pygame.font.SysFont(None, 24)
    # pygame.display.set_allow_screensaver()

    # setupr
    board = Box()
    mouse = Mouse(size)
    selection = Selection(index)

    # make it rain
    if RAIN and not profiling:
        board.rain_type(objects.Water)
    # profiling board setup
    if profiling:
        step = (len(board.board) + 23) // len(particles)
        index_d = 0
        for i in range(len(board.board)):
            for j in range(len(board.board) + 23):
                index_d = j // step
                if j % step < 2:
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
        # max profile time
        if profiling and fnum >= 400:
            pygame.quit()
            return
        # make frame num stable if paused
        fnum -= pause_time
        if pause:
            pause_time += 1

        # print(board.debug())
        # update particles
        board.update(win, fnum, pause)
        # mouse input
        if type(val := mouse.update(win, board, index)) == int:
            index = val
        # update index
        index = selection.update(win, index)
        # handle input
        if (
            res := input_handler.handle(mouse, board, selection, index, pause)
        ) == "reset":
            # reset game
            if not profiling:
                main(RAIN=False, index=selection.index, size=mouse.size, pause=pause)
            else:
                # profiler cannot reset
                return
        elif res == "end":
            # quit
            if not profiling:
                pygame.quit()
                exit()
            else:
                pygame.quit()
                return
        elif res == "stop":
            # pause game
            pause = True
        elif res == "play":
            # play fame
            pause = False
        elif type(res) == int:
            # set new index
            index = res

        # display game data
        img = font.render(f"{fnum}, fps={round(clock.get_fps(), 3)}", True, (0, 0, 0))
        win.blit(img, (30, 30))
        if pause:
            img = font.render("paused", True, (255, 0, 0))
            win.blit(img, (WIDTH - img.get_size()[0] - 10, 30))

        # update screen
        pygame.display.flip()

        win.fill((255, 255, 255))
        if not pause:
            clock.tick(30)


if __name__ == "__main__":
    # this comment is not needed
    main()
