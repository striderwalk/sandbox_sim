import itertools
import pygame
from .input_handler import input_handle
from .mouse import Mouse
from .selection import Selection
from .sandbox import Box
from .conts import particles, WIDTH, HEIGHT, LOWER_BOARDER, objects


def get_sub_win(win, board):
    board.draw_particles(win)
    return win.subsurface((0, 0, WIDTH, HEIGHT - LOWER_BOARDER)).copy()


def time():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    run_sim(win, slot=(0, "profiling"))


def run_sim(win, slot=(0, "empty"), RAIN=True, index=0, size=3, pause=False):
    slot, board_data = slot
    # setup pygame

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    # pygame.display.set_allow_screensaver()

    # setupr
    board = Box(board_data)
    mouse = Mouse(size)
    selection = Selection(index)

    # make it rain
    if RAIN and board_data != "profiling":
        board.rain_type(objects.Water)

    pause_time = 0
    # main loop
    counter = itertools.count()
    for fnum in counter:
        # max profile time
        if board_data == "profiling" and fnum >= 300:
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
        res = input_handle(mouse, board, selection, index, pause)
        if res == "reset":
            # reset game
            if board_data != "profiling":
                board.reset()
                pause_time += fnum
                pygame.event.get()
            else:
                # profiler cannot reset
                pygame.quit()
                return
        elif res == "end":
            # quit
            if board_data != "profiling":
                return {"type": "end", "board": board, "img": get_sub_win(win, board)}
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
        elif res == "menu":
            return {"type": "menu", "board": board, "img": get_sub_win(win, board)}

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
