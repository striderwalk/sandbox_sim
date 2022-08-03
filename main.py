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
            loading.run(win, 5)
            save.run(win, res["board"], res["img"])
            pygame.quit()
            run = False
        elif res["type"] == "menu":
            loading.run(win)
            save.run(win, res["board"], res["img"])
            loading.run(win)
            menu.run(win)

        from objects.water import done as done
        done()


if __name__ == "__main__":
    main()
