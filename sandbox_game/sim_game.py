import pygame
import itertools
import logging
from sandbox import Box, update_sim
from sandbox.objects.fountain import Fountain
from sandbox.get_particles import particles, objects
from sandbox.objects import Stone, Air
from sandbox.objects.fountain import Fountain
from .input_handler import input_handle
from .mouse import Mouse
from .selection import Selection
from conts import WIDTH, HEIGHT, LOWER_BOARDER, FPS, ROWS, COLS, CELL_WIDTH, CELL_HEIGHT

def get_sub_win(win, board):
    draw_board(win, board)
    image = win.subsurface((0, 0, WIDTH, HEIGHT - LOWER_BOARDER)).copy()
    logging.info("captured image of board")
    return image


def time():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.HIDDEN)
    logging.info("running sim in profiling mode")
    run_sim(win, slot=(0, "profiling"))

def draw_board(win, board, show_temp=False, show_fountain=True):
    # draw all particles
    for i, row in enumerate(board.board):
        for j, val in enumerate(row):
            # if air not dawn to save time
            if not show_temp:
                options = [Fountain, Air]
            else:
                options = [Fountain]
            if type(val) not in options:
                if show_temp:
                    colour = val.temp_colour
                else:
                    colour = val.colour
                try:
                    pygame.draw.rect(
                        win,
                        colour,
                        [j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT],
                    )
                except ValueError as e:
                    print(val)
                    raise e
            elif type(val) == Fountain:
                if show_fountain:
                    colour = val.colour
                else:
                    colour = val.obj.colour

                pygame.draw.rect(
                    win,
                    colour,
                    [j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT],
                )
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
    clicks = []
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
        draw_board(win, board, show_temp)
        update_sim(board, fnum, clicks)
        # mouse input
        if type(val := mouse.update(win, board.board, index)) == int:
            index = val
        elif type(val) == list:
            clicks = val
        # update index
        index = selection.update(win, index)
        # handle input
        index, _clicks, result = input_handle(mouse, board, selection, index)
        clicks.extend(_clicks)
        if result is None:
            pass
        elif result["type"] == "reset":
            # reset game
            if not profiling:
                board.reset()
                pause_time += fnum  # set frames to 0
                pygame.event.get()
            else:
                # profiler cannot reset
                logging.error("board reset attempted in profiling modes")
                pygame.quit()
                return
        elif result["type"] == "end":
            # quit
            if not profiling:
                return {"type": "end", "board": board, "img": get_sub_win(win, board)}
            else:
                pygame.quit()
                return
        elif result["type"] == "toggle_play":
            # pause game
            pause = not pause
        elif result["type"] == "menu":

            return  {"type": "menu", "board": board, "img": get_sub_win(win, board)}
        elif result["type"] == "temp":
            show_temp = not show_temp
            
        elif result["type"] == "update":
            pause_time -= 1
            board.update(win, fnum + 1, False, show_temp)
        elif result["type"] == "rain":
            clicks.append(result)
        else:
            logging.error("internal event not hadled conseder using pygame events")

        # display game data
        text = f"{fnum}, fps={round(clock.get_fps(), 3)}"
        colour = [255 * int(show_temp) for i in range(3)]
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
