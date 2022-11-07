import pygame
import itertools
import logging
from conts import WIDTH, HEIGHT, LOWER_BOARDER, FPS, WHITE, BLACK
from sandbox import Box, update_sim
from sandbox.get_particles import objects
import errors
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
        events = []
        clicks = []
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
        _events = mouse.update(win, board.board, selection.selected)
        events.extend(_events)
        # update index
        index = selection.update(win)

        # handle input
        _clicks, _event = input_handle(mouse, board, index)
        clicks.extend(_clicks)
        events.extend(_event)
        logging.debug(f"{events=}")
        for event in events:
            if not isinstance(event, dict):
                raise ValueError(f"{event}")
            if event["handler"] == "sim":
                clicks.append(event)

            elif event["handler"] == "game":
                game.handle(event)
            elif event["handler"] == "selection":
                selection.handle(event)

            elif event["type"] == "reset":  # reset game
                board.reset()
                pause_time += fnum  # set frames to 0
                pygame.event.get()

            elif event["type"] == "end":  # quit
                return {
                    "type": "end",
                    "board": board,
                    "img": get_sub_win(win, board.board),
                }

            elif event["type"] == "toggle_play":  # pause game
                game.toggle_pause()

            elif event["type"] == "menu":
                return {
                    "type": "menu",
                    "board": board,
                    "img": get_sub_win(win, board.board),
                }
            elif event["type"] == "temp":
                game.toggle_show_temp()

            elif event["type"] == "update":
                pause_time -= 1
                update_sim(board)
            else:
                raise errors.EventNotHandled(event)

        update_sim(board, clicks, mouse_pos, game.pause)
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
