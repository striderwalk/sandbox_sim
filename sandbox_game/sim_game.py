import pygame
import itertools
import logging
from conts import WIDTH, HEIGHT, LOWER_BOARDER, FPS, WHITE, BLACK
from sandbox import Box, update_sim
from sandbox.get_particles import objects
from .input_handler import input_handle
from .mouse import Mouse
from .selection import Selection
from .draw import draw_board
from .game import Game

BASE_SURF = pygame.Surface((WIDTH, HEIGHT - LOWER_BOARDER))


def get_sub_win(win, board):
    draw_board(win, board)
    image = win.subsurface((0, 0, WIDTH, HEIGHT - LOWER_BOARDER)).copy()
    logging.info("captured image of board")
    return image


######### USE **KWARGS #########
def run_sim(win, slot=(0, "empty"), RAIN=False, index=0, size=3, pause=False):
    ################################

    save_slot, board_data = slot
    # setup pygame

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)
    # pygame.display.set_allow_screensaver()

    # setup
    game = Game(slot=save_slot, pause=pause, show_temp=False)
    board = Box(board_data)
    mouse = Mouse(size)
    selection = Selection(index)
    # make it rain
    if RAIN:
        board.rain_type(objects.Water)

    pause_time = 0
    clicks = []
    counter = itertools.count()

    ###### MAIN LOOP #######
    for fnum in counter:
        # make frame num stable if paused
        fnum -= pause_time
        if game.pause:
            pause_time += 1

        # draw
        surf = BASE_SURF.copy()
        surf.fill(WHITE)
        surf = draw_board(surf, board.board, game.show_temp)
        win.blit(surf, (0, 0))

        # mouse input
        pos = mouse.get_pos()
        mouse_pos = pos[1:] if pos[0] == "BOX" else None
        val = mouse.update(win, board.board, index)
        if isinstance(val, int):
            index = val
        elif isinstance(val, list):
            clicks = val

        update_sim(board, clicks, mouse_pos, game.pause)

        # update index
        index = selection.update(win, index)

        # handle input
        index, _clicks, result = input_handle(mouse, board, selection, index)
        clicks.extend(_clicks)
        if result is None:
            pass
        elif result["handler"] == "sim":
            clicks.append(result)

        elif result["type"] == "reset":  # reset game
            board.reset()
            pause_time += fnum  # set frames to 0
            pygame.event.get()

        elif result["type"] == "end":  # quit
            return {
                "type": "end",
                "board": board,
                "img": get_sub_win(win, board.board),
            }

        elif result["type"] == "toggle_play":  # pause game
            game.toggle_pause()

        elif result["type"] == "menu":
            return {
                "type": "menu",
                "board": board,
                "img": get_sub_win(win, board.board),
            }
        elif result["type"] == "temp":
            show_temp = not show_temp

        elif result["type"] == "update":
            pause_time -= 1
            update_sim(board, fnum)
        else:
            logging.error("internal event not handled")

        # display game data
        text = f"{fnum}, fps={round(clock.get_fps(), 3)}"
        colour = [255 * int(game.show_temp) for i in range(3)]
        fps_text = font.render(text, True, colour)
        win.blit(fps_text, (30, 30))
        if game.pause:
            paused_text = font.render("paused", True, (255, 0, 0))
            win.blit(paused_text, (WIDTH - paused_text.get_size()[0] - 10, 30))
        # update screen
        pygame.display.flip()

        win.fill(BLACK)

        clock.tick(FPS)
