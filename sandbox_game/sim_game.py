import pygame
import itertools
import logging
import fonts
from conts import WIDTH, LOWER_BOARDER, FPS, WHITE, BLACK
import settings
from sandbox import Box, update_sim
from sandbox.get_particles import objects
import errors
from .input_handler import input_handle
from .mouse import Mouse
from .selection import Selection
from .draw import draw_board
from .game import Game

# are all of the imports used? yes
# are they really necessary? ...probaly not
# am I going to do anything? definitely not...

BASE_SURF = pygame.Surface((WIDTH, LOWER_BOARDER))


def get_sub_win(win, board):
    draw_board(win, board)
    image = win.subsurface((0, 0, WIDTH, LOWER_BOARDER)).copy()
    logging.info("captured image of board")
    return image


######### USE **KWARGS #########
def run_sim(win, slot=(0, "empty"), RAIN=False, index=0, size=3, pause=False):
    """handle the game, its not that hard"""

    save_slot, board_data = slot

    # setup pygame stuff
    clock = pygame.time.Clock()
    font = fonts.get_font(24)
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
        if settings.pause.value:
            pause_time += 1

        # draw sim
        surf = BASE_SURF.copy()
        surf.fill(WHITE)
        surf = draw_board(surf, board.board)
        win.blit(surf, (0, 0))
        # draw menu
        game.draw_menu(win)
        # update index
        selection.update(win)

        pos = mouse.get_pos()
        mouse_pos = pos[1:] if pos[0] == "BOX" else None
        _events = mouse.update(
            win, board.board, selection.selected, settings.showmenu.value
        )
        events.extend(_events)

        # handle input
        _clicks, _event = input_handle(mouse, board, selection.selected)
        clicks.extend(_clicks)
        events.extend(_event)
        logging.debug(f"{events=}, {clicks=}")
        for event in events:
            if not isinstance(event, dict):
                raise ValueError(f"{event}")
            if event["handler"] == "sim":
                clicks.append(event)

            elif event["handler"] == "settings":
                settings.handle_event(event)
            elif event["handler"] == "selection":
                selection.handle_event(event)

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

            elif event["type"] == "menu":
                return {
                    "type": "menu",
                    "board": board,
                    "img": get_sub_win(win, board.board),
                }

            elif event["type"] == "update":
                pause_time -= 1
                update_sim(board)
            else:
                raise errors.EventNotHandled(event)

        update_sim(board, clicks, mouse_pos, settings.pause.value)
        # display game data

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
