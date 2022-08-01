from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import sim
from conts import WIDTH, HEIGHT
import loading
import menu


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), 16)
    pygame.display.set_caption("SandBox")
    menu.run(win)
    loading.run(win)
    while True:
        if (res := sim.run_sim(win))["menu"]:
            loading.run(win)
            menu.run(win)


if __name__ == "__main__":
    main()
