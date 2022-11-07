import sys
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from sandbox_game import run_sim
import logging
from conts import WIDTH, HEIGHT
from menu import loading, menu, save, end
from slots import setup
from log import configer_logger


######################## A mess ##############################
def main(debug=False):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("SandBox")
    pygame.mouse.set_visible(False)

    if debug:
        run_sim(win)
    # normal game
    slot = menu(win)
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


###############################################################

if __name__ == "__main__":
    # setup
    setup()

    # run
    if len(sys.argv) > 1 and sys.argv[1] == "--debug":
        configer_logger(logging.INFO)
        main(debug=True)
    main(debug=False)
