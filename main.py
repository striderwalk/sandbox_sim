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
    data = {"RAIN" : True, "index":0,"size":30, "profiling": False, "pause": False}
    while True:
        if (res := sim.run_sim(win, data))["menu"]:
            menu.run(win)
        else:
            for i in res:
                data[i] = res[i]
        loading.run(win)


if __name__ == "__main__":
    main()