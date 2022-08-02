from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import sim
from conts import WIDTH, HEIGHT
import loading
import menu
import get_slot
import save

def main():
    get_slot.setup()
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), 16)
    pygame.display.set_caption("SandBox")
    pygame.mouse.set_visible(False)
    slot = menu.run(win)
    loading.run(win)
    run = True
    while run:
        if (res := sim.run_sim(win, slot))["type"] == "end":
            save.run(win, res["board"])
            pygame.quit()
            run = False
        elif res["type"] == "menu":
            save.run(win, res["board"])
            loading.run(win)
            menu.run(win)


if __name__ == "__main__":
    main()
