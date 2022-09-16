import pygame
import itertools
import logging
from .input_handler import input_handle
from .mouse import Mouse
from .selection import Selection
from .sandbox import Box
from conts import WIDTH, HEIGHT, LOWER_BOARDER, FPS
from .get_particles import particles, objects


def get_sub_win(win, board):
    board.draw_particles(win)
    image = win.subsurface((0, 0, WIDTH, HEIGHT - LOWER_BOARDER)).copy()
    logging.info("captured image of board")
    return image


def time():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.HIDDEN)
    logging.info("running sim in profiling mode")
    run_sim(win, slot=(0, "profiling"))



def run_sim(win, slot=(0, "empty"), RAIN=False, index=0, size=3, pause=False, show_temp=False):
    slot, board_data = slot
    profiling = type(board_data) == str and board_data == "profiling"
    # setup pygame

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    # pygame.display.set_allow_screensaver()

    # setup
    board = Box(board_data)
    mouse = Mouse(size)
    selection = Selection(index)
    # make it rain
    if RAIN and not profiling:
        board.rain_type(objects.Water)

    pause_time = 0
    # main loop
    counter = itertools.count()
    for fnum in counter:
        # max profile time
        if profiling and fnum >= 200:
            pygame.quit()
            return

        # make frame num stable if paused
        fnum -= pause_time
        if pause:
            pause_time += 1

        # print(board.debug())
        # update particles
        board.update(win, fnum, pause, show_temp)
        # mouse input
        if type(val := mouse.update(win, board, index)) == int:
            index = val
        # update index
        index = selection.update(win, index)
        # handle input
        result = input_handle(mouse, board, selection, index)
        if result == "reset":
            # reset game
            if not profiling:
                board.reset()
                pause_time += fnum # set frames to 0
                pygame.event.get()
            else:
                # profiler cannot reset
                logging.error("board reset attempted in profiling modes")
                pygame.quit()
                return
        elif result == "end":
            # quit
            if not profiling:
                return {"type": "end", "board": board, "img": get_sub_win(win, board)}
            else:
                pygame.quit()
                return
        elif result == "toggle_play":
            # pause game
            pause = not pause
        elif type(result) == int:
            # set new index
            index = result
        elif result == "menu":
            return {"type": "menu", "board": board, "img": get_sub_win(win, board)}
        elif result == "temp":
            show_temp = not show_temp
        elif result == "update":
            pause_time -= 1
            board.update(win, fnum+1, False, show_temp)
        else:
            logging.error(f"invalid result from input_handler of {result}")


        # display game data
        text = f"{fnum}, fps={round(clock.get_fps(), 3)}"
        colour = [255*int(show_temp) for i in range(3)] 
        fps_text = font.render(text, True, colour)
        win.blit(fps_text, (30, 30))
        if pause:
            paused_text = font.render("paused", True, (255, 0, 0))
            win.blit(paused_text, (WIDTH - paused_text.get_size()[0] - 10, 30))

        # update screen
        pygame.display.flip()

        win.fill((255, 255, 255))

        if not pause:
            clock.tick(FPS)
