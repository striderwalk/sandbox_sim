from log import configer_logger
from slots import setup
from menu import loading, menu, save, end
from conts import WIDTH, HEIGHT
import logging
from sandbox_game import run_sim
import pygame
import argparse
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def main(debug=False, profile_board=False):
    """this is a mess and this docstring is not useful"""
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("SandBox")
    pygame.mouse.set_visible(False)

    if debug:
        run_sim(win)

    # normal game
    if not profile_board:
        slot = menu(win)
    else:
        slot = (0, "profiling")
    logging.info(f"loaded slot {slot[0]}")
    loading(win, slot_text=f"slot {slot[0]}")
    run = True
    while run:
        if (res := run_sim(win, slot))["type"] == "end":
            loading(win, 10)
            save(win, res["board"], res["img"])
            end()

        elif res["type"] == "menu":
            loading(win)
            save(win, res["board"], res["img"])
            loading(win)
            slot = menu(win)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--debug", action="store_true", help="turn on debugging mode"
    )
    parser.add_argument(
        "-i", "--info", action="store_true", help="set logging level to info"
    )
    parser.add_argument("-p", "--profile_board", action="store_true",
                        help="load profiler board (to profile see profile.py)")
    args = parser.parse_args()

    # setup
    setup()
    # run
    if args.info:
        configer_logger(logging.INFO)
    elif args.debug:
        configer_logger(logging.DEBUG)

    main(args.debug, args.profile_board)
