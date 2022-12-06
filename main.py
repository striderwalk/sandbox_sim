from log import configer_logger
import slots
from menu import loading, menu, save, end
from conts import WIDTH, HEIGHT
import logging
import settings
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

    if debug:  # debugging
        run_sim(win)

    elif profile_board:  # profiling
        slot = (0, "profiling")
    else:  # normal
        slot = menu(win)

    logging.info(f"loaded slot {slot[0]}")
    loading(win, slot_text=f"slot {slot[0]}")

    # main loop ---------------->
    run = True
    while run:
        exit_data = run_sim(win, slot)

        if exit_data["type"] == "end":
            loading(win, 10)
            save(win, exit_data["board"], exit_data["img"])
            end()

        elif exit_data["type"] == "menu":
            loading(win)
            save(win, exit_data["board"], exit_data["img"])
            loading(win)
            slot = menu(win)


def process_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--debug", action="store_true", help="turn on debugging mode"
    )
    parser.add_argument(
        "-i", "--info", action="store_true", help="set logging level to info"
    )
    parser.add_argument(
        "-p",
        "--profile_board",
        action="store_true",
        help="load profiler board (to profile see profile.py)",
    )
    return parser.parse_args()


if __name__ == "__main__":

    args = process_args()
    # setup
    slots.setup()

    # set up logging ------------------------------->
    if args.info:
        configer_logger(logging.INFO)
    elif args.debug:
        configer_logger(logging.DEBUG)

        settings.debug.set(True)

    main(args.debug, args.profile_board)
