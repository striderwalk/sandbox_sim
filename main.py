from sandbox_game import run_sim
from menu import end, loading, menu, save
from log import configer_logger
from conts import HEIGHT, WIDTH
import slots
import settings
import pygame
import argparse
import logging
from os import environ

from slots import load_slot
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


def main(debug, profile_board, slot):
    if slot:
        slot = (int(slot), load_slot(int(slot)))

    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SandBox")
    pygame.mouse.set_visible(False)
    if debug:  # debugging
        if not slot:
            slot = (0, "profiling")

        run_sim(win, slot)

    elif profile_board:  # profiling
        slot = (0, "profiling")
    elif not slot:
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
        help="load profiler board- to profile use profile.py",
    )
    parser.add_argument("-s", "--slot",
                        action="store")

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
    try:
        import colour_util
    except ModuleNotFoundError:
        logging.warning("mdoule colour not found using saved colour values")

    main(args.debug, args.profile_board, args.slot)
