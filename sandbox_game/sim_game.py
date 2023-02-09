import itertools
import logging

import pygame

import errors
import fonts
import settings
from conts import (
    BLACK,
    CELL_HEIGHT,
    CELL_WIDTH,
    COLS,
    FPS,
    LOWER_BOARDER,
    ROWS,
    WHITE,
    WIDTH,
    YOFFSET,
)
from sandbox import Box, update_sim
from sandbox.get_particles import objects

from .draw import draw_board
from .game import Game
from .input_handler import input_handle
from .mouse import Mouse
from .selection import Selection

# are all of the imports used? yes
# are they really necessary? ...probaly not
# am I going to do anything? definitely not...


def get_sub_win(win, board):
    draw_board(win, board.board)
    image = win.subsurface((0, 0, WIDTH, LOWER_BOARDER)).copy()
    logging.info("captured image of board")
    return image


def run_sim(win, slot=(0, "empty"), index=0, size=3):
    """handle the game, its not that hard"""

    save_slot, board_data = slot

    # setup pygame
    clock = pygame.time.Clock()
    font = fonts.get_font(24)

    # setup sim
    game = Game(size, index, slot=save_slot)
    board = Box(board_data)

    pause_time = 0
    clicks = []
    # main loop -------------------------------->
    for fnum in itertools.count():
        events = []
        clicks = []

        # make frame num stable if paused
        fnum -= pause_time
        if settings.pause.value:
            pause_time += 1

        # draw sim -------------------------------->
        surf = pygame.Surface((COLS * CELL_WIDTH, ROWS * CELL_HEIGHT))
        draw_board(surf, board.board)
        win.blit(surf, (0, YOFFSET))

        _events = game.update(win, board)
        events.extend(_events)

        # handle input -------------------------------->
        _clicks, _event = input_handle(game)
        clicks.extend(_clicks)
        events.extend(_event)

        if not settings.pause.value or clicks or events:
            logging.debug(f"{events=}, {clicks=}")

        for event in events:
            if event["handler"] == "sim":
                clicks.append(event)

            elif event["handler"] == "settings":
                settings.handle_event(event)
            elif event["handler"] == "selection":
                game.handle_event(event)

            elif event["type"] == "reset":  # reset game
                board.reset()
                pause_time += fnum  # set frames to 0
                pygame.event.get()

            elif event["type"] in ["end", "menu"]:  # quit
                return {
                    "type": event["type"],
                    "board": board,
                    "img": get_sub_win(win, board),
                }
            elif event["type"] == "update":
                pause_time -= 1
                update_sim(board)
            else:
                raise errors.EventNotHandled(event)

        pos = game.mouse.get_pos()
        mouse_pos = pos[1:] if pos[0] == "BOX" else None
        update_sim(board, clicks, mouse_pos, settings.pause.value)

        # display game data
        if settings.debug.value:
            text = f"{fnum}, fps={round(clock.get_fps(), 3)}"
            colour = [255 * int(settings.showtemp.value) for i in range(3)]
            fps_text = font.render(text, True, colour)
            win.blit(fps_text, (30, 30))

        if settings.pause.value:
            paused_text = font.render("paused", True, (255, 0, 0))
            win.blit(paused_text, (WIDTH - paused_text.get_size()[0] - 10, 30))

        # update screen
        pygame.display.flip()
        win.fill(BLACK)
        clock.tick(FPS)
