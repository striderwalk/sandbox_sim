from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from sandbox import run_sim
from conts import WIDTH, HEIGHT
from menu import loading, menu, save, end


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), 16)
    pygame.display.set_caption("SandBox")
    pygame.mouse.set_visible(False)
    slot = menu(win)
    loading(win)
    run = True
    while run:
        if (res := run_sim(win, slot))["type"] == "end":
            loading(win, 5)
            save(win, res["board"], res["img"])
            end()

        elif res["type"] == "menu":
            loading(win)
            save(win, res["board"], res["img"])
            loading(win)
            menu(win)


if __name__ == "__main__":
    main()
loading