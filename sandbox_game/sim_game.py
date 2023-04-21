import itertools
import logging

import pygame

import errors
import settings
from conts import (
    BLACK,
    CELL_HEIGHT,
    CELL_WIDTH,
    COLS,
    FPS,
    LOWER_BOARDER,
    ROWS,
    WIDTH,
    YOFFSET,
)
from sandbox import Box, update_sim

from .draw import draw_board
from .game import Game
from .input_handler import input_handle

# are all of the imports used? yes
# are they really necessary? ...probaly not
# am I going to do anything? definitely not...


def get_sub_win(win, board):
    draw_board(win, board.board)
    image = win.subsurface((0, 0, WIDTH, LOWER_BOARDER)).copy()
    logging.info("captured image of board")
    return image


def update(frame, win, clock, game, board, event_handlers):

    events = []

    # make frame num stable if paused
    frame -= game.pause_time

    # draw sim -------------------------------->
    surf = pygame.Surface((COLS * CELL_WIDTH, ROWS * CELL_HEIGHT))
    draw_board(surf, board.board)
    win.blit(surf, (0, YOFFSET))

    _events = game.update(win, board)
    events.extend(_events)

    # handle input -------------------------------->
    _events = input_handle(game)
    events.extend(_events)

    if not settings.pause.value or events:
        logging.debug(f"{events=}")

    # check for board reset
    if settings.reset_board.value:
        events.append({"handler": "main", "type": "reset"})
        settings.reset_board.toggle()

    sim_events = []
    for event in events:
        handler = event["handler"]
        if handler == "main":
            if event["type"] == "reset":  # reset game
                board.reset()
                game.pause_time += frame  # set frames to 0
                pygame.event.get()

            elif event["type"] in ["end", "menu"]:  # quit
                settings.showtemp.reset()
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
        elif handler == "sim":
            sim_events.append(event)
        else:
            event_handlers[handler](event)

    if not settings.sim_running.value:
        return {
            "type": "menu",
            "board": board,
            "img": get_sub_win(win, board),
        }

    # update sim -------------------------------->
    pos = game.mouse.get_pos()
    mouse_pos = pos[1:] if pos[0] == "BOX" else None
    update_sim(board, sim_events, mouse_pos, settings.pause.value)

    # update screen -------------------------------->
    pygame.display.set_caption(f"Sandbox | fps={clock.get_fps():.2f}")
    pygame.display.flip()
    win.fill(BLACK)
    clock.tick(FPS)


def run_sim(win, slot=(0, "empty"), index=0, size=3):
    """handle the game, its not that hard"""

    settings.sim_running.set(True)

    save_slot, board_data = slot

    # setup -------------------------------->
    clock = pygame.time.Clock()
    game = Game(size, index, slot=save_slot)
    board = Box(board_data)

    event_handlers = {
        "settings": lambda event: settings.handle_event(event),
        "selection": lambda event: game.handle_event(event),
    }

    # main loop -------------------------------->

    for frame in itertools.count():
        if return_dat := update(frame, win, clock, game, board, event_handlers):
            return return_dat
