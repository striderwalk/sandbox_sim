import pygame
from conts import FPS
from slots import get_saved, load_slot
from buttons import Slots
from end import end
from buttons import make_menu_buttons
from sandbox_game import Background


"""
 menu for start of game loop
 allow user:
    to select save
    start game
    end game
    ???clear save slot???

"""
font = pygame.font.SysFont(None, 24)


def run(win):
    # pygame setup
    clock = pygame.time.Clock()
    # save slots
    index = 0
    slots = Slots(get_saved())
    # make menu buttons
    buttons = make_menu_buttons([("  start  ", load_slot), ("  exit  ", end)])
    background = Background()
    while True:
        # clear screen
        win.fill((255, 255, 255))
        background.update(win)
        # check menu buttons
        for i, button in enumerate(buttons):
            button.draw(win)
            if res := button.check_click():
                return index, res(index)

        index = slots.update(win, index)

        # mouse
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 0, 255), pos, 5)

        clock.tick(FPS)
        text = f"fps={round(clock.get_fps(), 3)}"
        fps_text = font.render(text, True, (0, 0, 0))
        win.blit(fps_text, (30, 30))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return index, buttons[0].click()(index)
