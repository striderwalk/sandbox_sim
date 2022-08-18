from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from sandbox import run_sim
from conts import WIDTH, HEIGHT


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    run_sim(win)
    pygame.quit()


if __name__ == "__main__":
    main()
